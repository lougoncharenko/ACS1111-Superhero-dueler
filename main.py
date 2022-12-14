from ability import Ability
from armor import Armor
from hero import Hero


def battle_arena():
    """
    a while loop that keeps fight until one player returns false for is_alive
    """
    pass

if __name__ == "__main__":

    # wonder woman
    captain_america = Hero('Captain America', 200)
    agility = Ability("Agility", 50)
    captain_america.add_ability(agility)
    shield = Armor("Captain America Sheild", 10)
    captain_america.add_armor(shield)

    # Hulk
    hulk = Hero('Hulk', 200)
    hulk_smash=Ability('Hulk Smash', 50)
    hulk.add_ability(hulk_smash)
    mutated_skin = Armor('Mutated Skin', 10)
    hulk.add_armor(mutated_skin)

    # fight
    captain_america.fight(hulk)

    #second test
    hero1 = Hero("Wonder Woman", 200)
    hero2 = Hero("Dumbledore", 200)
    ability1 = Ability("Super Speed", 10)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)


