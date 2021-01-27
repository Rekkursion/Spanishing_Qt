from PyQt5.QtCore import Qt

from enums.strs import Strs
from utils import dimension as dim
from views.styled import StyledHBox, StyledLabel, StyledLineEdit, StyledVBox, StyledGridLayout, StyledButton, \
    StyledTextEdit, StyledDialog
from views.voc_adding.example_form.example_form_dialog import ExampleFormDialog


class MeaningFormDialog(StyledDialog):
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

    def __init_views(self):
        # the v-box for all sub-views
        self.__vbox_base = StyledVBox()
        # the grid-layout for containing translations & part-of-speech-selecting button
        self.__grid_translations_and_pos = StyledGridLayout()
        # the translation for chinese
        self.__lbl_translation_chi = StyledLabel(Strs.Chinese)
        self.__le_translation_chi = StyledLineEdit(Strs.Voc_Adding_Page_Translation_Chi_Placeholder)
        self.__hbox_translation_chi = StyledHBox((self.__lbl_translation_chi, 0), (self.__le_translation_chi, 1))
        # the translation for english
        self.__lbl_translation_eng = StyledLabel(Strs.English)
        self.__le_translation_eng = StyledLineEdit(Strs.Voc_Adding_Page_Translation_Eng_Placeholder)
        self.__hbox_translation_eng = StyledHBox((self.__lbl_translation_eng, 0), (self.__le_translation_eng, 1))
        # the button for selecting the part-of-speech
        self.__btn_pos = StyledButton(Strs.Voc_Adding_Page_Select_Pos_Button_Text)
        # add translations & pos-button into the grid-layout
        self.__grid_translations_and_pos.addLayout(self.__hbox_translation_chi, 0, 0, 1, 6)
        self.__grid_translations_and_pos.addLayout(self.__hbox_translation_eng, 1, 0, 1, 6)
        self.__grid_translations_and_pos.addWidget(self.__btn_pos, 0, 6, 2, 1)
        self.__vbox_base.addLayout(self.__grid_translations_and_pos)
        # the button for adding example sentences
        self.__btn_add_new_example = StyledButton(Strs.Voc_Adding_Page_New_Example_Sentence_Button_Text)
        self.__vbox_base.addWidget(self.__btn_add_new_example)
        # the h-box for containing all added example sentences
        self.__hbox_examples = StyledHBox()
        self.__vbox_base.addLayout(self.__hbox_examples)
        # the text-edit for notes
        self.__te_notes = StyledTextEdit(Strs.Voc_Adding_Page_Notes_Placeholder)
        self.__vbox_base.addWidget(self.__te_notes)
        # the buttons of cancelling & submitting
        self.__btn_cancel = StyledButton(Strs.Cancel)
        self.__btn_submit = StyledButton(Strs.Submit)
        self.__hbox_button_bar = StyledHBox((self.__btn_cancel, 1), (self.__btn_submit, 1))
        self.__vbox_base.addLayout(self.__hbox_button_bar)
        # set the base v-box as the layout of this widget
        self.setLayout(self.__vbox_base)
        # set the height of the pos-button
        self.__btn_pos.setMinimumHeight(
            self.__hbox_translation_chi.sizeHint().height() +
            self.__hbox_translation_eng.sizeHint().height() +
            self.__hbox_translation_chi.spacing()
        )

    def __init_events(self):
        self.__btn_add_new_example.clicked.connect(self.__event_add_new_example)

    # the event for adding a new example sentence
    def __event_add_new_example(self):
        # prompt up a dialog for filling the info of new example sentence
        dialog = ExampleFormDialog(Strs.Example_Form_Dialog_Title, self.__vocabulary).show_and_exec()
        if dialog.result_example is not None:
            
            print(dialog.result_example)
