from enums.strs import Strs
from views.pages.base_page import BasePage
from views.styled import StyledHBox, StyledLabel, StyledLineEdit


class VocAddingPage(BasePage):
    def __init__(self, page_name):
        super(VocAddingPage, self).__init__(page_name)
        # initialize all views
        self._init_views()
        # initialize all events
        self._init_events()

    def _init_views(self):
        # the h-box for the word
        self.__hbox_word = StyledHBox()
        self.__lbl_word = StyledLabel(Strs.Voc_Adding_Page_Word)
        self.__le_word = StyledLineEdit(Strs.Voc_Adding_Page_Word_Placeholder)
        self.__hbox_word.addWidget(self.__lbl_word, 0)
        self.__hbox_word.addWidget(self.__le_word, 1)
        self._add_layout(self.__hbox_word)

    def _init_events(self):
        return NotImplemented
