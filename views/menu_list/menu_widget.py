from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from views.pages.base_page import BasePage
from views.styled import StyledLabel


class MenuWidget(QWidget):
    def __init__(self, page: BasePage, index: int, parent=None):
        super(MenuWidget, self).__init__(parent)
        # the page corresponding to this menu-widget
        self.page = page
        # the index of this widget
        self.index = index
        # initialize all views
        self.__init_views()

    def __init_views(self):
        # the base v-box
        self.__vbox_all = QVBoxLayout()
        # the label for displaying the name of this menu-item
        self.__lbl_menu_name = StyledLabel(self.page.page_name)
        self.__vbox_all.addWidget(self.__lbl_menu_name, 0, Qt.AlignCenter)
        # set the v-box as the layout of this widget
        self.setLayout(self.__vbox_all)
