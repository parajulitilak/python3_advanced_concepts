import random


player_power = 300
enemy_attack_low = 60
enemy_attack_high = 120


while player_power > 0:
    damage = random.randrange(enemy_attack_low,enemy_attack_high)
    player_power = player_power - damage

    if player_power <=50:
        player_power = 50

    print("Enemy strikes = ",damage,"Player power remaining ",player_power)

    if player_power ==50:
        print("\nYou have low health. Do you want to add more power ??")
        x = input("Type 'y' for yes and any other keys for no :")

        if x is 'y':
            powe = int(input("\nEnter power less than 300 :"))
            player_power =powe
        else:
            break