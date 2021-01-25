from dataclasses import dataclass, field
from typing import Dict, List, Tuple

from enums.part_of_speech import PartOfSpeech


@dataclass
class Meaning:
    # the part-of-speech
    pos: PartOfSpeech
    # the dictionary of translations (multiple languages supported)
    translation_dict: Dict[str, str] = field(default_factory=dict, compare=False)
    # the list of example sentences
    example_list: List[Tuple[str]] = field(default_factory=list, compare=False)
    # some notes for this meaning, if any
    notes: str = field(default='', compare=False)
