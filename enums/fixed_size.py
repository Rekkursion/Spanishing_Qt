from enum import Enum


class FixedSizes(Enum):
    TINY = 10
    SMALL = 12
    MEDIUM = 14
    LARGE = 16
    GIGANTIC = 18

    # for the convenience (no need to write FixedSizes.XXX.value, FixedSizes.XXX is enough)
    def __get__(self, instance, owner):
        return self.value
