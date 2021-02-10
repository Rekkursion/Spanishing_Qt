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
    # u -> ue
    U2UE = 5
