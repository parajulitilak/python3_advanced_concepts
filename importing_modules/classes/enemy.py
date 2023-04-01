class Enemy:
    def __init__(self, hp, mp):
        self.hp_max = hp
        self.hp = hp
        self.mp_max = mp
        self.mp = mp

    def get_hp(self):
        return self.hp
