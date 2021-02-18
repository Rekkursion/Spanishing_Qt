import re

from PyQt5.QtWidgets import QWidget

from enums.strs import Strs
from utils import dimension
from views.list_widgets.meaning_list.meaning_list_widget import MeaningListWidget
from views.styled_views.styled import StyledLabel, StyledLineEdit, StyledButton, \
    StyledGridLayout
from views.voc_adding.conjugation_form_dialog import ConjugationFormDialog
from views.voc_adding.meaning_form_dialog import MeaningFormDialog


class SingleVocForm(QWidget):
    def __init__(self):
        super(SingleVocForm, self).__init__()
        # initialize all views
        self.__init_views()
        # initialize all events
        self.__init_events()

    def __init_views(self):
        # the grid-layout for containing all sub-views
        self.__grid_base = StyledGridLayout()
        # the label of word
        self.__lbl_word = StyledLabel(Strs.Voc_Adding_Page_Word)
        self.__grid_base.addWidget(self.__lbl_word, 0, 0, 1, 1)
        # the line-edit for entering the word
        self.__le_word = StyledLineEdit(Strs.Voc_Adding_Page_Word_Placeholder)
        self.__grid_base.addWidget(self.__le_word, 0, 1, 1, 9)
        # the button for adding a new meaning for this vocabulary
        self.__btn_new_meaning = StyledButton(Strs.Voc_Adding_Page_New_Meaning_Button_Text)
        self.__grid_base.addWidget(self.__btn_new_meaning, 1, 0, 1, 5)
        # the button for editing the conjugation of this vocabulary if it has at least one verb-meaning
        self.__btn_edit_conjugation = StyledButton(Strs.Voc_Adding_Page_Edit_Conjugation_Button_Text)
        self.__btn_edit_conjugation.setEnabled(False)
        self.__grid_base.addWidget(self.__btn_edit_conjugation, 1, 5, 1, 5)
        # the list-widget for containing all added meanings
        self.__lis_meanings = MeaningListWidget()
        self.__lis_meanings.setMinimumHeight(dimension.main_window_size[1] // 2)
        self.__grid_base.addWidget(self.__lis_meanings, 2, 0, 1, 10)
        # set the base grid-layout as the layout
        self.setLayout(self.__grid_base)

    def __init_events(self):
        self.__btn_new_meaning.clicked.connect(self.__event_add_new_meaning)
        self.__btn_edit_conjugation.clicked.connect(self.__event_edit_conjugation)

    # the event for adding a new meaning
    def __event_add_new_meaning(self):
        # prompt up a dialog for filling the data of the new meaning
        dialog = MeaningFormDialog(Strs.Meaning_Form_Dialog_Title_A, self.get_vocabulary).show_and_exec()
        if dialog.result is not None:
            self.__lis_meanings.push_back(self.get_vocabulary, data_model=dialog.result, adjust_height=False)
            # if the result-meaning is a verb, show up the verb conjugation form
            if dialog.result.pos.is_verb():
                self.__btn_edit_conjugation.setEnabled(True)

    # the event for editing the verb conjugation if there's at least one verb-meaning of this vocabulary
    def __event_edit_conjugation(self):
        # prompt up a dialog for editing the conjugation
        dialog = ConjugationFormDialog(Strs.Conjugation_Form_Dialog_Title, self.get_vocabulary).show_and_exec()
        if dialog.result is not None:
            # todo: the returning of conjugation-editing
            pass

    # get the text of the current vocabulary
    def get_vocabulary(self):
        return re.sub(r'\s+', ' ', self.__le_word.text().strip())

    def setFocus(self) -> None:
        self.__le_word.setFocus()
