from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from views.pages.base_page import BasePage
from views.styled_views.styled import StyledLabel, StyledVBox


class MenuWidget(QWidget):
    def __init__(self, page: BasePage, attached):
        super(MenuWidget, self).__init__()
        # the page corresponding to this menu-widget
        self.page = page
        # the list-widget that this widget attached on
        self.__attached = attached
        # initialize all views
        self.__init_views()

    def __init_views(self):
        # the base v-box
        self.__vbox_all = StyledVBox(spacing=0)
        # the label for displaying the name of this menu-item
        self.__lbl_menu_name = StyledLabel(self.page.page_name)
        self.__vbox_all.addWidget(self.__lbl_menu_name, 0, Qt.AlignCenter)
        # set the v-box as the layout of this widget
        self.setLayout(self.__vbox_all)
