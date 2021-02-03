from enums.fixed_size import FixedSizes
from enums.word_variability import WordVariability
from views.styled_views.styled import StyledRadioButton


class StyledWordVariabilityRadioButton(StyledRadioButton):
    def __init__(self, word_variability: WordVariability, text, fixed_size=FixedSizes.MEDIUM):
        super(StyledWordVariabilityRadioButton, self).__init__(text, fixed_size)
        self.__word_variability = word_variability

    @property
    def word_variability(self):
        return self.__word_variability

    @word_variability.setter
    def word_variability(self, value):
        self.__word_variability = value
