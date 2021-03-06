from enums.stem_changing_type import StemChangingType
from utils.character_checker import CharChecker as Checker
from utils.syllable_linked_list import SyllableLinkedList, NodeType


class WordAnalyzer:
    # split a certain word into syllables
    @staticmethod
    def split_syllables(word: str):
        # the lowered word
        lowered_word = word.lower()
        # the list of components of this word, each element is a pair, <component, int>,
        # where the int-value represents its type: 1 = vowel-component, 0 = consonant-component, -1 = non-latin alphabet
        linked_list = SyllableLinkedList()
        """ step 1. iterate the whole word to build up the list of components """
        k = 0; length = len(word)
        while k < length:
            ch = lowered_word[k]
            # if it's a consonant
            if Checker.is_consonant(ch):
                # if it's a consonant-cluster, 'll', 'rr', or 'ch'
                if k + 1 < length and Checker.is_consonant_or_consonant_cluster(lowered_word[k:k + 2]):
                    linked_list.push_back(word[k:k + 2], NodeType.CONSONANT)
                    k += 2
                # otherwise, it's a single-character consonant
                else:
                    linked_list.push_back(word[k:k + 1], NodeType.CONSONANT)
                    k += 1
            # if it's a vowel
            elif Checker.is_vowel(ch):
                # i actually have no idea if this case could possibly happen by any chance, but just in case
                if k + 3 < length and k > 0 and lowered_word[k - 1:k] in 'qg' and ch == 'u' and lowered_word[k + 1:k + 2] == 'i' and Checker.is_strong_vowel(lowered_word[k + 2:k + 3]) and Checker.is_weak_vowel(lowered_word[k + 3:k + 4]):
                    linked_list.push_back(word[k:k + 4], NodeType.VOWEL)
                    k += 4
                # check the case of triphthong
                # if it's a weak-strong-weak structure, it's the case of triphthong, e.g. 'iai', 'iei'
                elif k + 2 < length and Checker.is_weak_vowel(ch) and Checker.is_strong_vowel(lowered_word[k + 1:k + 2]) and Checker.is_weak_vowel(lowered_word[k + 2:k + 3]):
                    linked_list.push_back(word[k:k + 3], NodeType.VOWEL)
                    k += 3
                # special case: like 'quien' or 'guión'
                elif k + 2 < length and k > 0 and lowered_word[k - 1:k] in 'qg' and ch == 'u' and ((lowered_word[k + 1:k + 2] == 'i' and Checker.is_vowel(lowered_word[k + 2:k + 3])) or (lowered_word[k + 1:k + 2] == 'e' and Checker.is_weak_vowel(lowered_word[k + 2:k + 3]))):
                    linked_list.push_back(word[k:k + 3], NodeType.VOWEL)
                    k += 3
                # check the case of diphthong
                # if it's a weak-weak, weak-strong, or strong-weak structure, it's the case of diphthong, e.g., 'ia', 'ui', 'ou'
                elif k + 1 < length and ((Checker.is_weak_vowel(ch) and Checker.is_weak_vowel(lowered_word[k + 1:k + 2])) or (Checker.is_strong_vowel(ch) and Checker.is_weak_vowel(lowered_word[k + 1:k + 2])) or (Checker.is_weak_vowel(ch) and Checker.is_strong_vowel(lowered_word[k + 1:k + 2]))):
                    linked_list.push_back(word[k:k + 2], NodeType.VOWEL)
                    k += 2
                # the case of monophthong
                else:
                    linked_list.push_back(word[k:k + 1], NodeType.VOWEL)
                    k += 1
            # if it's neither a consonant nor a vowel, maybe it's a space or something else
            else:
                linked_list.push_back(word[k:k + 1], NodeType.OTHER)
                k += 1
        """ step 2. distribute ONLY ONE consonant-component to the following vowel-component """
        for q in linked_list.as_list_copied():
            # if its a vowel-component and the preceding is a consonant-component
            if q.node_type == NodeType.VOWEL and q.prev_p is not None and q.prev_p.node_type == NodeType.CONSONANT:
                linked_list.combine_with_previous_node(q)
        """ step 3. distribute the rest consonant-component(s) to the PRECEDING vowel-component """
        for q in linked_list.as_list_copied():
            # if its a vowel-component and the following is a consonant-component
            while q.node_type == NodeType.VOWEL and q.next_p is not None and q.next_p.node_type == NodeType.CONSONANT:
                linked_list.combine_with_next_node(q)
        """ step 4. deal w/ the special case that the first syllable begins w/ two consonant-characters, e.g., sheriff """
        for q in linked_list.as_list_copied():
            # if its a vowel-component and the preceding is a consonant-component
            while q.node_type == NodeType.VOWEL and q.prev_p is not None and q.prev_p.node_type == NodeType.CONSONANT:
                linked_list.combine_with_previous_node(q)
        print(linked_list)
        # return it as a python-list
        return linked_list.as_list_copied()

    # get the stressed syllable of a certain word
    # return: (<the stressed syllable>, <the index of the syllable>, <the index of string where the syllable begins>)
    @staticmethod
    def get_stressed_syllable(syllable_list):
        # the last syllable (in the case that the last component is an OTHER-type, i.e., '!' or spaces)
        last_syllable = None
        # the index of the last syllable in the list
        idx_of_last_syllable = -1
        # the index of word
        idx_of_word = 0
        # iterate the whole list to find the stressed syllable
        for idx_of_syllables, syllable in enumerate(syllable_list):
            # iterate this single syllable to try if there's a stressed alphabet, i.e., 'á', 'ó', 'é', 'í', 'ú'
            for ch in syllable.component:
                if Checker.is_stressed(ch):
                    return syllable.component, idx_of_syllables, idx_of_word
            # update the index of word
            idx_of_word += len(syllable.component)
            # update the last syllable
            if syllable.node_type != NodeType.OTHER:
                last_syllable = syllable
                idx_of_last_syllable = idx_of_syllables
        # if there's no stressed alphabet, take the last syllable a look
        if last_syllable is not None:
            if last_syllable.component.lower().endswith(('n', 's', 'a', 'o', 'e', 'i', 'u', 'á', 'ó', 'é', 'í', 'ú')) and \
                    last_syllable.prev_p is not None and last_syllable.prev_p.node_type != NodeType.OTHER:
                return last_syllable.prev_p.component, idx_of_last_syllable - 1, idx_of_word - len(last_syllable.component) - len(last_syllable.prev_p.component)
            else:
                return last_syllable.component, idx_of_last_syllable, idx_of_word - len(last_syllable.component)

    # change the stem of a certain verb according to the type of the stem-changing
    @staticmethod
    def change_stem(inf: str, stem_changing_type: StemChangingType):
        # split the infinite-form into several syllables
        syllables = WordAnalyzer.split_syllables(inf)
        # if the number of syllables is smaller than 2, directly return the infinite-form
        if len(syllables) < 2:
            return inf, inf
        # otherwise, do the replacement at the second to last syllable
        basic_second_to_last_syllable = syllables[-2].component.replace(stem_changing_type.get_before(), stem_changing_type.get_after())
        # join the replaced syllables into a string
        basic = ''.join([*map(lambda x: x.component, syllables[:-2]), basic_second_to_last_syllable, syllables[-1].component])
        # if it's an advanced type of stem-changing
        advanced_second_to_last_syllable = syllables[-2].component.replace(stem_changing_type.get_before(), stem_changing_type.get_advanced_after())
        # join the replaced syllables into a string
        advanced = ''.join([*map(lambda x: x.component, syllables[:-2]), advanced_second_to_last_syllable, syllables[-1].component])
        # return both basic & advanced stem-changed forms
        return basic, advanced
