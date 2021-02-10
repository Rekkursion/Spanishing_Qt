from enum import Enum


# noinspection NonAsciiCharacters
class Personal(Enum):
    # singular 1st-personal
    YO = 0
    # informal singular 2nd-personal
    TÚ = 1
    # formal singular 2nd-personal & singular 3rd-personal
    UD = 2
    # plural 1st-personal
    NOSOTROS = 3
    # informal plural 2nd-personal
    VOSOTROS = 4
    # formal plural 2nd-personal & plural 3rd-personal
    UDS = 5
