# makes classes of player and enemy and stores calculations for game
import random, math

class Player:
    def __init__(self, health, attack, defense, defending, special_meter, max_hp):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.defending = defending
        self.special_meter = special_meter
        self.max_hp = max_hp
        self.name = "player"

    
class Enemy:
    def __init__(self, health, attack, defense, defending, special_meter, max_hp):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.defending = defending
        self.special_meter = special_meter
        self.max_hp = max_hp
        self.name = "enemy"


def attack(attacker, defender):
    dmg = random.randint(1, attacker.attack) - random.randint(1, defender.defense)

    if dmg < 0:
        dmg = 0
    
    defender.health -= dmg

    print(f"{attacker.name} attacks\n")

    print(f"{attacker.name} did {dmg} to {defender.name}\n")
    
    special(attacker, defender, dmg)

    return dmg


def defending(defender):
    defender.defense *= 2
    defender.defending = True
    print(f"{defender.name} protected itself, defense doubled!\n")


def special(attacker, defender, damage):
    percent_attacker = (damage / attacker.max_hp) * 100
    percent_defender = (damage / defender.max_hp) * 100

    attacker.special_meter += percent_attacker
    defender.special_meter += percent_defender


    if attacker.special_meter > 100:
        attacker.special_meter = 100

    if defender.special_meter > 100:
        defender.special_meter = 100

def heal(healer):
        
    percent = healer.special_meter / 100
    healed = (healer.max_hp * percent) // 2
    
    healer.special_meter = 0

    healer.health += math.floor(healed)

    if healer.health > healer.max_hp:
        healer.health = healer.max_hp

    print(f"{healer.name} healed himself {healed}")
    
    




        
