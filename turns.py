# holds player and enemy inputs and stats
import random
from classes import Player, Enemy


player = Player(10, 10, 5, False, 0)
enemy = Enemy(10, 10, 5, False, 0)

def player_turn(turn):
    
    if player.defending:
        player.defense //= 2
        player.defending = False
        
    print(player.defense)
    player_input = input(f"turn {turn}\nplayer has {player.health} health left\nenemy has {enemy.health} health left, what do you do?\nattack\ndefend\nsurrender\n")
    
    if player_input == "attack":
        dmg = dmg_cal(player, enemy)
        enemy.health -= dmg
        print(f"you did {dmg} damage to enemy")
        

    elif player_input == "defend":
        print("player is defending, his defense doubled!")
        defending(player)
        print(player.defense)
        
        

    elif player_input == "surrender":
        player.health = 0
    
    else:
        raise Exception("Invalid choice")
        


enemy_max_hp = enemy.health

def enemy_turn():

    if enemy.defending:
        enemy.defense //= 2
        enemy.defending = False

    enemy_choice = random.randint(1, 2)

    if enemy_choice == 1 or enemy.health == enemy_max_hp:
        print("enemy attacks!")
        dmg = dmg_cal(enemy, player)
        player.health -= dmg
        print(f"enemy did {dmg} damage to player")
    
    elif enemy_choice == 2:
        defending(enemy)
        print("The enemy is defending, his defense doubled!")
        

def dmg_cal(attacker, defender):
    dmg = random.randint(1, attacker.attack) - random.randint(1, defender.defense)

    if dmg < 0:
        dmg = 0

    return dmg


def defending(defender):
    defender.defense *= 2
    defender.defending = True




