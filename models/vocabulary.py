from dataclasses import dataclass, field
from typing import List, Tuple, Set

from models.meaning import Meaning


@dataclass
class Vocabulary:
    # the string of this vocabulary
    word: str
    # the list of meanings
    meaning_list: List[Meaning] = field(default_factory=list)
    # the remarks of this vocabulary, if any
    remarks: str = field(default='', compare=False)
    # the set of tags
    tag_set: Set[str] = field(default_factory=set, compare=False)
    # the list of phrases pertains to this vocabulary
    phrase_list: List[Tuple[str]] = field(default_factory=list, compare=False)
