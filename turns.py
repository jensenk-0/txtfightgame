# holds player and enemy inputs and stats
import random
from classes import Player, Enemy


player = Player(10, 10, 5, 5)
enemy = Enemy(10, 10, 5, 5)

def player_turn(turn):
    player_input = input(f"turn {turn}\nplayer has {player.health} left\nenemy has {enemy.health} health left, what do you do?\nattack\nsurrender\n")
    if player_input == "attack":
        dmg = dmg_cal(player, enemy)
        enemy.health -= dmg
        print(f"you did {dmg} damage to enemy")

    elif player_input == "surrender":
        player.health = 0
    
    else:
        raise Exception("Invalid choice")
        



def enemy_turn():
    print("enemy attacks!")
    dmg = dmg_cal(enemy, player)
    player.health -= dmg
    print(f"enemy did {dmg} damage to player")
        

def dmg_cal(attacker, defender):
    dmg = random.randint(1, attacker.attack) - random.randint(1, defender.defense)

    if dmg < 0:
        dmg = 0

    return dmg