from dataclasses import dataclass, field
from typing import List

from enums.personal import Personal
from enums.stem_changing_type import StemChangingType
from enums.tense import Tense


@dataclass
class MiscIrregularForm:
    # the mood & tense (including particles) where this irregular form at
    tense: Tense
    # the personal of this form (1st, 2nd, or 3rd/singular or plural)
    personal: Personal
    # the string of this irregular form
    sp_form: str


# noinspection SpellCheckingInspection,NonAsciiCharacters
@dataclass
class VerbIrregularity:
    # the stem-changing type
    stem_changing_type: StemChangingType = field(default=None)
    # the special form of past particle, e.g., poner: puesto, romper: roto
    sp_past_particle: str = field(default=None)
    # the special form of 1st-personal singular in simple tense, e.g., tener: tengo, padecer: padezco
    sp_yo_form: str = field(default=None)
    # the stem of special form in preterite tense, e.g., andar: anduv-
    sp_preterite_stem: str = field(default=None)
    # the stem of special form in imperfect tense, e.g., ser: er-
    sp_imperfect_stem: str = field(default=None)
    # the stem of special form in conditional & future tenses, e.g., querer: querr-
    sp_cond_and_future_stem: str = field(default=None)
    # the stem of special form in present subjunctive, e.g., saber: sep-
    sp_present_subjunctive_stem: str = field(default=None)
    # the special form of tú-form in affirmative imperative, e.g., tener: ten, venir: ven, ser: sé
    sp_tú_form_affirmative_imperative: str = field(default=None)
    # the other types of special forms/irregularities, if any
    misc_forms: List[MiscIrregularForm] = field(default_factory=list)

    # check if the type of stem-changing is an advanced one or not
    @staticmethod
    def check_advanced_stem_changing(verb_irr):
        return verb_irr is not None and verb_irr.stem_changing_type is not None and verb_irr.stem_changing_type.is_advanced()

    # get the special past particle, if any
    @staticmethod
    def get_sp_past_particle(verb_irr):
        return None if verb_irr is None else verb_irr.sp_past_particle

    # get the special yo-form of present tense, if any
    @staticmethod
    def get_sp_yo_form(verb_irr):
        return None if verb_irr is None else verb_irr.sp_yo_form

    # get the special stem of preterite tense, if any
    @staticmethod
    def get_sp_preterite_stem(verb_irr):
        return None if verb_irr is None else verb_irr.sp_preterite_stem
