import copy

from PyQt5.QtWidgets import QWidget

from enums.strs import Strs
from models.example_sentence import ExampleSentence
from utils import configuration as cfg
from views.styled_views.styled import StyledLabel, StyledHBox
from views.styled_views.styled_action_button import StyledActionButton


class ExampleWidget(QWidget):
    def __init__(self, index: int, example_sentence: ExampleSentence, attached):
        super(ExampleWidget, self).__init__()
        # the example sentence for this widget
        self.__example_sentence = copy.deepcopy(example_sentence)
        # the index of this widget
        self.__index = index
        # the list-widget that this widget attached on
        self.__attached = attached
        # initialize all views
        self.__init_views()
        # initialize all events
        self.__init_events()

    @property
    def example_sentence(self):
        return copy.deepcopy(self.__example_sentence)

    def __init_views(self):
        # the line-edit for displaying the translation
        self.__lbl_sentence = StyledLabel(self.__example_sentence.sentence)
        # the action-button for some actions about this example sentence
        self.__btn_actions = StyledActionButton(cfg.example_action_icon_path)
        # the base h-box
        self.__hbox_base = StyledHBox(
            (self.__lbl_sentence, 1), (self.__btn_actions, 0),
            spacing=-6
        )
        # set the h-box as the layout of this widget
        self.setLayout(self.__hbox_base)

    def __init_events(self):
        # todo: add actions for each example sentence
        self.__btn_actions.add_action(Strs.Delete, lambda: print('la alcachofa'))
