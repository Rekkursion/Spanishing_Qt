from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QAction, QMainWindow, QDialog, QMenu, QHBoxLayout, \
    QVBoxLayout, QGridLayout, QTextEdit, QLayout, QWidget, QCheckBox, QComboBox

from enums.fixed_size import FixedSizes
from enums.pref_key import PrefKey
from enums.strs import Strs
from managers.lang_manager import LangManager
from managers.pref_manager import PrefManager
from utils import configuration as cfg
from utils import dimension as dim


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
        # q-label, q-push-button, q-action, q-check-box -> set its text
        if isinstance(self, (QLabel, QPushButton, QAction, QCheckBox)):
            self.setText(literal_str)
        # q-line-edit, q-text-edit -> set its placeholder
        elif isinstance(self, (QLineEdit, QTextEdit)):
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
    def __init__(self, placeholder='', text='', fixed_size=FixedSizes.MEDIUM):
        super(StyledLineEdit, self).__init__()
        # set the placeholder
        self.register_str_enum(placeholder)
        # if the text is not empty, set it on
        if text != '':
            self.setText(text)
        # set the fixed-size
        self.setFont(QFont(cfg.font_family, fixed_size))
        # set the padding-left
        self.setStyleSheet('padding-left: 2px;')


class StyledTextEdit(QTextEdit, BaseStyled):
    def __init__(self, placeholder='', fixed_size=FixedSizes.MEDIUM):
        super(StyledTextEdit, self).__init__()
        # set the placeholder
        self.register_str_enum(placeholder)
        # set the fixed-size
        self.setFont(QFont(cfg.font_family, fixed_size))
        # set the padding-left
        self.setStyleSheet('padding-left: 2px; padding-top: 2px;')


class StyledCheckBox(QCheckBox, BaseStyled):
    def __init__(self, text='', fixed_size=FixedSizes.MEDIUM):
        super(StyledCheckBox, self).__init__()
        # set the text
        self.register_str_enum(text)
        # set the fixed-size
        self.setFont(QFont(cfg.font_family, fixed_size))


class StyledComboBox(QComboBox, BaseStyled):
    def __init__(self, fixed_size=FixedSizes.MEDIUM):
        super(StyledComboBox, self).__init__()
        # set the fixed-size
        self.setFont(QFont(cfg.font_family, fixed_size))
        # for centering the displayed text
        # self.setEditable(True)
        # self.lineEdit().setReadOnly(True)
        # self.lineEdit().setAlignment(Qt.AlignCenter)

    # add a single item
    def add_item(self, text):
        self.addItem(text)
        self.register_str_enum(text)
        # for centering the texts of items in the pop-up list
        # self.setItemData(self.count() - 1, Qt.AlignCenter, Qt.TextAlignmentRole)

    # add multiple items
    def add_items(self, *texts):
        for text in texts:
            self.add_item(text)


class StyledAction(QAction, BaseStyled):
    def __init__(self, text='', fixed_size=FixedSizes.MEDIUM):
        super(StyledAction, self).__init__()
        # set the text
        self.register_str_enum(text)
        # set the fixed-size
        self.setFont(QFont(cfg.font_family, fixed_size))


class StyledMainWindow(QMainWindow, BaseStyled):
    def __init__(self, win_title, fixed_size=FixedSizes.MEDIUM):
        super(StyledMainWindow, self).__init__()
        # set the window-title
        self.register_str_enum(win_title)
        # set the fixed-size
        self.setFont(QFont(cfg.font_family, fixed_size))


class StyledDialog(QDialog, BaseStyled):
    def __init__(self, dialog_title, fixed_size=FixedSizes.MEDIUM):
        super(StyledDialog, self).__init__()
        # set the window-title
        self.register_str_enum(dialog_title)
        # set the fixed-size
        self.setFont(QFont(cfg.font_family, fixed_size))

    # show & execute the dialog, then return itself
    def show_and_exec(self):
        self.show()
        self.exec()
        return self


class StyledHBox(QHBoxLayout):
    def __init__(self, *sub_views, spacing=dim.general_spacing):
        super(StyledHBox, self).__init__()
        self.setSpacing(spacing)
        for (sub_view, stretch) in sub_views:
            if isinstance(sub_view, QLayout):
                self.addLayout(sub_view, stretch=stretch)
            elif isinstance(sub_view, QWidget):
                self.addWidget(sub_view, stretch=stretch)


class StyledVBox(QVBoxLayout):
    def __init__(self, *sub_views, spacing=dim.general_spacing):
        super(StyledVBox, self).__init__()
        self.setSpacing(spacing)
        for (sub_view, stretch) in sub_views:
            if isinstance(sub_view, QLayout):
                self.addLayout(sub_view, stretch=stretch)
            elif isinstance(sub_view, QWidget):
                self.addWidget(sub_view, stretch=stretch)


class StyledGridLayout(QGridLayout):
    def __init__(self, spacing=dim.general_spacing):
        super(StyledGridLayout, self).__init__()
        self.setSpacing(spacing)
