from PyQt5.QtWidgets import QComboBox

from enums.pref_key import PrefKey
from enums.strs import Strs
from managers.lang_manager import LangManager
from managers.pref_manager import PrefManager
from utils import configuration as cfg
from views.pages.base_page import BasePage
from views.styled import StyledLabel, StyledHBox


class PreferencesPage(BasePage):
    def __init__(self, page_name):
        super(PreferencesPage, self).__init__(page_name)
        # initialize all views
        self._init_views()
        # initialize all events
        self._init_events()

    def _init_views(self):
        # the setting of interface languages
        self.__hbox_lang = StyledHBox()
        self.__hbox_lang.setSpacing(cfg.general_spacing)
        self.__lbl_lang = StyledLabel(Strs.Preferences_Page_Lang)
        self.__comb_lang = QComboBox()
        self.__comb_lang.addItems(LangManager.supported_languages)
        self.__comb_lang.setCurrentIndex(PrefManager.get_pref(PrefKey.LANG))
        self.__hbox_lang.addWidget(self.__lbl_lang, 0)
        self.__hbox_lang.addWidget(self.__comb_lang, 1)
        self._add_layout(self.__hbox_lang)

    # noinspection PyUnresolvedReferences
    def _init_events(self):
        self.__comb_lang.currentIndexChanged.connect(self.__event_lang_selected)

    # noinspection PyMethodMayBeStatic
    def __event_lang_selected(self, i):
        PrefManager.set_pref(PrefKey.LANG, i)
        LangManager.notify_all_registered()
