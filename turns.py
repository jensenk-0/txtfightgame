# holds player and enemy inputs and stats
import random
from classes import Player, Enemy, dmg_cal, defending


player = Player(10, 10, 5, False, 0)
enemy = Enemy(10, 10, 5, False, 0)

def player_turn(turn):
    
    if player.defending:
        player.defense //= 2
        player.defending = False


    player_input = input(f"\nturn {turn}\nplayer has {player.health} health left and enemy has {enemy.health} health left\nwhat do you do?\nattack\ndefend\nsurrender\n: ")
    
    if player_input == "attack":
        dmg = dmg_cal(player, enemy)
        enemy.health -= dmg
        print(f"\nyou did {dmg} damage to enemy")
        
    elif player_input == "defend":
        print("\nplayer is defending, his defense doubled!")
        defending(player)
        
    elif player_input == "surrender":
        player.health = 0
    
    else:
        raise Exception("Invalid choice")
        


#global variable to store enemy max hp for smarter enemy choices
enemy_max_hp = enemy.health

def enemy_turn(turn):

    if enemy.defending:
        enemy.defense //= 2
        enemy.defending = False

    enemy_choice = random.randint(1, 2)

    if enemy_choice == 1 or turn == 1 or enemy.health == enemy_max_hp:
        
        print("\nenemy attacks!")
        dmg = dmg_cal(enemy, player)
        player.health -= dmg
        print(f"\nenemy did {dmg} damage to player")
    
    elif enemy_choice == 2:
        defending(enemy)
        print("\nThe enemy is defending, his defense doubled!")
        






