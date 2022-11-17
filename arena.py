from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
  def __init__(self):
    '''Instantiate properties
        team_one: None
        team_two: None
    '''
    self.team_one = list()
    self.team_two = list()

  def create_ability(self):
    '''Prompt for Ability information.
      return Ability with values from user Input
    '''
    name = input("What is the ability name?  ")
    max_damage = int(input(
      "What is the max damage of the ability?  "))

    return Ability(name, max_damage)

  def create_weapon(self):
    '''Prompt user for Weapon information
        return Weapon with values from user input.
    '''
    weapon_name = input("What is the weapon name?  ")
    max_damage = int(input(
      "What is the max damage of the weapon  "))
    return Weapon(weapon_name, max_damage)

  def create_armor(self):
    '''Prompt user for Armor information
      return Armor with values from user input.
    '''
    armor_name = input("What is the name of the armor?  ")
    max_block = int(input("What is the max blockage the armor provides  "))

  def create_hero(self):
    '''Prompt user for Hero information
      return Hero with values from user input.
    '''
    hero_name = input("Hero's name: ")
    hero = Hero(hero_name)
    add_item = None
    while add_item != "4":
        add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
        if add_item == "1":
            ability= self.create_ability()
            hero.add_ability(ability)
        elif add_item == "2":
            weapon = self.create_weapon()
            hero.add_weapon(weapon)
        elif add_item == "3":
            armor = self.create_armor()
            hero.add_armor(armor)
    return hero