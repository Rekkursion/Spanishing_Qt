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
