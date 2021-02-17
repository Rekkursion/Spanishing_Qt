from enum import Enum

from enums.personal import Personal


# noinspection PyTypeChecker
class Tense(Enum):
    # present & past particles
    PARTICLES = -1
    # tenses of indicative-mood
    INDICATIVE_PRESENT = 0
    INDICATIVE_PRETERITE = 1
    INDICATIVE_IMPERFECT = 2
    INDICATIVE_CONDITIONAL = 3
    INDICATIVE_FUTURE = 4
    # tenses of subjunctive-mood
    SUBJUNCTIVE_PRESENT = 5
    SUBJUNCTIVE_IMPERFECT_1 = 6
    SUBJUNCTIVE_IMPERFECT_2 = 7
    SUBJUNCTIVE_FUTURE = 8
    # tenses of imperative-mood
    IMPERATIVE_AFFIRMATIVE = 9
    IMPERATIVE_NEGATIVE = 10

    def format(self):
        return self.name.replace('_', ' ').title()

    # @staticmethod
    # def get_all_indicative_tenses():
    #     return [tense for tense in list(Tense) if tense.name.startswith('INDICATIVE')]
    #
    # @staticmethod
    # def get_all_subjunctive_tenses():
    #     return [tense for tense in list(Tense) if tense.name.startswith('SUBJUNCTIVE')]
    #
    # @staticmethod
    # def get_all_imperative_tenses():
    #     return [tense for tense in list(Tense) if tense.name.startswith('IMPERATIVE')]

    # get all personals according to the corresponding tense (or particle)
    def get_personals(self):
        # if it's the present or past particle
        if self.value < 0:
            return [Personal.PRESENT_PARTICLE, Personal.PAST_PARTICLE]
        # if it's the general tense
        else:
            return [Personal.YO, Personal.TÚ, Personal.ÉL__ELLA__USTED, Personal.NOSOTROS, Personal.VOSOTROS, Personal.ELLOS__ELLAS__USTEDES]

    def __str__(self):
        return self.name.title()

    def __repr__(self):
        return self.name.title()
