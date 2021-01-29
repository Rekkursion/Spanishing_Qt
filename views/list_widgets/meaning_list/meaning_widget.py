import copy

from PyQt5.QtWidgets import QWidget

from models.meaning import Meaning
from utils import configuration as cfg
from views.styled_views.styled import StyledLabel, StyledHBox
from views.styled_views.styled_action_button import StyledActionButton


class MeaningWidget(QWidget):
    def __init__(self, meaning: Meaning, attached):
        super(MeaningWidget, self).__init__()
        # the meaning for this widget
        self.__meaning = copy.deepcopy(meaning)
        # the list-widget that this widget attached on
        self.__attached = attached
        # initialize all views
        self.__init_views()
        # initialize all events
        self.__init_events()

    @property
    def meaning(self):
        return copy.deepcopy(self.__meaning)

    @meaning.setter
    def meaning(self, value):
        self.__meaning = copy.deepcopy(value)
        self.__lbl_pos.set_string_by_str_enum_or_literal_str(self.__get_formatted_abbr_of_pos())
        self.__lbl_translations.set_string_by_str_enum_or_literal_str(self.__get_formatted_translations())

    def __init_views(self):
        # the label for displaying the part-of-speech
        self.__lbl_pos = StyledLabel(self.__get_formatted_abbr_of_pos())
        # the label for displaying the translations in chinese & english
        self.__lbl_translations = StyledLabel(self.__get_formatted_translations())
        # the action-button for some actions about this meaning
        self.__btn_actions = StyledActionButton(cfg.more_actions_icon_path)
        # the base h-box
        self.__hbox_base = StyledHBox((self.__lbl_pos, 0), (self.__lbl_translations, 1), (self.__btn_actions, 0), spacing=-6)
        # set the h-box as the layout of this widget
        self.setLayout(self.__hbox_base)

    def __init_events(self):
        pass

    # get the formatted part-of-speech to be displayed w/ abbreviation only
    def __get_formatted_abbr_of_pos(self):
        return f'<span style="color: rgb(110, 80, 130);">[{self.__meaning.pos.get_abbr()}]</span>'

    # get the formatted translations (chinese & english) to be displayed
    def __get_formatted_translations(self):
        # if both translations are not empty
        if self.__meaning.translation_chi != '' and self.__meaning.translation_eng != '':
            return f'{self.__meaning.translation_chi} ({self.__meaning.translation_eng})'
        # if the one in english is empty
        elif self.__meaning.translation_chi != '':
            return self.__meaning.translation_chi
        # if the one in chinese is empty
        else:
            return self.__meaning.translation_eng
