
class Character:
    def __init__(self, name_char, class_char, race_char, level_char):
        # GENERAL INFORMATION
        self.name_char = name_char
        self.class_char = class_char
        self.race_char = race_char
        self.level_char = level_char

        # ABILITIES
        self.__st = None
        self.__dex = None
        self.__cons = None
        self.__intel = None
        self.__wis = None
        self.__ch = None

    # GENERAL INFORMATION
    @property
    def name_char(self):
        return self.name_char

    @name_char.setter
    def name_char(self, name_char):
        self.name_char = name_char

    @property
    def class_char(self):
        return self.class_char

    @class_char.setter
    def class_char(self, class_char):
        self.class_char = class_char

    @property
    def race_char(self):
        return self.race_char

    @race_char.setter
    def race_char(self, race_char):
        self.race_char = race_char

    @property
    def level_char(self):
        return self.level_char

    @level_char.setter
    def level_char(self, level_char):
        self.level_char = level_char


    # ABILITIES
    @property
    def __ability_strength(self):
        return self.__st

    @__ability_strength.setter
    def __ability_strength(self, st):
        self.__st = st

    @property
    def __ability_dex(self):
        return self.__dex

    @__ability_dex.setter
    def __ability_dex(self, dex):
        self.__dex = dex

    @property
    def __ability_cons(self):
        return self.__cons

    @__ability_cons.setter
    def __ability_cons(self, cons):
        self.__cons = cons

    @property
    def __ability_intel(self):
        return self.__intel

    @__ability_intel.setter
    def __ability_intel(self, intel):
        self.__intel = intel

    @property
    def __ability_wis(self):
        return self.__wis

    @__ability_wis.setter
    def __ability_wis(self, wis):
        self.__wis = wis

    @property
    def __ability_ch(self):
        return self.__ch

    @__ability_ch.setter
    def __ability_ch(self, ch):
        self.__ch = ch