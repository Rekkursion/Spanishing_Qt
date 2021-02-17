from enum import Enum


class StemChangingType(Enum):
    # e -> ie
    E2IE = 0
    # e -> i
    E2I = 1
    # advanced e -> i, e.g., medir -> midiendo
    E2I_ADVANCED = 2
    # o -> ue (including o -> hue, e.g., oler -> huelo)
    O2UE = 3
    # advanced o -> ue, e.g., dormir -> durmiendo
    O2UE_ADVANCED = 4
    # i -> ie, e.g., adquirir -> adquiero, inquirir -> inquiero
    I2IE = 5
    # u -> ue, e.g., jugar -> juego
    U2UE = 6

    def format(self):
        return self.name.lower().replace('2', ' > ').replace('_advanced', ' (Advanced)')
