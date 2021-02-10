from dataclasses import dataclass, field
from typing import List, Tuple, Set

from models.meaning import Meaning
from models.verb_irregularity import VerbIrregularity


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
    # the verb-irregularity if this vocabulary has at least one verb-meaning and if it has some irregularity
    verb_irregularity: VerbIrregularity = field(default=None)
