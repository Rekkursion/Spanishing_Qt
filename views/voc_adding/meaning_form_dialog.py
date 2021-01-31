from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

from enums.Add_Modify_Dialog_Mode import AddModifyDialogMode
from enums.dialog_result import DialogResult
from enums.part_of_speech import PartOfSpeech
from enums.pref_key import PrefKey
from enums.strs import Strs
from managers.pref_manager import PrefManager
from models.meaning import Meaning
from utils import dimension as dim
from views.list_widgets.example_list.example_list_widget import ExampleListWidget
from views.message_boxes.base_message_box import BaseMessageBox
from views.styled_views.styled import StyledLabel, StyledLineEdit, StyledGridLayout, \
    StyledButton, \
    StyledTextEdit, StyledDialog, StyledComboBox
from views.voc_adding.example_form_dialog import ExampleFormDialog


class MeaningFormDialog(StyledDialog):
    @staticmethod
    def from_instance(dialog_title, vocabulary: str, meaning: Meaning):
        # instantiate an instance of meaning-form-dialog
        instance = MeaningFormDialog(dialog_title, vocabulary)
        # set the texts of translations in both chinese & english
        instance.__le_translation_chi.setText(meaning.translation_chi)
        instance.__le_translation_eng.setText(meaning.translation_eng)
        # set the part-of-speech
        instance.__comb_pos.setCurrentText(meaning.pos.format())
        # set the example sentences
        for example in meaning.example_list:
            instance.__lis_examples.push_back(data_model=example, max_height=dim.example_list_widget_max_height)
        # set the notes
        instance.__te_notes.setText(meaning.notes)
        # set the dialog-mode to modification mode
        instance.__dialog_mode = AddModifyDialogMode.M
        # set the focus-point on the line-edit of chinese translation
        instance.__le_translation_chi.setFocus()
        # return the created instance
        return instance

    def __init__(self, dialog_title, vocabulary: str):
        super(MeaningFormDialog, self).__init__(dialog_title)
        # force this dialog being the top form
        self.setWindowModality(Qt.ApplicationModal)
        # the vocabulary
        self.__vocabulary = vocabulary
        # initialize all views
        self.__init_views()
        # initialize all events
        self.__init_events()
        # resize to a proper one
        self.resize(*dim.meaning_form_dialog_size)
        # initially set the focus on the first line-edit
        self.__le_translation_chi.setFocus()
        # the result-meaning
        self.__result_meaning = None
        # the add-modify-dialog-mode
        self.__dialog_mode = AddModifyDialogMode.A

    @property
    def result_meaning(self):
        return self.__result_meaning

    # noinspection PyTypeChecker
    def __init_views(self):
        # the grid-layout for containing all sub-views
        self.__grid_base = StyledGridLayout()
        # the translation for chinese
        self.__lbl_translation_chi = StyledLabel(Strs.Chinese)
        self.__le_translation_chi = StyledLineEdit(Strs.Voc_Adding_Page_Translation_Chi_Placeholder)
        self.__grid_base.addWidget(self.__lbl_translation_chi, 0, 0, 1, 1)
        self.__grid_base.addWidget(self.__le_translation_chi, 0, 1, 1, 6)
        # the translation for english
        self.__lbl_translation_eng = StyledLabel(Strs.English)
        self.__le_translation_eng = StyledLineEdit(Strs.Voc_Adding_Page_Translation_Eng_Placeholder)
        self.__grid_base.addWidget(self.__lbl_translation_eng, 1, 0, 1, 1)
        self.__grid_base.addWidget(self.__le_translation_eng, 1, 1, 1, 6)
        # the combo-box for selecting the part-of-speech
        self.__comb_pos = StyledComboBox()
        self.__comb_pos.add_items(*list(map(lambda x: x.format(), PartOfSpeech)))
        self.__comb_pos.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored))
        self.__grid_base.addWidget(self.__comb_pos, 0, 7, 2, 1)
        # the button for adding example sentences
        self.__btn_add_new_example = StyledButton(Strs.Voc_Adding_Page_New_Example_Sentence_Button_Text)
        self.__btn_add_new_example.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored))
        self.__grid_base.addWidget(self.__btn_add_new_example, 2, 0, 1, 1)
        # the list-widget for containing all added example sentences
        self.__lis_examples = ExampleListWidget()
        self.__grid_base.addWidget(self.__lis_examples, 2, 1, 1, 7)
        # the text-edit for notes
        self.__te_notes = StyledTextEdit(Strs.Voc_Adding_Page_Notes_Placeholder)
        self.__grid_base.addWidget(self.__te_notes, 3, 0, 1, 8)
        # the buttons of cancelling & submitting
        self.__btn_cancel = StyledButton(Strs.Cancel)
        self.__btn_submit = StyledButton(Strs.Submit)
        self.__btn_submit.setEnabled(False)
        self.__grid_base.addWidget(self.__btn_cancel, 5, 0, 1, 4)
        self.__grid_base.addWidget(self.__btn_submit, 5, 4, 1, 4)
        # set the base grid-layout as the layout
        self.setLayout(self.__grid_base)

    def __init_events(self):
        self.__btn_add_new_example.clicked.connect(self.__event_add_new_example)
        self.__btn_cancel.clicked.connect(self.__event_cancel)
        self.__btn_submit.clicked.connect(self.__event_submit)
        self.__le_translation_chi.textChanged.connect(self.__event_translation_line_edits_changed)
        self.__le_translation_eng.textChanged.connect(self.__event_translation_line_edits_changed)

    # the event for adding a new example sentence
    def __event_add_new_example(self):
        # prompt up a dialog for filling the info of new example sentence
        dialog = ExampleFormDialog(Strs.Example_Form_Dialog_Title_A, self.__vocabulary).show_and_exec()
        if dialog.result_example is not None:
            self.__lis_examples.push_back(data_model=dialog.result_example, max_height=dim.example_list_widget_max_height)

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
            # instantiate a meaning as the result
            self.__result_meaning = Meaning(pos, translation_chi, translation_eng, example_sentences, notes)
            print(self.__result_meaning)
            # close the dialog
            self.close()

    # the event for disable/enable the submission button
    def __event_translation_line_edits_changed(self):
        self.__btn_submit.setEnabled(self.__le_translation_chi.text() != '' or self.__le_translation_eng.text() != '')
