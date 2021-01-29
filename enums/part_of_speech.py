from enum import Enum

from enums.pref_key import PrefKey
from enums.strs import Strs
from managers.pref_manager import PrefManager


class PartOfSpeech(Enum):
    MASCULINE = 'm'
    FEMININE = 'f'
    PLURAL_MASCULINE = 'f.pl'
    PLURAL_FEMININE = 'm.pl'
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

    # get the part-of-speech by the text displayed at the combo-box in meaning-form-dialog
    @staticmethod
    def get_pos_by_displayed_text(text: str):
        abbr_text = text[text.index('[') + 1: text.index(']')]
        for pos in PartOfSpeech:
            if pos.value == abbr_text:
                return pos
        return None
