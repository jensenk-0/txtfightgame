import random
from classes import Player, Enemy


player = Player(10, 10, 5, 5)
enemy = Enemy(10, 10, 5, 5)


def main_game(turns):
    for turn in range(1, turns+1):
        player_input = input(f"turn {turn}\nenemy has {enemy.health} health left, what do you do?\n")
        if player_input == "attack":
            dmg = random.randint(1, player.attack) - random.randint(1, enemy.defense)
            enemy.health -= dmg
            print(f"you did {dmg} damage to enemy")

main_game(5)


