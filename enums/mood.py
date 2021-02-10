from enum import Enum


class MoodAndTense(Enum):
    # present particle
    PRESENT_PARTICLE = 0
    # past particle
    PAST_PARTICLE = 1
    # tenses of indicative-mood
    INDICATIVE_SIMPLE = 2
    INDICATIVE_PRETERITE = 3
    INDICATIVE_IMPERFECT = 4
    INDICATIVE_CONDITIONAL = 5
    INDICATIVE_FUTURE = 6
    # tenses of subjunctive-mood
    SUBJUNCTIVE_SIMPLE = 7
    SUBJUNCTIVE_IMPERFECT_1 = 8
    SUBJUNCTIVE_IMPERFECT_2 = 9
    SUBJUNCTIVE_FUTURE = 10
    # tenses of imperative-mood
    IMPERATIVE_AFFIRMATIVE = 11
    IMPERATIVE_NEGATIVE = 12
