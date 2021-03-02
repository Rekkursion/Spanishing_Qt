import copy

from enums.personal import Personal
from enums.tense import Tense
from enums.verb_type import VerbType
from models.verb_irregularity import VerbIrregularity
from utils.word_analyzer import WordAnalyzer


# noinspection PyTypeChecker
class Conjugation:
    def __init__(self, verb: str):
        # the infinitive form of the verb
        self.__verb = verb
        # split the verb (possibly a verb phrase) into the infinitive form and the rest parts
        self.__inf, *self.__rest_part_list = verb.split(' ', maxsplit=1)
        # get the verb-type (ar/er/ir/arse/erse/irse)
        self.__verb_type = VerbType.check_verb_type(self.__inf)
        # the dictionary of the whole conjugation
        self.__dict = {tense: {personal: None for personal in tense.get_personals()} for tense in list(Tense)}

    @property
    def verb(self):
        return self.__verb

    @property
    def inf(self):
        return self.__inf

    @property
    def verb_type(self):
        return self.__verb_type

    # set a field of conjugation w/ a certain tense & a certain personal
    def set(self, form: str, tense: Tense, personal: Personal):
        if tense in self.__dict and personal in self.__dict[tense]:
            success, conjugated, spelling_change = self.verb_type.get_conjugated(form, tense, personal)
            # if the conjugating process succeeded
            if success and conjugated != '':
                # it's a simple verb w/o any phrase parts
                if len(self.__rest_part_list) == 0:
                    self.__dict[tense][personal] = conjugated
                # it's a verb phrase, e.g., 'tener esperanza'
                else:
                    self.__dict[tense][personal] = f'{conjugated} {" ".join(self.__rest_part_list)}'

    # get a field of conjugation w/ a certain tense & a certain personal
    def get(self, tense: Tense, personal: Personal):
        if tense in self.__dict and personal in self.__dict[tense]:
            return self.__dict[tense][personal]
        return None

    # get the whole conjugation as a python-dictionary
    def get_all(self):
        return copy.deepcopy(self.__dict)


# noinspection PyTypeChecker,SpellCheckingInspection
class Conjugator:
    """
    atreverse, quejarse, medir, comenzar, almorzar, dormir, torcer, padecer, seducir, degollar, aullar,
    apaciguar, jugar, tocar, gozar,
    freír, sonreír, tañer, empeller, teñir, bruñir, bullir,
    hervir, roer, oír, traer, embaír, creer, criar, confiar, cambiar, limpiar
    garuar, evacuar, graduar, graduarse, apaciguar,
    argüir, erguir, seguir, delinquir, sustituir, rehuir, huir
    """
    # conjugate a verb in infinitive form w/ some irregularity, if any
    @staticmethod
    def conjugate(verb: str, verb_irregularity: VerbIrregularity = None):
        # instantiate a new conjugation
        conjugation = Conjugation(verb)
        # change the stem of the infinite-form, e.g., for the word 'comenzar' -> 'comienzar'
        if verb_irregularity is not None and verb_irregularity.stem_changing_type is not None:
            basic, advanced = WordAnalyzer.change_stem(conjugation.inf, verb_irregularity.stem_changing_type)
        else:
            basic, advanced = conjugation.inf, conjugation.inf
        # prepare the form of first personal present no matter if it's actually a stem-changing verb or not
        _, non_stem_changed_first_personal_present_form, _ = conjugation.verb_type.get_conjugated(conjugation.inf, Tense.INDICATIVE_PRESENT, Personal.YO)
        # iterate all tenses
        for tense in list(Tense):
            # and all personals corresponding to the tense
            for personal in tense.get_personals():
                # if the tense is imperfect-1, imperfect-2, or future of the subjunctive mood
                if tense in (Tense.SUBJUNCTIVE_IMPERFECT_1, Tense.SUBJUNCTIVE_IMPERFECT_2, Tense.SUBJUNCTIVE_FUTURE):
                    form = conjugation.get(Tense.INDICATIVE_PRETERITE, Personal.ELLOS__ELLAS__USTEDES)
                    if form is not None:
                        conjugation.set(form.split(' ')[0], tense, personal)

                # if the tense is present subjunctive
                elif tense == Tense.SUBJUNCTIVE_PRESENT:
                    if personal.should_change_stem():
                        form = conjugation.get(Tense.INDICATIVE_PRESENT, Personal.YO)
                    elif verb_irregularity is not None and verb_irregularity.is_advanced_stem_changing():
                        form = advanced[:-2] + 'o'
                    else:
                        form = non_stem_changed_first_personal_present_form
                    if form is not None:
                        conjugation.set(form.split(' ')[0], tense, personal)

                # if the tense is negative imperative
                elif tense == Tense.IMPERATIVE_NEGATIVE:
                    form = conjugation.get(Tense.SUBJUNCTIVE_PRESENT, personal)
                    if form is not None:
                        conjugation.set(form.split(' ')[0], tense, personal)

                # the general case
                else:
                    # do the basic stem-changing if it's a stem-changing verb
                    if tense in (Tense.INDICATIVE_PRESENT, Tense.IMPERATIVE_AFFIRMATIVE) and personal.should_change_stem():
                        conjugation.set(basic, tense, personal)
                    # do the advanced stem-changing
                    elif (tense == Tense.PARTICLES and personal == Personal.PRESENT_PARTICLE) or\
                            (tense == Tense.INDICATIVE_PRETERITE and personal in (Personal.ÉL__ELLA__USTED, Personal.ELLOS__ELLAS__USTEDES)) or\
                            (tense == Tense.IMPERATIVE_AFFIRMATIVE and personal == Personal.NOSOTROS):
                        conjugation.set(advanced, tense, personal)
                    else:
                        conjugation.set(conjugation.inf, tense, personal)
        # return the new conjugation
        return conjugation
