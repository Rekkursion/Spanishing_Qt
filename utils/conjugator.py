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

    # set a field of conjugation directly
    def set_directly(self, form: str, tense: Tense, personal: Personal):
        self.__dict[tense][personal] = form

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
    argüir, erguir, seguir, delinquir, sustituir, rehuir, huir, asir
    """
    # conjugate a verb in its infinite form w/ some irregularity, if any
    @staticmethod
    def conjugate(verb: str, verb_irregularity: VerbIrregularity = None):
        # instantiate a new conjugation
        conjugation = Conjugation(verb)
        # change the stem of the infinite form, e.g., 'comenzar' -> 'comienzar'
        if verb_irregularity is not None and verb_irregularity.stem_changing_type is not None:
            basic, advanced = WordAnalyzer.change_stem(conjugation.inf, verb_irregularity.stem_changing_type)
        else:
            basic, advanced = conjugation.inf, conjugation.inf
        # the special yo-form of present tense
        sp_yo_form = VerbIrregularity.get_sp_yo_form(verb_irregularity)
        # prepare the regular yo-form of present tense no matter if it's a stem-changing verb or not
        _, non_stem_changed_yo_form, _ = conjugation.verb_type.get_conjugated(conjugation.inf, Tense.INDICATIVE_PRESENT, Personal.YO)
        # iterate all tenses
        for tense in list(Tense):
            # and all personals corresponding to the current tense
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
                    elif verb_irregularity is not None and VerbIrregularity.check_advanced_stem_changing(verb_irregularity):
                        form = advanced[:-2] + 'o'
                    else:
                        form = sp_yo_form if sp_yo_form is not None else non_stem_changed_yo_form
                    if form is not None:
                        conjugation.set(form.split(' ')[0], tense, personal)

                # if the tense is negative imperative
                elif tense == Tense.IMPERATIVE_NEGATIVE:
                    form = conjugation.get(Tense.SUBJUNCTIVE_PRESENT, personal)
                    if form is not None:
                        conjugation.set(form.split(' ')[0], tense, personal)

                # if the tense is affirmative imperative
                elif tense == Tense.IMPERATIVE_AFFIRMATIVE:
                    if personal == Personal.NOSOTROS:
                        if sp_yo_form is not None:
                            form = sp_yo_form
                        elif VerbIrregularity.check_advanced_stem_changing(verb_irregularity):
                            form = advanced[:-2] + 'o'
                        else:
                            form = non_stem_changed_yo_form
                    elif personal == Personal.VOSOTROS:
                        form = conjugation.inf
                    else:
                        form = conjugation.get(Tense.INDICATIVE_PRESENT, Personal.YO)
                    if form is not None:
                        conjugation.set(form.split(' ')[0], tense, personal)

                # the general case
                else:
                    # if there's a special yo-form of present tense, set it directly
                    if tense == Tense.INDICATIVE_PRESENT and personal == Personal.YO and sp_yo_form is not None:
                        conjugation.set_directly(sp_yo_form, tense, personal)
                    # do the basic stem-changing
                    elif tense == Tense.INDICATIVE_PRESENT and personal.should_change_stem():
                        conjugation.set(basic, tense, personal)
                    # do the advanced stem-changing
                    elif (tense == Tense.PARTICLES and personal == Personal.PRESENT_PARTICLE) or\
                            (tense == Tense.INDICATIVE_PRETERITE and personal in (Personal.ÉL__ELLA__USTED, Personal.ELLOS__ELLAS__USTEDES)):
                        conjugation.set(advanced, tense, personal)
                    else:
                        conjugation.set(conjugation.inf, tense, personal)
        # return the new conjugation
        return conjugation
