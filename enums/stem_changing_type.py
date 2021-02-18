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

    def format(self):
        return self.name.lower().replace('2', ' > ').replace('_advanced', ' (Advanced)')
