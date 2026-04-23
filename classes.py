# makes classes of player and enemy and stores calculations for game
import random, math

class Player:
    def __init__(self, health, attack, defense, special_meter, max_hp):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special_meter = special_meter
        self.max_hp = max_hp
        self.name = "player"
        self.defending = False
    
class Enemy:
    def __init__(self, health, attack, defense, special_meter, max_hp):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special_meter = special_meter
        self.max_hp = max_hp
        self.name = "enemy"
        self.defending = False

def attack(attacker, defender):
    
    print(f"{attacker.name} attacks\n")
    
    if defender.defending:
        print(f"{defender.name} was defending!, damage reduced")
        dmg = random.randint(1, attacker.attack) - random.randint(1, defender.defense)
    else:
        dmg = random.randint(1, attacker.attack)

    if dmg < 0:
        dmg = 0
    
    defender.health -= dmg

    print(f"{attacker.name} did {dmg} to {defender.name}\n")
    
    special(attacker, defender, dmg)

    return dmg


def defending(defender):
    defender.defending = True
    print(f"{defender.name} protected itself, defense doubled!\n")
    
def def_reset(defender):
    if defender.defending:
        defender.defending = False



def special(attacker, defender, damage):
    percent_attacker = (damage / attacker.max_hp) * 100
    percent_defender = (damage / defender.max_hp) * 100

    attacker.special_meter += percent_attacker
    defender.special_meter += percent_defender


    if attacker.special_meter > 100:
        attacker.special_meter = 100

    if defender.special_meter > 100:
        defender.special_meter = 100

def special_attack(attacker, defender):

    print(f"{attacker.name} used a special attack!\n")
    

    if attacker.special_meter < 100:
        raise Exception("not enough special power")
    
    if defender.defending:
        print(f"{defender.name} was defending!, damage reduced")
        special_dmg = attacker.attack - random.randint(1, defender.defense)
    
    else:
        special_dmg = attacker.attack

    if special_dmg < 0:
        special_dmg = 0

    print(f"{defender.name} took {special_dmg} damage from attack!")

    defender.health -= special_dmg

    attacker.special_meter = 0.0

    



    




        
