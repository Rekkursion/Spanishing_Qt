from dataclasses import dataclass, field
from typing import List


@dataclass
class ExampleSentence:
    # the word for this example sentence
    word: str
    # the example sentence
    sentence: str
    # the list of translation
    translation_list: List[str] = field(default_factory=list, compare=False)
