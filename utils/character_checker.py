# noinspection SpellCheckingInspection
class CharChecker:
    # check a certain character is a consonant or not
    @staticmethod
    def is_consonant(char: str):
        if len(char) == 1:
            return char.lower() in 'bcdfghjklmnñpqrstvwxyz'
        elif len(char) == 2:
            return char.lower() in ('ll', 'ch', 'rr')
        return False

    # check a certain pair of characters is a consonant-cluster
    @staticmethod
    def is_consonant_cluster(pair_of_chars: str):
        return (len(pair_of_chars) == 2 and pair_of_chars.lower()[0] in 'pbtcgf' and pair_of_chars.lower()[1] in 'lr') or pair_of_chars.lower() == 'dr'

    # check a certain character is a consonant or a consonant-cluster
    @staticmethod
    def is_consonant_or_consonant_cluster(char: str):
        return CharChecker.is_consonant(char) or CharChecker.is_consonant_cluster(char)

    # check a certain character is a vowel or not
    @staticmethod
    def is_vowel(char: str):
        return len(char) == 1 and char.lower() in 'aoeiuáóéíúü'

    # check a certain character is a stressed vowel or not
    @staticmethod
    def is_stressed(char: str):
        return len(char) == 1 and char.lower() in 'áóéíú'

    # check a certain character is a strong vowel or not
    @staticmethod
    def is_strong_vowel(char: str):
        return len(char) == 1 and char.lower() in 'aoeáóéíú'

    # check a certain character is a weak vowel or not
    @staticmethod
    def is_weak_vowel(char: str):
        return len(char) == 1 and char.lower() in 'iuü'
