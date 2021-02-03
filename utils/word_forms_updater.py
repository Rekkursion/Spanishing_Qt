from enums.part_of_speech import PartOfSpeech
from enums.word_variability import WordVariability


class WordFormsUpdater:
    def __init__(self, grp_genders, grp_numbers, le_m_s, le_f_s, le_m_pl, le_f_pl):
        # the button-group of gender-variability
        self.__grp_genders = grp_genders
        # the button-group of number-variability
        self.__grp_numbers = grp_numbers
        # the line-edit of the form in masculine & singular
        self.__le_m_s = le_m_s
        # the line-edit of the form in feminine & singular
        self.__le_f_s = le_f_s
        # the line-edit of the form in masculine & plural
        self.__le_m_pl = le_m_pl
        # the line-edit of the form in feminine & plural
        self.__le_f_pl = le_f_pl

    # update the forms by the change of part-of-speech, gender-variability, & number-variability
    def update(self, pos: PartOfSpeech, gender_variability, number_variability):
        # get the variabilities of genders & numbers according to the part-of-speech
        is_gender_variant = pos.is_gender_variant()
        is_number_variant = pos.is_number_variant()
        # set the enabilities of gender-variability radio-buttons
        for button in self.__grp_genders.buttons():
            button.setEnabled(is_gender_variant)
        if pos == PartOfSpeech.MASCULINE_OR_FEMININE:
            self.__grp_genders.buttons()[2].setEnabled(False)
        # set the enabilities of number-variability radio-buttons
        for button in self.__grp_numbers.buttons():
            button.setEnabled(is_number_variant)
        # get the gender & number of the part-of-speech
        is_m = pos.is_masculine()
        is_f = pos.is_feminine()
        is_s = pos.is_singular()
        is_pl = pos.is_plural()
        g_v = gender_variability == WordVariability.INVARIANT
        n_v = number_variability == WordVariability.INVARIANT
        # set the enabilities of line-edits
        self.__le_m_s.setEnabled((is_gender_variant and is_number_variant) or (is_number_variant and is_m and (not n_v or is_s)))
        self.__le_f_s.setEnabled((is_gender_variant and is_number_variant and not g_v) or (is_number_variant and is_f and (not n_v or is_s)))
        self.__le_m_pl.setEnabled((is_gender_variant and is_number_variant and not n_v) or (is_number_variant and is_m and (not n_v or is_pl)))
        self.__le_f_pl.setEnabled((is_gender_variant and is_number_variant and not g_v and not n_v) or (is_number_variant and is_f and (not n_v or is_pl)))
