# holds player and enemy inputs and stats
import random
from classes import Player, Enemy


player = Player(10, 10, 5, 5)
enemy = Enemy(10, 10, 5, 5)

def player_turn(turn):
    player_input = input(f"turn {turn}\nplayer has {player.health} left\nenemy has {enemy.health} health left, what do you do?\nattack\nsurrender\n")
    if player_input == "attack":
        dmg = random.randint(1, player.attack) - random.randint(1, enemy.defense)
        enemy.health -= dmg
        if dmg < 0:
            dmg = 0
        print(f"you did {dmg} damage to enemy")
    elif player_input == "surrender":
        player.health = 0
    
    else:
        print("error: invalid choice")


def enemy_turn():
    print("enemy attacks!")
    dmg = random.randint(1, enemy.attack) - random.randint(1, player.defense)
    if dmg < 0:
        dmg = 0
    player.health -= dmg
    print(f"enemy did {dmg} damage to player")
        

