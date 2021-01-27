from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

from enums.strs import Strs
from utils import dimension as dim
from views.styled_views.styled import StyledLabel, StyledLineEdit, StyledGridLayout, \
    StyledButton, \
    StyledTextEdit, StyledDialog
from views.voc_adding.example_form.example_form_dialog import ExampleFormDialog
from views.voc_adding.meaning_form.example_list_widget import ExampleListWidget


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
        # the button for selecting the part-of-speech
        self.__btn_pos = StyledButton(Strs.Voc_Adding_Page_Select_Pos_Button_Text)
        self.__btn_pos.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored))
        self.__grid_base.addWidget(self.__btn_pos, 0, 7, 2, 1)
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
        self.__grid_base.addWidget(self.__btn_cancel, 5, 0, 1, 4)
        self.__grid_base.addWidget(self.__btn_submit, 5, 4, 1, 4)
        # set the base grid-layout as the layout
        self.setLayout(self.__grid_base)

    def __init_events(self):
        self.__btn_add_new_example.clicked.connect(self.__event_add_new_example)

    # the event for adding a new example sentence
    def __event_add_new_example(self):
        # prompt up a dialog for filling the info of new example sentence
        dialog = ExampleFormDialog(Strs.Example_Form_Dialog_Title_A, self.__vocabulary).show_and_exec()
        if dialog.result_example is not None:
            self.__lis_examples.push_back(dialog.result_example)
