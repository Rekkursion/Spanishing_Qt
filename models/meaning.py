from dataclasses import dataclass, field
from typing import List

from enums.part_of_speech import PartOfSpeech
from models.example_sentence import ExampleSentence


@dataclass
class Meaning:
    # the part-of-speech
    pos: PartOfSpeech
    # the translation in chinese
    translation_chi: str = field(default='')
    # the translation in english
    translation_eng: str = field(default='')
    # the list of example sentences
    example_list: List[ExampleSentence] = field(default_factory=list, compare=False)
    # some notes for this meaning, if any
    notes: str = field(default='', compare=False)
