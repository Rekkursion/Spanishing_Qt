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
