from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QPushButton, QMenu

from enums.fixed_size import FixedSizes
from views.styled_views.styled import StyledAction


class StyledActionButton(QPushButton):
    def __init__(self, icon_path: str, fixed_size=FixedSizes.MEDIUM):
        super(StyledActionButton, self).__init__(QIcon(QPixmap(icon_path)), '')
        # set an empty menu
        self.setMenu(QMenu())
        # set the style-sheet
        self.setStyleSheet("""
            QPushButton {background-color: transparent;}
            QPushButton:pressed {background-color: rgb(226, 230, 234);}
            QPushButton:hover:!pressed {background-color: rgb(226, 230, 234);}
        """)
        # set the size of fonts
        self.__fixed_size = fixed_size

    # add an action on this action-button
    def add_action(self, action_name, event):
        action = StyledAction(action_name, self.__fixed_size)
        self.menu().addAction(action)
        action.triggered.connect(event)
