# holds player and enemy inputs and stats and holds the functions of player and enemy turns
import random
from classes import Player, Enemy, dmg_cal, defending, special

#classes
player = Player(10, 10, 5, False, 0.0, 10)
enemy = Enemy(10, 10, 5, False, 0.0, 10)





def player_turn(turn):
    
    if player.defending:
        player.defense //= 2
        player.defending = False


    player_input = input(f"\nturn {turn}\nplayer has {player.health} health left and enemy has {enemy.health} health left\n\nspecial meter at {player.special_meter}%\n\nwhat do you do?\n\nattack\n\ndefend\n\nsurrender\n\n: ")
    
    if player_input == "attack":
        dmg = dmg_cal(player, enemy)
        enemy.health -= dmg

        print(f"\nyou did {dmg} damage to enemy")

        special(player, enemy, dmg)
        
    elif player_input == "defend":
        print("\nplayer is defending, his defense doubled!")

        defending(player)
        
    elif player_input == "surrender":
        player.health = 0
    
    else:
        raise Exception("Invalid choice")
        





def enemy_turn(turn):

    if enemy.defending:
        enemy.defense //= 2
        enemy.defending = False
    
    print(f"enemy's turn, special meter for enemy is {enemy.special_meter}%")

    enemy_choice = random.randint(1, 2)

    if enemy_choice == 1 or turn == 1 or enemy.health == enemy.max_hp:
        
        print("\nenemy attacks!")

        dmg = dmg_cal(enemy, player)
        player.health -= dmg
        
        print(f"\nenemy did {dmg} damage to player")

        special(enemy, player, dmg)
    
    elif enemy_choice == 2:
        defending(enemy)
        print("\nThe enemy is defending, his defense doubled!")
        






