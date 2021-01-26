from PyQt5.QtCore import Qt

from enums.strs import Strs
from utils import configuration as cfg
from views.styled import StyledLineEdit, StyledGridLayout, StyledButton, StyledDialog, StyledLabel
from views.voc_adding.example_form.example_translation_list_widget import ExampleTranslationListWidget


class ExampleFormDialog(StyledDialog):
    def __init__(self, dialog_title, vocabulary: str):
        super(ExampleFormDialog, self).__init__(dialog_title)
        # force this dialog being the top form
        self.setWindowModality(Qt.ApplicationModal)
        # the vocabulary of examples
        self.__vocabulary = vocabulary
        # initialize all views
        self.__init_views()
        # initialize all events
        self.__init_events()
        # resize to a proper one
        self.resize(*cfg.example_form_dialog_size)
        # initially set the focus on the first line-edit
        self.__le_example.setFocus()

    def __init_views(self):
        # the grid-layout for containing all sub-views
        self.__grid_base = StyledGridLayout()
        # the label for displaying the vocabulary
        self.__lbl_vocabulary = StyledLabel(self.__vocabulary)
        self.__grid_base.addWidget(self.__lbl_vocabulary, 0, 0, 1, 1)
        # the line-edit for typing the example sentence
        self.__le_example = StyledLineEdit(Strs.Voc_Adding_Page_Example_Sentence_Placeholder)
        self.__grid_base.addWidget(self.__le_example, 0, 1, 1, 10)
        # the button for adding new translations for this example sentence
        self.__btn_add_new_translation = StyledButton(Strs.Voc_Adding_Page_Example_Sentence_New_Translation_Button_Text)
        self.__grid_base.addWidget(self.__btn_add_new_translation, 0, 11, 1, 1)
        # the list for displaying added translations
        self.__lis_translations = ExampleTranslationListWidget()
        self.__grid_base.addWidget(self.__lis_translations, 1, 0, 6, 12)
        # the buttons of cancelling & submitting
        self.__btn_cancel = StyledButton(Strs.Cancel)
        self.__btn_submit = StyledButton(Strs.Submit)
        self.__grid_base.addWidget(self.__btn_cancel, 7, 0, 1, 6)
        self.__grid_base.addWidget(self.__btn_submit, 7, 6, 1, 6)
        # set the base v-box as the layout of this widget
        self.setLayout(self.__grid_base)

    def __init_events(self):
        self.__btn_add_new_translation.clicked.connect(self.__event_add_new_translation)

    def __event_add_new_translation(self):
        self.__lis_translations.push_back()
