from PyQt5.QtCore import Qt

from enums.Add_Modify_Dialog_Mode import AddModifyDialogMode
from enums.dialog_result import DialogResult
from enums.pref_key import PrefKey
from enums.strs import Strs
from managers.pref_manager import PrefManager
from models.example_sentence import ExampleSentence
from utils import dimension as dim
from views.list_widgets.example_translation_list.example_translation_list_widget import ExampleTranslationListWidget
from views.message_boxes.base_message_box import BaseMessageBox
from views.styled_views.styled import StyledLineEdit, StyledGridLayout, StyledButton, StyledDialog, StyledLabel


class ExampleFormDialog(StyledDialog):
    @staticmethod
    def from_instance(dialog_title, example_sentence: ExampleSentence):
        # instantiate an instance of example-form-dialog
        instance = ExampleFormDialog(dialog_title, example_sentence.word)
        # set the text of the example sentence
        instance.__le_example.setText(example_sentence.sentence)
        # set the texts of translations
        for translation in example_sentence.translation_list:
            instance.__lis_translations.push_back(translation, max_height=dim.example_translation_list_widget_max_height)
        # set the dialog-mode to modification mode
        instance.__dialog_mode = AddModifyDialogMode.M
        # set the focus-point on the example-line-edit
        instance.__le_example.setFocus()
        # return the created instance
        return instance

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
        self.resize(*dim.example_form_dialog_size)
        # initially set the focus on the first line-edit
        self.__le_example.setFocus()
        # the result-example
        self.__result_example = None
        # the add-modify-dialog-mode
        self.__dialog_mode = AddModifyDialogMode.A

    @property
    def result_example(self):
        return self.__result_example

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
        self.__grid_base.addWidget(self.__lis_translations, 1, 0, 2, 12)
        # the buttons of cancelling & submitting
        self.__btn_cancel = StyledButton(Strs.Cancel)
        self.__btn_submit = StyledButton(Strs.Submit)
        self.__btn_submit.setEnabled(False)
        self.__grid_base.addWidget(self.__btn_cancel, 3, 0, 1, 6)
        self.__grid_base.addWidget(self.__btn_submit, 3, 6, 1, 6)
        # set the base v-box as the layout of this widget
        self.setLayout(self.__grid_base)

    def __init_events(self):
        self.__btn_add_new_translation.clicked.connect(self.__event_add_new_translation)
        self.__btn_cancel.clicked.connect(self.__event_cancel)
        self.__btn_submit.clicked.connect(self.__event_submit)
        self.__le_example.textChanged.connect(self.__event_example_line_edit_changed)

    # the event for adding a new translation
    def __event_add_new_translation(self):
        self.__lis_translations.push_back('', max_height=dim.example_translation_list_widget_max_height)

    # the event for cancelling the action of adding a new example sentence
    def __event_cancel(self):
        # if a message-box for warning the user is needed
        if self.__dialog_mode == AddModifyDialogMode.A and PrefManager.get_pref(PrefKey.MSG_BOX_CANCELLING_NEW_EXAMPLE):
            # create & show the dialog to make sure that the user really want to cancel the action for adding it
            if BaseMessageBox.Builder.\
                    init(Strs.Make_Sure_For_Cancelling_Sth_Dialog_Title, PrefKey.MSG_BOX_CANCELLING_NEW_EXAMPLE).\
                    set_content(Strs.Make_Sure_For_Cancelling_Adding_New_Example_Sentence_Dialog_Content).create().\
                    show_and_exec().\
                    dialog_result == DialogResult.YES:
                self.close()
        # otherwise, close the example-form-dialog directly
        else:
            self.close()

    # the event for submitting the new example sentence
    def __event_submit(self):
        # get the text of the example sentence
        example_text = self.__le_example.text()
        # if the line-edit of the example sentence is not empty
        if example_text != '':
            # instantiate an example-sentence as the result
            self.__result_example = ExampleSentence(self.__vocabulary, example_text, self.__lis_translations.get_all_translations())
            # close the dialog
            self.close()

    # the event for disable/enable the submission button
    def __event_example_line_edit_changed(self):
        self.__btn_submit.setEnabled(self.__le_example.text() != '')

    def setFocus(self) -> None:
        self.__le_example.setFocus()
