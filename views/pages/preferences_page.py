from views.pages.base_page import BasePage
from views.styled import StyledButton


class PreferencesPage(BasePage):
    def __init__(self, page_name):
        super(PreferencesPage, self).__init__(page_name)
        self.__btn = StyledButton(page_name)
        self.addWidget(self.__btn)
