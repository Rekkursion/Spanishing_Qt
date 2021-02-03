from dataclasses import dataclass, field
from typing import List

from enums.part_of_speech import PartOfSpeech
from enums.word_variability import WordVariability
from models.example_sentence import ExampleSentence


# the type of meanings that the form of a word is variable, i.e., nouns & adjectives
@dataclass
class WordForms:
    # the variability of gender
    gender_variability: WordVariability = field(default=WordVariability.GENERAL, compare=False)
    # the variability of number
    number_variability: WordVariability = field(default=WordVariability.GENERAL, compare=False)
    # all of the forms, i.e., (<m.s>, <f.s>, <m.pl>, <f.pl>)
    __forms: List[str] = field(default_factory=lambda: [None, None, None, None], compare=False)

    # get a certain kind of forms of this meaning
    def get_form(self, is_masculine: bool, is_singular: bool):
        # get the form of masculines
        if is_masculine:
            return self.__forms[0 if is_singular else 2]
        # get the form of feminines
        else:
            return self.__forms[1 if is_singular else 3]

    # set a certain kind of forms of this meaning
    def set_form(self, form: str, is_masculine: bool, is_singular: bool):
        # set the form of masculines
        if is_masculine:
            self.__forms[0 if is_singular else 2] = form
        # set the form of feminines
        else:
            self.__forms[1 if is_singular else 3] = form


@dataclass
class Meaning:
    # the part-of-speech
    pos: PartOfSpeech
    # the translation in chinese
    translation_chi: str = field(default='')
    # the translation in english
    translation_eng: str = field(default='')
    # the list of example sentences
    example_list: List[ExampleSentence] = field(default_factory=list, compare=False)
    # some notes for this meaning, if any
    notes: str = field(default='', compare=False)
    # the forms & variability of the word
    forms: WordForms = field(default=None, compare=False)
