from enum import Enum


class PartOfSpeech(Enum):
    MASCULINE = 'm'
    FEMININE = 'f'
    PLURAL_MASCULINE = 'f.pl'
    PLURAL_FEMININE = 'm.pl'
    MASCULINE_OR_FEMININE = 'm/f'
    PRONOUN = 'pron'
    PROPER_NOUN = 'n'

    VERB = 'v'
    REFLEXIVE_VERB = 'ref.v'

    ADJECTIVE = 'adj'

    ADVERB = 'adv'

    PHRASE = 'phr'

    CONJUNCTION = 'conj'

    INTERJECTION = 'interj'

    PREPOSITION = 'prep'

    DEFINITE_ARTICLE = 'def.art'
    INDEFINITE_ARTICLE = 'ind.art'

    # get the abbreviation of a certain part-of-speech
    def get_abbr(self):
        return self.value
