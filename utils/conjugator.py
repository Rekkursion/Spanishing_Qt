import copy

from enums.personal import Personal
from enums.tense import Tense
from enums.verb_type import VerbType
from models.verb_irregularity import VerbIrregularity


class Conjugation:
    # noinspection PyTypeChecker
    def __init__(self, inf: str):
        # the infinitive form of the verb
        self.__inf = inf
        # get the verb-type (ar/er/ir/arse/erse/irse)
        self.__verb_type = VerbType.check_verb_type(inf)
        # the dictionary of the whole conjugation
        self.__dict = {tense: {personal: None for personal in tense.get_personals()} for tense in list(Tense)}

    @property
    def inf(self):
        return self.__inf

    @property
    def verb_type(self):
        return self.__verb_type

    # set a field of conjugation w/ a certain tense & a certain personal
    def set(self, form: str, tense: Tense, personal: Personal):
        if tense in self.__dict and personal in self.__dict[tense]:
            self.__dict[tense][personal] = self.verb_type.get_conjugated(form, tense, personal)[1]

    # get a field of conjugation w/ a certain tense & a certain personal
    def get(self, tense: Tense, personal: Personal):
        if tense in self.__dict and personal in self.__dict[tense]:
            return self.__dict[tense][personal]
        return None

    # get the whole conjugation as a python-dictionary
    def get_all(self):
        return copy.deepcopy(self.__dict)


# noinspection PyTypeChecker
class Conjugator:
    """
    atreverse, quejarse, medir, comenzar, almorzar, dormir, torcer, padecer, seducir
    freír, sonreír, huir, fluir, sustituir, seguir, conseguir, tañer, teñir
    evacuar, graduar, graduarse, apaciguar, hervir
    """
    # conjugate a verb in infinitive form w/ some irregularity, if any
    @staticmethod
    def conjugate(inf: str, verb_irregularity: VerbIrregularity = None):
        # instantiate a new conjugation
        conjugation = Conjugation(inf)
        # iterate all tenses
        for tense in list(Tense):
            # and all personals corresponding to the tense
            for personal in tense.get_personals():
                # if the tense is imperfect-1, imperfect-2, or future of the subjunctive mood
                if tense in (Tense.SUBJUNCTIVE_IMPERFECT_1, Tense.SUBJUNCTIVE_IMPERFECT_2, Tense.SUBJUNCTIVE_FUTURE):
                    conjugation.set(conjugation.get(Tense.INDICATIVE_PRETERITE, Personal.ELLOS__ELLAS__USTEDES), tense, personal)
                # if the tense is imperative-affirmative
                elif tense == Tense.IMPERATIVE_AFFIRMATIVE:
                    conjugation.set(conjugation.get(Tense.INDICATIVE_PRESENT, Personal.YO), tense, personal)
                # the rest cases
                else:
                    conjugation.set(conjugation.inf, tense, personal)
        # return the new conjugation
        return conjugation
