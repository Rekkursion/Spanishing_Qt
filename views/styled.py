from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QAction, QMainWindow, QDialog, QMenu

from enums.fixed_size import FixedSizes
from enums.pref_key import PrefKey
from enums.strs import Strs
from managers.lang_manager import LangManager
from managers.pref_manager import PrefManager
from utils import configuration as cfg


# the base class of all styled views
class BaseStyled:
    def __init__(self):
        super(BaseStyled, self).__init__()

    def register_str_enum(self, str_enum_or_literal_str):
        LangManager.register(self, str_enum_or_literal_str)

    # set the string on this view according to its type
    def set_string_by_str_enum_or_literal_str(self, str_enum_or_literal_str):
        # get the literal string
        if isinstance(str_enum_or_literal_str, Strs):
            literal_str = str_enum_or_literal_str.value[PrefManager.get_pref(PrefKey.LANG)]
        else:
            literal_str = str_enum_or_literal_str
        # q-label, q-push-button, q-action -> set its text
        if isinstance(self, (QLabel, QPushButton, QAction)):
            self.setText(literal_str)
        # q-line-edit -> set its placeholder
        elif isinstance(self, QLineEdit):
            self.setPlaceholderText(literal_str)
        # q-main-window, q-dialog -> set its window-title
        elif isinstance(self, (QMainWindow, QDialog)):
            self.setWindowTitle(literal_str)
        # q-menu -> set its title
        elif isinstance(self, QMenu):
            self.setTitle(literal_str)


class StyledLabel(QLabel, BaseStyled):
    def __init__(self, text, fixed_size=FixedSizes.MEDIUM):
        super(StyledLabel, self).__init__()
        # set the text
        self.register_str_enum(text)
        # set the fixed-size
        self.setFont(QFont(cfg.font_family, fixed_size))


class StyledButton(QPushButton, BaseStyled):
    def __init__(self, text, fixed_size=FixedSizes.MEDIUM):
        super(StyledButton, self).__init__()
        # set the text
        self.register_str_enum(text)
        # set the fixed-size
        self.setFont(QFont(cfg.font_family, fixed_size))


class StyledLineEdit(QLineEdit, BaseStyled):
    def __init__(self, placeholder='', fixed_size=FixedSizes.MEDIUM):
        super(StyledLineEdit, self).__init__()
        # set the placeholder
        self.register_str_enum(placeholder)
        # set the fixed-size
        self.setFont(QFont(cfg.font_family, fixed_size))


class StyledMainWindow(QMainWindow, BaseStyled):
    def __init__(self, win_title, fixed_size=FixedSizes.MEDIUM):
        super(StyledMainWindow, self).__init__()
        # set the window-title
        self.register_str_enum(win_title)
        # set the fixed-size
        self.setFont(QFont(cfg.font_family, fixed_size))
