import copy

from PyQt5.QtWidgets import QWidget

from enums.dialog_result import DialogResult
from enums.pref_key import PrefKey
from enums.strs import Strs
from managers.lang_manager import LangManager
from managers.pref_manager import PrefManager
from models.meaning import Meaning
from utils import configuration as cfg
from views.message_boxes.base_message_box import BaseMessageBox
from views.styled_views.styled import StyledLabel, StyledHBox
from views.styled_views.styled_action_button import StyledActionButton
from views.voc_adding.meaning_form_dialog import MeaningFormDialog


class MeaningWidget(QWidget):
    def __init__(self, meaning: Meaning, vocabulary_getter, attached):
        super(MeaningWidget, self).__init__()
        # the vocabulary-getter for this meaning
        self.__vocabulary_getter = vocabulary_getter
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
        self.__btn_actions.add_action(Strs.Modify, cfg.modification_icon_path, self.__event_modify_meaning)
        self.__btn_actions.add_action(Strs.Move_Up, cfg.moving_up_icon_path, self.__event_move_meaning_up)
        self.__btn_actions.add_action(Strs.Move_Down, cfg.moving_down_icon_path, self.__event_move_meaning_down)
        self.__btn_actions.add_action(Strs.Remove, cfg.removal_icon_path, self.__event_remove_meaning)

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

    # the event for modifying this meaning
    def __event_modify_meaning(self):
        # prompt up a dialog for modifying this meaning sentence
        dialog = MeaningFormDialog(Strs.Meaning_Form_Dialog_Title_M, self.__vocabulary_getter, meaning=self.__meaning).show_and_exec()
        if dialog.result is not None:
            self.meaning = dialog.result

    # the event for moving this meaning up
    def __event_move_meaning_up(self):
        self.__attached.move_certain_meaning(self, True)

    # the event for moving this meaning down
    def __event_move_meaning_down(self):
        self.__attached.move_certain_meaning(self, False)

    # the event for removing this meaning
    def __event_remove_meaning(self):
        # the nested function for removing the meaning actually
        def ____remove_meaning():
            # unregister the registered views
            LangManager.unregister(*self.__btn_actions.get_all_actions())
            # remove the item in the list
            self.__attached.takeItem(self.__attached.indexAt(self.pos()).row())

        # if a message-box for warning the user is needed
        if PrefManager.get_pref(PrefKey.MSG_BOX_DELETING_ADDED_MEANING):
            if BaseMessageBox.Builder. \
                    init(Strs.Make_Sure_For_Cancelling_Sth_Dialog_Title, PrefKey.MSG_BOX_DELETING_ADDED_MEANING). \
                    set_content(Strs.Make_Sure_For_Removing_Added_Example_Sentence_Dialog_Content).create(). \
                    show_and_exec(). \
                    dialog_result == DialogResult.YES:
                ____remove_meaning()
        # otherwise, remove the example directly
        else:
            ____remove_meaning()
