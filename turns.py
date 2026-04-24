# holds player and enemy inputs and stats and holds the functions of player and enemy turns
import random
from classes import Mage, Tank, Rogue, Enemy, attack, defending, special_attack, def_reset, ability


#classes

mage = Mage(10, 15, 5, 0.0, "mage", 10)
rogue = Rogue(15, 10, 10, 0.0, "rogue", 15)
tank = Tank(20, 5, 15, 0.0, "tank", 20)
    
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
        return Enemy(10, 5, 5, 0.0, "grunt", 10)
    elif player_choice == "normal":
        return Enemy(15, 10, 10, 0.0, "evil knight", 15)
    elif player_choice == "hard":
        return Enemy(20, 15, 15, 0.0, "warmonger", 20)
    elif player_choice == "boss fight":
        return Enemy(50, 10, 10, 100.0, "boss", 50)
    else:
        raise Exception("invalid input")

enemy = difficulty()

def player_turn(turn):
    
    def_reset(player)

    player_input = input(f"\nturn {turn}\n{player.name} has {player.health} health left and {enemy.name} has {enemy.health} health left\n\nspecial meter at {player.special_meter}%\n\nwhat do you do?\n\nattack\n\ndefend\n\nability\n\nsurrender\n\n: ")
    
    if player_input == "attack":
        attack(player, enemy)
        
    elif player_input == "defend":
        defending(player)

    elif player_input == "ability":
        ability(player, enemy)
        
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
        else:
            attack(enemy, player)

    elif enemy_choice == 2:
        defending(enemy)
    
    

        