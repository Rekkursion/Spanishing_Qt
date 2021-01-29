from PyQt5.QtWidgets import QWidget

from enums.strs import Strs
from utils import dimension
from views.list_widgets.meaning_list.meaning_list_widget import MeaningListWidget
from views.styled_views.styled import StyledLabel, StyledLineEdit, StyledButton, \
    StyledGridLayout
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
        self.__grid_base.addWidget(self.__btn_new_meaning, 1, 0, 1, 10)
        # the list-widget for containing all added meanings
        self.__lis_meanings = MeaningListWidget()
        self.__lis_meanings.setMinimumHeight(dimension.main_window_size[1] // 2)
        self.__grid_base.addWidget(self.__lis_meanings, 2, 0, 1, 10)
        # set the base grid-layout as the layout
        self.setLayout(self.__grid_base)

    def __init_events(self):
        self.__btn_new_meaning.clicked.connect(self.__event_add_new_meaning)

    # the event for adding a new meaning
    def __event_add_new_meaning(self):
        # prompt up a dialog for filling the data of the new meaning
        dialog = MeaningFormDialog(Strs.Meaning_Form_Dialog_Title, self.__le_word.text()).show_and_exec()
        if dialog.result_meaning is not None:
            self.__lis_meanings.push_back(dialog.result_meaning, adjust_height=False)

    def setFocus(self) -> None:
        self.__le_word.setFocus()
