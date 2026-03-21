# makes classes of player and enemy and stores calculations for game
import random

class Player:
    def __init__(self, health, attack, defense, defending, special_meter):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.defending = defending
        self.special_meter = special_meter

    
class Enemy:
    def __init__(self, health, attack, defense, defending, special_meter):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.defending = defending
        self.special_meter = special_meter


def dmg_cal(attacker, defender):
    dmg = random.randint(1, attacker.attack) - random.randint(1, defender.defense)

    if dmg < 0:
        dmg = 0

    return dmg


def defending(defender):
    defender.defense *= 2
    defender.defending = True


        
