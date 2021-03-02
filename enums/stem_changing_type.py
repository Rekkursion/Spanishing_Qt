from enum import Enum


class StemChangingType(Enum):
    # e -> ie
    E2IE = 0
    # advanced e -> ie, e.g., hervir -> hirviendo
    E2IE_ADVANCED = 1
    # e -> i
    E2I = 2
    # advanced e -> i, e.g., medir -> midiendo
    E2I_ADVANCED = 3
    # o -> ue (including o -> hue, e.g., oler -> huelo)
    O2UE = 4
    # advanced o -> ue, e.g., dormir -> durmiendo
    O2UE_ADVANCED = 5
    # i -> ie, e.g., adquirir -> adquiero, inquirir -> inquiero
    I2IE = 6
    # u -> ue, e.g., jugar -> juego
    U2UE = 7

    # check if it's an advanced type of stem-changing
    def is_advanced(self):
        return self.name.find('_') != -1

    # get the form before the stem-changing
    def get_before(self):
        return self.name.lower()[:self.name.find('2')]

    # get the basic form after the stem-changing
    def get_after(self):
        idx_of_underline = self.name.find('_')
        if idx_of_underline == -1:
            return self.name.lower()[self.name.find('2') + 1:]
        return self.name.lower()[self.name.find('2') + 1:idx_of_underline]

    # get the advanced form after the stem-changing
    def get_advanced_after(self):
        # e.g., hervir (e2ie), medir (e2i)
        if self == StemChangingType.E2IE_ADVANCED or self == StemChangingType.E2I_ADVANCED:
            return 'i'
        # e.g., dormir
        elif self == StemChangingType.O2UE_ADVANCED:
            return 'u'
        # non-advanced cases
        return self.get_before()

    def format(self):
        return self.name.lower().replace('2', ' > ').replace('_advanced', ' (Advanced)')
