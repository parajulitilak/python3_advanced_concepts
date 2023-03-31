import random


class enemy:
    def __init__(self,e_low,e_high):
        self.e_low = e_low
        self.e_high = e_high

    def attack_pow(self):
        print(self.e_low)

enemy1 = enemy(50,90)
enemy1.attack_pow()