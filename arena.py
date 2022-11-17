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