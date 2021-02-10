from enum import Enum

from enums.pref_key import PrefKey
from enums.strs import Strs
from managers.pref_manager import PrefManager


class PartOfSpeech(Enum):
    MASCULINE = 'm'
    FEMININE = 'f'
    PLURAL_MASCULINE = 'm.pl'
    PLURAL_FEMININE = 'f.pl'
    MASCULINE_OR_FEMININE = 'm/f'
    PRONOUN = 'pron'
    PROPER_NOUN = 'n'

    VERB = 'v'
    REFLEXIVE_VERB = 'v.r'
    TRANSITIVE_VERB = 'v.t'
    INTRANSITIVE_VERB = 'v.i'

    ADJECTIVE = 'adj'

    ADVERB = 'adv'

    PHRASE = 'phr'

    CONJUNCTION = 'conj'

    INTERJECTION = 'interj'

    PREPOSITION = 'prep'

    DEFINITE_ARTICLE = 'art.def'
    INDEFINITE_ARTICLE = 'art.ind'

    # get the abbreviation of a certain part-of-speech
    def get_abbr(self):
        return self.value

    # get the fullname of a certain part-of-speech
    def get_fullname(self):
        return Strs[self.name].value[PrefManager.get_pref(PrefKey.LANG)]

    # get the formatted text of a certain part-of-speech
    def format(self):
        return f'{self.get_fullname()} [{self.get_abbr()}]'

    # check if it's a gender-variant part-of-speech or not
    def is_gender_variant(self):
        return self == PartOfSpeech.MASCULINE_OR_FEMININE or self == PartOfSpeech.PRONOUN or self == PartOfSpeech.ADJECTIVE

    # check if it's a number-variant part-of-speech or not
    def is_number_variant(self):
        return self == PartOfSpeech.MASCULINE or self == PartOfSpeech.FEMININE or self == PartOfSpeech.PLURAL_MASCULINE or self == PartOfSpeech.PLURAL_FEMININE or self == PartOfSpeech.MASCULINE_OR_FEMININE or self == PartOfSpeech.PRONOUN or self == PartOfSpeech.ADJECTIVE

    # check if it's a masculine part-of-speech or not
    def is_masculine(self):
        return self == PartOfSpeech.MASCULINE or self == PartOfSpeech.PLURAL_MASCULINE

    # check if it's a feminine part-of-speech or not
    def is_feminine(self):
        return self == PartOfSpeech.FEMININE or self == PartOfSpeech.PLURAL_FEMININE

    # check if it's a singular part-of-speech or not
    def is_singular(self):
        return self == PartOfSpeech.MASCULINE or self == PartOfSpeech.FEMININE or self == PartOfSpeech.MASCULINE_OR_FEMININE or self == PartOfSpeech.PRONOUN or self == PartOfSpeech.ADJECTIVE

    # check if it's a plural part-of-speech or not
    def is_plural(self):
        return self == PartOfSpeech.PLURAL_MASCULINE or self == PartOfSpeech.PLURAL_FEMININE

    # check if it's a verb
    def is_verb(self):
        return self == PartOfSpeech.VERB or self == PartOfSpeech.REFLEXIVE_VERB or self == PartOfSpeech.TRANSITIVE_VERB or self == PartOfSpeech.INTRANSITIVE_VERB

    # get the part-of-speech by the formatted text
    @staticmethod
    def get_pos_by_formatted_text(text: str):
        abbr_text = text[text.index('[') + 1: text.index(']')]
        for pos in PartOfSpeech:
            if pos.value == abbr_text:
                return pos
        return None
