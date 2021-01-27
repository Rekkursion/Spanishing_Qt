from PyQt5.QtCore import Qt

from enums.dialog_result import DialogResult
from enums.fixed_size import FixedSizes
from enums.pref_key import PrefKey
from enums.strs import Strs
from managers.pref_manager import PrefManager
from utils import dimension as dim
from views.styled_views.styled import StyledGridLayout, StyledLabel, StyledDialog, StyledButton, StyledCheckBox


class BaseMessageBox(StyledDialog):
    # the builder-class for the base-message-box
    class Builder:
        # the instance of a base-message-box
        __instance = None

        # initialize the instance
        @staticmethod
        def init(dialog_title, size=dim.base_message_box_size):
            BaseMessageBox.Builder.__instance = BaseMessageBox(dialog_title, size)
            return BaseMessageBox.Builder

        # set the content of the instance
        @staticmethod
        def set_content(content):
            BaseMessageBox.Builder.__instance.set_content(content)
            return BaseMessageBox.Builder

        # return the instance
        @staticmethod
        def create():
            return BaseMessageBox.Builder.__instance

    # ================================================================================ #

    def __init__(self, dialog_title, size):
        super(BaseMessageBox, self).__init__(dialog_title)
        # force this dialog being the top form
        self.setWindowModality(Qt.ApplicationModal)
        # initialize base views
        self.__init_views()
        # initialize base events
        self.__init_events()
        # resize to a proper one
        self.resize(*size)
        # the result of this dialog
        self.__dialog_result = DialogResult.NO

    @property
    def dialog_result(self):
        return self.__dialog_result

    def __init_views(self):
        # the grid-layout for containing all sub-views
        self.__grid_base = StyledGridLayout()
        # the label for the content
        self.__lbl_content = StyledLabel('')
        self.__lbl_content.setWordWrap(True)
        self.__grid_base.addWidget(self.__lbl_content, 0, 0, 8, 12, Qt.AlignTop)
        # the check-box for letting the user to choose that this message-box will not appear next time
        self.__chk_not_appears_next_time = StyledCheckBox(Strs.Not_Appears_Next_Time, FixedSizes.SMALL)
        self.__grid_base.addWidget(self.__chk_not_appears_next_time, 8, 0, 1, 12, Qt.AlignBottom)
        # the buttons of answering yes/no
        self.__btn_no = StyledButton(Strs.No)
        self.__btn_yes = StyledButton(Strs.Yes)
        self.__grid_base.addWidget(self.__btn_no, 9, 4, 1, 4)
        self.__grid_base.addWidget(self.__btn_yes, 9, 8, 1, 4)
        # set the base grid-layout
        self.setLayout(self.__grid_base)

    def __init_events(self):
        self.__btn_no.clicked.connect(self.__event_rejected)
        self.__btn_yes.clicked.connect(self.__event_accepted)

    # set the content of this message-box
    def set_content(self, content):
        self.__lbl_content.set_string_by_str_enum_or_literal_str(content)

    # the event for rejecting
    def __event_rejected(self):
        self.__dialog_result = DialogResult.NO
        self.close()

    # the event for accepting
    def __event_accepted(self):
        self.__dialog_result = DialogResult.YES
        self.close()

    def close(self) -> bool:
        # if the not-appears-next-time check-box is checked
        PrefManager.set_pref(PrefKey.MSG_BOX_CANCELLING_NEW_EXAMPLE, not self.__chk_not_appears_next_time.isChecked())
        # close this message-box
        return super(BaseMessageBox, self).close()
