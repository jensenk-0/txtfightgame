# makes classes of player and enemy and stores calculations for game
import random, math

class Entity:
    def __init__(self, health, attack, defense, special_meter, name, max_hp):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special_meter = special_meter
        self.name = name
        self.max_hp = max_hp
        self.defending = False
    
class Player(Entity):
    def __init__(self, health, attack, defense, special_meter, name, max_hp):
        super().__init__(health, attack, defense, special_meter, name, max_hp)

class Mage(Player):
    def __init__(self, health, attack, defense, special_meter, name, max_hp):
        super().__init__(health, attack, defense, special_meter, name, max_hp)
        self.ability = "magic attack"

class Tank(Player):
    def __init__(self, health, attack, defense, special_meter, name, max_hp):
        super().__init__(health, attack, defense, special_meter, name, max_hp)
        self.ability = "healing aura"

class Rogue(Player):
    def __init__(self, health, attack, defense, special_meter, name, max_hp):
        super().__init__(health, attack, defense, special_meter, name, max_hp)
        self.ability = "drain"


class Enemy(Entity):
    def __init__(self, health, attack, defense, special_meter, name, max_hp):
        super().__init__(health, attack, defense, special_meter, name, max_hp)









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
    print(f"{defender.name} protected itself!\n")
    
def def_reset(defender):
    if defender.defending:
        defender.defending = False



def special(attacker, defender, damage):
    percent_attacker = math.ceil((damage / attacker.max_hp) * 100)
    percent_defender = math.ceil((damage / defender.max_hp) * 100)

    

    attacker.special_meter += percent_attacker
    defender.special_meter += percent_defender


    if attacker.special_meter > 100:
        attacker.special_meter = 100

    if defender.special_meter > 100:
        defender.special_meter = 100

def special_attack(attacker, defender):

    print(f"{attacker.name} used special attack!\n")
    
    if defender.defending:
        print(f"{defender.name} was defending!, damage reduced")
        special_dmg = attacker.attack - random.randint(1, defender.defense) 
    else:
        special_dmg = attacker.attack

    if special_dmg < 0:
        special_dmg = 0

    print(f"{defender.name} took {special_dmg} damage from {attacker.name} attack!")
    defender.health -= special_dmg
    
    attacker.special_meter = 0

    return special_dmg

def ability(attacker, defender):
    if attacker.special_meter < 100:
        raise Exception("not enough power")
    
    print(f"{attacker.name} used {attacker.ability}")

    if attacker.ability == "magic attack":
        special_attack(attacker, defender)

    elif attacker.ability == "healing aura":
        amount_healed = attacker.max_hp // 2
        attacker.defending = True
        attacker.health += amount_healed
        print(f"{attacker.name} healed {amount_healed}!\n")
        

    elif attacker.ability == "drain":
        drained = attack(attacker, defender)
        attacker.health += drained
        defender.special_meter //= 2
        print(f"{attacker.name} healed {drained}\n{defender.name} special meter went down!")

    attacker.special_meter = 0

        
        



    



    




        
