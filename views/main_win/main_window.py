from PyQt5.QtWidgets import QHBoxLayout, QFrame, QStackedLayout

from enums.strs import Strs
from utils import configuration as cfg
from views.menu_list.menu_list_widget import MenuListWidget
from views.pages.preferences_page import PreferencesPage
from views.pages.voc_adding_page import VocAddingPage
from views.styled import StyledMainWindow


class MainWindow(StyledMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(Strs.Main_Window_Title)
        # initialize all views
        self.__init_views()
        # resize to a proper one
        self.resize(*cfg.main_window_size)

    def __init_views(self):
        # the base h-box
        self.__hbox_all = QHBoxLayout()
        # the menu list
        # self.__lis_menu = MenuListWidget(
        #     Strs.Menu_List_Item_Voc_List,
        #     Strs.Menu_List_Item_Add_Voc,
        #     Strs.Menu_List_Item_Verb_Conjugations,
        #     Strs.Menu_List_Item_Practices,
        #     Strs.Menu_List_Item_Preferences
        # )
        self.__lis_menu = MenuListWidget(
            VocAddingPage(Strs.Menu_List_Item_Add_Voc),
            PreferencesPage(Strs.Menu_List_Item_Preferences)
        )
        self.__hbox_all.addWidget(self.__lis_menu, 0)
        # the stacked-layout for containing various pages
        self.__page_layout = QStackedLayout()
        for menu_widget in self.__lis_menu.get_all_widgets():
            self.__page_layout.addWidget(menu_widget.page.wrap_as_frame())
        self.__hbox_all.addLayout(self.__page_layout)
        # set the h-box as the layout of this window
        self.__frame_all = QFrame()
        self.__frame_all.setLayout(self.__hbox_all)
        self.setCentralWidget(self.__frame_all)

    # set the page
    def set_page_by_index(self, index: int):
        self.__page_layout.setCurrentIndex(index)
