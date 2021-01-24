from views.pages.base_page import BasePage
from views.styled import StyledLabel


class VocAddingPage(BasePage):
    def __init__(self, page_name):
        super(VocAddingPage, self).__init__(page_name)
        self.__lbl = StyledLabel(page_name)
        self.addWidget(self.__lbl)
