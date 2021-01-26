from PyQt5.QtWidgets import QWidget

from enums.strs import Strs
from views.styled import StyledHBox, StyledLabel, StyledLineEdit, StyledVBox, StyledButton
from views.voc_adding.meaning_form_dialog import MeaningFormDialog


class SingleVocForm(QWidget):
    def __init__(self):
        super(SingleVocForm, self).__init__()
        # initialize all views
        self.__init_views()
        # initialize all events
        self.__init_events()

    def __init_views(self):
        # the v-box for all sub-views
        self.__vbox_base = StyledVBox()
        # the h-box for the word
        self.__lbl_word = StyledLabel(Strs.Voc_Adding_Page_Word)
        self.__le_word = StyledLineEdit(Strs.Voc_Adding_Page_Word_Placeholder)
        self.__vbox_base.addLayout(StyledHBox((self.__lbl_word, 0), (self.__le_word, 1)))
        # the button for adding a new meaning for this vocabulary
        self.__btn_new_meaning = StyledButton(Strs.Voc_Adding_Page_New_Meaning_Button_Text)
        self.__vbox_base.addWidget(self.__btn_new_meaning)
        # the v-box for displaying the sub-form for meanings
        # self.__vbox_meanings = StyledVBox()
        # self.__meaning_form = MeaningFormDialog()
        # self.__vbox_meanings.addWidget(self.__meaning_form)
        # self.__vbox_base.addLayout(self.__vbox_meanings)
        # set the base v-box as the layout of this widget
        self.setLayout(self.__vbox_base)

    def __init_events(self):
        self.__btn_new_meaning.clicked.connect(self.__event_add_new_meaning)

    def __event_add_new_meaning(self):
        dialog = MeaningFormDialog(Strs.Meaning_Form_Dialog_Title, self.__le_word.text())
        dialog.show()
        dialog.exec()

    def setFocus(self) -> None:
        self.__le_word.setFocus()
