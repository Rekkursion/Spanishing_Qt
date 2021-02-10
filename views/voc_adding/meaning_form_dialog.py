from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy, QButtonGroup

from enums.add_modify_dialog_mode import AddModifyDialogMode
from enums.dialog_result import DialogResult
from enums.part_of_speech import PartOfSpeech
from enums.pref_key import PrefKey
from enums.strs import Strs
from enums.word_variability import WordVariability
from managers.pref_manager import PrefManager
from models.meaning import Meaning, WordForms
from utils import dimension as dim
from utils.word_forms_updater import WordFormsUpdater
from views.list_widgets.example_list.example_list_widget import ExampleListWidget
from views.message_boxes.base_message_box import BaseMessageBox
from views.styled_views.styled import StyledLabel, StyledLineEdit, StyledGridLayout, \
    StyledButton, StyledTextEdit, StyledDialog, StyledComboBox, StyledHBox
from views.styled_views.styled_word_variability_radio_button import StyledWordVariabilityRadioButton
from views.voc_adding.example_form_dialog import ExampleFormDialog


# noinspection PyTypeChecker,PyUnresolvedReferences
class MeaningFormDialog(StyledDialog):
    def __init__(self, dialog_title, vocabulary: str, meaning=None):
        super(MeaningFormDialog, self).__init__(dialog_title)
        # force this dialog being the top form
        self.setWindowModality(Qt.ApplicationModal)
        # the vocabulary
        self.__vocabulary = vocabulary
        # initialize all views
        self.__init_views(meaning)
        # initialize all events
        self.__init_events()
        # resize to a proper one
        self.resize(*dim.meaning_form_dialog_size)
        # initially set the focus on the first line-edit
        self.__le_translation_chi.setFocus()
        # the result-meaning
        self.__result_meaning = None
        # the add-modify-dialog-mode
        self.__dialog_mode = AddModifyDialogMode.A if meaning is None else AddModifyDialogMode.M
        # the word-forms-updater
        self.__forms_updater = WordFormsUpdater(
            self.__grp_gender_variability, 0,
            self.__grp_number_variability, 0,
            self.__le_masculine_singular, self.__le_feminine_singular, self.__le_masculine_plural, self.__le_feminine_plural
        )
        # initially update the word-forms
        self.__event_update_word_forms()

    @property
    def result_meaning(self):
        return self.__result_meaning

    def __init_views(self, meaning):
        # the grid-layout for containing all sub-views
        self.__grid_base = StyledGridLayout()
        # the translation for chinese
        self.__lbl_translation_chi = StyledLabel(Strs.Chinese)
        self.__le_translation_chi = StyledLineEdit(Strs.Voc_Adding_Page_Translation_Chi_Placeholder)
        self.__grid_base.addWidget(self.__lbl_translation_chi, 0, 0, 1, 1)
        self.__grid_base.addWidget(self.__le_translation_chi, 0, 1, 1, 10)
        # the translation for english
        self.__lbl_translation_eng = StyledLabel(Strs.English)
        self.__le_translation_eng = StyledLineEdit(Strs.Voc_Adding_Page_Translation_Eng_Placeholder)
        self.__grid_base.addWidget(self.__lbl_translation_eng, 1, 0, 1, 1)
        self.__grid_base.addWidget(self.__le_translation_eng, 1, 1, 1, 10)
        # the combo-box for selecting the part-of-speech
        self.__comb_pos = StyledComboBox()
        self.__comb_pos.add_items(*list(map(lambda x: x.format(), PartOfSpeech)))
        self.__comb_pos.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored))
        self.__grid_base.addWidget(self.__comb_pos, 0, 11, 2, 5)
        # the radio-buttons for gender-variabilities and their button-group
        self.__lbl_gender_variability = StyledLabel(Strs.Gender_Variability)
        self.__rdb_gender_general = StyledWordVariabilityRadioButton(WordVariability.GENERAL, Strs.Word_Variability_General)
        self.__rdb_gender_special = StyledWordVariabilityRadioButton(WordVariability.SPECIAL, Strs.Word_Variability_Special)
        self.__rdb_gender_invariant = StyledWordVariabilityRadioButton(WordVariability.INVARIANT, Strs.Word_Variability_Invariant)
        self.__grp_gender_variability = QButtonGroup()
        self.__grp_gender_variability.addButton(self.__rdb_gender_general)
        self.__grp_gender_variability.addButton(self.__rdb_gender_special)
        self.__grp_gender_variability.addButton(self.__rdb_gender_invariant)
        self.__hbox_gender_variability = StyledHBox(self.__lbl_gender_variability, self.__rdb_gender_general, self.__rdb_gender_special, self.__rdb_gender_invariant, StyledLabel('    '))
        self.__grid_base.addLayout(self.__hbox_gender_variability, 2, 0, 1, 8)
        self.__rdb_gender_general.setChecked(True)
        # the radio-buttons for number-variabilities and their button-group
        self.__lbl_number_variability = StyledLabel(Strs.Number_Variability)
        self.__rdb_number_general = StyledWordVariabilityRadioButton(WordVariability.GENERAL, Strs.Word_Variability_General)
        self.__rdb_number_special = StyledWordVariabilityRadioButton(WordVariability.SPECIAL, Strs.Word_Variability_Special)
        self.__rdb_number_invariant = StyledWordVariabilityRadioButton(WordVariability.INVARIANT, Strs.Word_Variability_Invariant)
        self.__grp_number_variability = QButtonGroup()
        self.__grp_number_variability.addButton(self.__rdb_number_general)
        self.__grp_number_variability.addButton(self.__rdb_number_special)
        self.__grp_number_variability.addButton(self.__rdb_number_invariant)
        self.__hbox_number_variability = StyledHBox(self.__lbl_number_variability, self.__rdb_number_general, self.__rdb_number_special, self.__rdb_number_invariant, StyledLabel('    '))
        self.__grid_base.addLayout(self.__hbox_number_variability, 2, 8, 1, 8)
        self.__rdb_number_general.setChecked(True)
        # the labels & line-edits for the forms of genders & numbers
        self.__lbl_masculine_singular = StyledLabel(Strs.Masculine_Singular_Placeholder)
        self.__le_masculine_singular = StyledLineEdit(Strs.Masculine_Singular_Placeholder)
        self.__grid_base.addWidget(self.__lbl_masculine_singular, 3, 0, 1, 2)
        self.__grid_base.addWidget(self.__le_masculine_singular, 3, 2, 1, 6)
        self.__lbl_feminine_singular = StyledLabel(Strs.Feminine_Singular_Placeholder)
        self.__le_feminine_singular = StyledLineEdit(Strs.Feminine_Singular_Placeholder)
        self.__grid_base.addWidget(self.__lbl_feminine_singular, 3, 8, 1, 2)
        self.__grid_base.addWidget(self.__le_feminine_singular, 3, 10, 1, 6)
        self.__lbl_masculine_plural = StyledLabel(Strs.Masculine_Plural_Placeholder)
        self.__le_masculine_plural = StyledLineEdit(Strs.Masculine_Plural_Placeholder)
        self.__grid_base.addWidget(self.__lbl_masculine_plural, 4, 0, 1, 2)
        self.__grid_base.addWidget(self.__le_masculine_plural, 4, 2, 1, 6)
        self.__lbl_feminine_plural = StyledLabel(Strs.Feminine_Plural_Placeholder)
        self.__le_feminine_plural = StyledLineEdit(Strs.Feminine_Plural_Placeholder)
        self.__grid_base.addWidget(self.__lbl_feminine_plural, 4, 8, 1, 2)
        self.__grid_base.addWidget(self.__le_feminine_plural, 4, 10, 1, 6)
        # the button for adding example sentences
        self.__btn_add_new_example = StyledButton(Strs.Voc_Adding_Page_New_Example_Sentence_Button_Text)
        self.__btn_add_new_example.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored))
        self.__grid_base.addWidget(self.__btn_add_new_example, 5, 0, 1, 2)
        # the list-widget for containing all added example sentences
        self.__lis_examples = ExampleListWidget()
        self.__grid_base.addWidget(self.__lis_examples, 5, 2, 1, 14)
        # the text-edit for notes
        self.__te_notes = StyledTextEdit(Strs.Voc_Adding_Page_Notes_Placeholder)
        self.__grid_base.addWidget(self.__te_notes, 6, 0, 1, 16)
        # the buttons of cancelling & submitting
        self.__btn_cancel = StyledButton(Strs.Cancel)
        self.__btn_submit = StyledButton(Strs.Submit)
        self.__btn_submit.setEnabled(meaning is not None)
        self.__grid_base.addWidget(self.__btn_cancel, 8, 0, 1, 8)
        self.__grid_base.addWidget(self.__btn_submit, 8, 8, 1, 8)
        # set the base grid-layout as the layout
        self.setLayout(self.__grid_base)
        # initially set the data from the data-model of meaning, if exists
        if meaning is not None and isinstance(meaning, Meaning):
            # set the texts of translations in both chinese & english
            self.__le_translation_chi.setText(meaning.translation_chi)
            self.__le_translation_eng.setText(meaning.translation_eng)
            # set the part-of-speech
            self.__comb_pos.setCurrentText(meaning.pos.format())
            # set the example sentences
            for example in meaning.example_list:
                self.__lis_examples.push_back(vocabulary, data_model=example, max_height=dim.example_list_widget_max_height)
            # set the notes
            self.__te_notes.setText(meaning.notes)
            # set the dialog-mode to modification mode
            self.__dialog_mode = AddModifyDialogMode.M
            # set the focus-point on the line-edit of chinese translation
            self.__le_translation_chi.setFocus()
            self.__grp_gender_variability.buttons()[meaning.forms.gender_variability.value].setChecked(True)
            self.__grp_number_variability.buttons()[meaning.forms.number_variability.value].setChecked(True)
            self.__le_masculine_singular.setText(meaning.forms.get_form(True, True))
            self.__le_feminine_singular.setText(meaning.forms.get_form(False, True))
            self.__le_masculine_plural.setText(meaning.forms.get_form(True, False))
            self.__le_feminine_plural.setText(meaning.forms.get_form(False, False))
        self.__rdb_gender_special.hide()
        self.__rdb_number_special.hide()

    def __init_events(self):
        self.__btn_add_new_example.clicked.connect(self.__event_add_new_example)
        self.__btn_cancel.clicked.connect(self.__event_cancel)
        self.__btn_submit.clicked.connect(self.__event_submit)
        self.__le_translation_chi.textChanged.connect(self.__event_translation_line_edits_changed)
        self.__le_translation_eng.textChanged.connect(self.__event_translation_line_edits_changed)
        self.__comb_pos.currentIndexChanged.connect(self.__event_update_word_forms)
        self.__grp_gender_variability.buttonClicked.connect(self.__event_update_word_forms)
        self.__grp_number_variability.buttonClicked.connect(self.__event_update_word_forms)

    # the event for adding a new example sentence
    def __event_add_new_example(self):
        # prompt up a dialog for filling the info of new example sentence
        dialog = ExampleFormDialog(Strs.Example_Form_Dialog_Title_A, self.__vocabulary).show_and_exec()
        if dialog.result_example is not None:
            self.__lis_examples.push_back(self.__vocabulary, data_model=dialog.result_example, max_height=dim.example_list_widget_max_height)

    # the event for cancelling the action of adding a new meaning
    def __event_cancel(self):
        # if a message-box for warning the user is needed
        if self.__dialog_mode == AddModifyDialogMode.A and PrefManager.get_pref(PrefKey.MSG_BOX_CANCELLING_NEW_MEANING):
            # create & show the dialog to make sure that the user really want to cancel the action for adding it
            if BaseMessageBox.Builder. \
                    init(Strs.Make_Sure_For_Cancelling_Sth_Dialog_Title, PrefKey.MSG_BOX_CANCELLING_NEW_MEANING). \
                    set_content(Strs.Make_Sure_For_Cancelling_Adding_New_Meaning_Dialog_Content).create(). \
                    show_and_exec(). \
                    dialog_result == DialogResult.YES:
                self.close()
        # otherwise, close this meaning-form-dialog directly
        else:
            self.close()

    # the event for submitting the new meaning
    def __event_submit(self):
        # get the selected part-of-speech
        pos = PartOfSpeech.get_pos_by_formatted_text(self.__comb_pos.currentText())
        # get the text of the translation in chinese and in english respectively
        translation_chi = self.__le_translation_chi.text()
        translation_eng = self.__le_translation_eng.text()
        # get the list of example sentences
        example_sentences = self.__lis_examples.get_all_examples()
        # get the notes
        notes = self.__te_notes.toPlainText()
        if translation_chi != '' or translation_eng != '':
            # instantiate a 'word-forms'
            forms = WordForms(self.__grp_gender_variability.checkedButton().word_variability, self.__grp_number_variability.checkedButton().word_variability)
            if self.__le_masculine_singular.isEnabled():
                forms.set_form(self.__le_masculine_singular.text(), True, True)
            if self.__le_feminine_singular.isEnabled():
                forms.set_form(self.__le_feminine_singular.text(), False, True)
            if self.__le_masculine_plural.isEnabled():
                forms.set_form(self.__le_masculine_plural.text(), True, False)
            if self.__le_feminine_plural.isEnabled():
                forms.set_form(self.__le_feminine_plural.text(), False, False)
            # instantiate a meaning as the result
            self.__result_meaning = Meaning(pos, translation_chi, translation_eng, example_sentences, notes, forms)
            print(self.__result_meaning)
            # close the dialog
            self.close()

    # the event for disable/enable the submission button
    def __event_translation_line_edits_changed(self):
        self.__btn_submit.setEnabled(self.__le_translation_chi.text() != '' or self.__le_translation_eng.text() != '')

    # the event for updating the forms for the word according to its selected part-of-speech
    def __event_update_word_forms(self):
        # update forms by the change of part-of-speech or word-variabilities
        self.__forms_updater.update(
            list(PartOfSpeech)[self.__comb_pos.currentIndex()],
            self.__grp_gender_variability.checkedButton().word_variability,
            self.__grp_number_variability.checkedButton().word_variability
        )
        # m_s, f_s, m_pl, f_pl = WordAnalyzer.get_general_forms(self.__vocabulary, list(PartOfSpeech)[self.__comb_pos.currentIndex()])
        # if self.__le_masculine_singular.isEnabled() and self.__le_masculine_singular.text() == '':
        #     self.__le_masculine_singular.setText(m_s)
        # if self.__le_feminine_singular.isEnabled() and self.__le_feminine_singular.text() == '':
        #     self.__le_feminine_singular.setText(f_s)
        # if self.__le_masculine_plural.isEnabled() and self.__le_masculine_plural.text() == '':
        #     self.__le_masculine_plural.setText(m_pl)
        # if self.__le_feminine_plural.isEnabled() and self.__le_feminine_plural.text() == '':
        #     self.__le_feminine_plural.setText(f_pl)
