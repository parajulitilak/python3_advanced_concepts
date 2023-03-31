import random


class enemy:

    #class instances var
    hp = 220

    #instance function
    def __init__(self,e_low,e_high):
        #instance variables
        self.e_low = e_low
        self.e_high = e_high

    def e_damage(self):
        print("Damage =",self.e_low)

    def h_p(self):
        print("HP = ",self.hp)


enemy1 = enemy(60, 120)
enemy1.e_damage()
enemy1.h_p()

enemy2 = enemy(30, 80)
enemy2.e_damage()

#class instances calling
enemy2.h_p()