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
            QPushButton:menu-indicator {width: 0px;}
            QPushButton {background-color: transparent;}
            QPushButton:pressed {background-color: rgb(226, 230, 234);}
            QPushButton:hover:!pressed {background-color: rgb(226, 230, 234);}
        """)
        # set the size of fonts
        self.__fixed_size = fixed_size

    # add an action on this action-button
    def add_action(self, action_name, icon_path: str, event):
        action = StyledAction(action_name, self.__fixed_size)
        if icon_path is not None and icon_path != '':
            action.setIcon(QIcon(icon_path))
        self.menu().addAction(action)
        action.triggered.connect(event)

    # get all of the added actions
    def get_all_actions(self):
        return self.menu().actions()
