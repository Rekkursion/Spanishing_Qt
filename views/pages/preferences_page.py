from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QHBoxLayout, QComboBox, QFrame

from enums.pref_key import PrefKey
from enums.strs import Strs
from managers.lang_manager import LangManager
from managers.pref_manager import PrefManager
from utils import configuration as cfg
from views.pages.base_page import BasePage
from views.styled import StyledLabel


class PreferencesPage(BasePage):
    def __init__(self, page_name):
        super(PreferencesPage, self).__init__(page_name)
        # initialize all views
        self._init_views()
        # initialize all events
        self._init_events()

    def _init_views(self):
        # the setting of interface languages
        self.__hbox_lang = QHBoxLayout()
        self.__hbox_lang.setSpacing(cfg.general_spacing)
        self.__lbl_lang = StyledLabel(Strs.Preferences_Page_Lang)
        self.__comb_lang = QComboBox()
        self.__comb_lang.addItems(LangManager.supported_languages)
        self.__comb_lang.setCurrentIndex(PrefManager.get_pref(PrefKey.LANG))
        self.__hbox_lang.addWidget(self.__lbl_lang, 0)
        self.__hbox_lang.addWidget(self.__comb_lang, 1)
        f = QFrame(); f.setLayout(self.__hbox_lang); self.addWidget(f)

    # noinspection PyUnresolvedReferences
    def _init_events(self):
        self.__comb_lang.currentIndexChanged.connect(self.__event_lang_selected)

    def setGeometry(self, a0: QRect) -> None:
        parent_size = self.parentWidget().size()
        w, h = parent_size.width(), self.sizeHint().height()
        y = 0
        for item in self._item_list:
            item.setGeometry(QRect(0, y, w, h))
            y += h

    # noinspection PyMethodMayBeStatic
    def __event_lang_selected(self, i):
        PrefManager.set_pref(PrefKey.LANG, i)
        LangManager.notify_all_registered()
