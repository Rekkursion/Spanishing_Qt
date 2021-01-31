import copy

from PyQt5.QtWidgets import QWidget

from enums.dialog_result import DialogResult
from enums.pref_key import PrefKey
from enums.strs import Strs
from managers.lang_manager import LangManager
from managers.pref_manager import PrefManager
from models.example_sentence import ExampleSentence
from utils import configuration as cfg
from views.message_boxes.base_message_box import BaseMessageBox
from views.styled_views.styled import StyledLabel, StyledHBox
from views.styled_views.styled_action_button import StyledActionButton
from views.voc_adding.example_form_dialog import ExampleFormDialog


class ExampleWidget(QWidget):
    def __init__(self, example_sentence: ExampleSentence, attached):
        super(ExampleWidget, self).__init__()
        # the example sentence for this widget
        self.__example_sentence = copy.deepcopy(example_sentence)
        # the list-widget that this widget attached on
        self.__attached = attached
        # initialize all views
        self.__init_views()
        # initialize all events
        self.__init_events()

    @property
    def example_sentence(self):
        return copy.deepcopy(self.__example_sentence)

    @example_sentence.setter
    def example_sentence(self, value):
        self.__example_sentence = copy.deepcopy(value)
        self.__lbl_sentence.set_string_by_str_enum_or_literal_str(self.__example_sentence.sentence)

    def __init_views(self):
        # the line-edit for displaying the translation
        self.__lbl_sentence = StyledLabel(self.__example_sentence.sentence)
        # the action-button for some actions about this example sentence
        self.__btn_actions = StyledActionButton(cfg.more_actions_icon_path)
        # the base h-box
        self.__hbox_base = StyledHBox((self.__lbl_sentence, 1), (self.__btn_actions, 0), spacing=-6)
        # set the h-box as the layout of this widget
        self.setLayout(self.__hbox_base)

    def __init_events(self):
        self.__btn_actions.add_action(Strs.Modify, cfg.modification_icon_path, self.__event_modify_example)
        self.__btn_actions.add_action(Strs.Move_Up, cfg.moving_up_icon_path, self.__event_move_example_up)
        self.__btn_actions.add_action(Strs.Move_Down, cfg.moving_down_icon_path, self.__event_move_example_down)
        self.__btn_actions.add_action(Strs.Remove, cfg.removal_icon_path, self.__event_remove_example)

    # the event for modifying this example
    def __event_modify_example(self):
        # prompt up a dialog for modifying this example sentence
        dialog = ExampleFormDialog.from_instance(Strs.Example_Form_Dialog_Title_M, self.__example_sentence).show_and_exec()
        if dialog.result_example is not None:
            self.example_sentence = dialog.result_example

    # the event for moving this example up
    def __event_move_example_up(self):
        self.__attached.move_certain_example(self, True)

    # the event for moving this example down
    def __event_move_example_down(self):
        self.__attached.move_certain_example(self, False)

    # the event for removing this example
    def __event_remove_example(self):
        # the nested function for removing the example actually
        def ____remove_example():
            # unregister the registered views
            LangManager.unregister(*self.__btn_actions.get_all_actions())
            # remove the item in the list
            self.__attached.takeItem(self.__attached.indexAt(self.pos()).row())

        # if a message-box for warning the user is needed
        if PrefManager.get_pref(PrefKey.MSG_BOX_DELETING_ADDED_EXAMPLE):
            if BaseMessageBox.Builder. \
                    init(Strs.Make_Sure_For_Cancelling_Sth_Dialog_Title, PrefKey.MSG_BOX_DELETING_ADDED_EXAMPLE). \
                    set_content(Strs.Make_Sure_For_Removing_Added_Example_Sentence_Dialog_Content).create(). \
                    show_and_exec(). \
                    dialog_result == DialogResult.YES:
                ____remove_example()
        # otherwise, remove the example directly
        else:
            ____remove_example()
