from enum import Enum


# noinspection NonAsciiCharacters
class Personal(Enum):
    # the present particle
    PRESENT_PARTICLE = -2
    # the past particle
    PAST_PARTICLE = -1
    # singular 1st-personal
    YO = 0
    # informal singular 2nd-personal
    TÚ = 1
    # formal singular 2nd-personal & singular 3rd-personal
    ÉL__ELLA__USTED = 2
    # plural 1st-personal
    NOSOTROS = 3
    # informal plural 2nd-personal
    VOSOTROS = 4
    # formal plural 2nd-personal & plural 3rd-personal
    ELLOS__ELLAS__USTEDES = 5

    # check if the personal is the one which should change its stem when conjugating the first personal present
    def should_change_stem(self):
        return self in (Personal.YO, Personal.TÚ, Personal.ÉL__ELLA__USTED, Personal.ELLOS__ELLAS__USTEDES)

    def format(self):
        return self.name.title().replace('__', '/').replace('_', ' ')

    def __str__(self):
        return self.name.title()

    def __repr__(self):
        return self.name.title()
