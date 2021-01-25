from enum import Enum


class FixedSizes(Enum):
    TINY = 8
    SMALL = 10
    MEDIUM = 12
    LARGE = 14
    GIGANTIC = 16

    # for the convenience (no need to write FixedSizes.XXX.value, FixedSizes.XXX is enough)
    def __get__(self, instance, owner):
        return self.value
