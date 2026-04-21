# holds player and enemy inputs and stats and holds the functions of player and enemy turns
import random
from classes import Player, Enemy, attack, defending, special_attack, def_reset


#classes

mage = Player(10, 20, 5, 0.0, 10)
rogue = Player(15, 15, 10, 0.0, 15)
tank = Player(20, 10, 15, 0.0, 20)
    
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

def difficulty():
    player_choice = input("choose difficulty: easy, normal, hard, boss fight\n:")
    if player_choice == "easy":
        return Enemy(10, 5, 5, 0.0, 10)
    elif player_choice == "normal":
        return Enemy(15, 10, 10, 0.0, 15)
    elif player_choice == "hard":
        return Enemy(20, 15, 15, 0.0, 20)
    elif player_choice == "boss fight":
        return Enemy(50, 10, 10, 100.0, 25)
    else:
        raise Exception("invalid input")

enemy = difficulty()

def player_turn(turn):
    
    def_reset(player)

    player_input = input(f"\nturn {turn}\nplayer has {player.health} health left and enemy has {enemy.health} health left\n\nspecial meter at {player.special_meter}%\n\nwhat do you do?\n\nattack\n\ndefend\n\nspecial attack\n\nsurrender\n\n: ")
    
    if player_input == "attack":
        attack(player, enemy)
        
    elif player_input == "defend":
        defending(player)

    elif player_input == "special":
        special_attack(player, enemy)
        
    elif player_input == "surrender":
        player.health = 0
    
    else:
        raise Exception("Invalid choice")
        





def enemy_turn(turn):
    
    def_reset(enemy)

    print(f"enemy's turn, special meter for enemy is {enemy.special_meter}%\n")

    enemy_choice = random.randint(1, 2)

    if enemy_choice == 1 or turn == 1 or enemy.health == enemy.max_hp:
        
        if enemy.special_meter == 100:
            special_attack(enemy, player)
        attack(enemy, player)

    elif enemy_choice == 2:
        defending(enemy)
    
    

        