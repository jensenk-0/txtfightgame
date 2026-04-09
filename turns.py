# holds player and enemy inputs and stats and holds the functions of player and enemy turns
import random
from classes import Player, Enemy, attack, defending, special


#classes

mage = Player(10, 20, 5, False, 0.0, 10)
rogue = Player(15, 15, 10, False, 0.0, 15)
tank = Player(20, 10, 15, False, 0.0, 20)
    
def choose_character():
    player_choice = input("choose character: rogue, tank, mage\n:")
    if player_choice == "rogue":
        return rogue
    elif player_choice == "tank":
        return tank
    elif player_choice == "mage":
        return mage
    else:
        raise ValueError

player = choose_character()

enemy = Enemy(10, 10, 5, False, 0.0, 10)

def player_turn(turn):
    
    if player.defending:
        player.defense //= 2
        player.defending = False


    player_input = input(f"\nturn {turn}\nplayer has {player.health} health left and enemy has {enemy.health} health left\n\nspecial meter at {player.special_meter}%\n\nwhat do you do?\n\nattack\n\ndefend\n\nsurrender\n\n: ")
    
    if player_input == "attack":
        attack(player, enemy)
        
    elif player_input == "defend":
        defending(player)
        
    elif player_input == "surrender":
        player.health = 0
    
    else:
        raise Exception("Invalid choice")
        





def enemy_turn(turn):

    if enemy.defending:
        enemy.defense //= 2
        enemy.defending = False
    
    print(f"enemy's turn, special meter for enemy is {enemy.special_meter}%\n")

    enemy_choice = random.randint(1, 2)

    if enemy_choice == 1 or turn == 1 or enemy.health == enemy.max_hp:
        attack(enemy, player)

    elif enemy_choice == 2:
        defending(enemy)
        
        






