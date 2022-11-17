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
    starting_health = input("Starting health: ")
    hero = Hero(hero_name, starting_health)
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

  def build_team_one(self):
    '''Prompt the user to build team_one '''
    numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
    for i in range(numOfTeamMembers):
      hero = self.create_hero()
      self.team_one.append(hero)

  def build_team_two(self):
    '''Prompt the user to build team_two'''
    numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
    for i in range(numOfTeamMembers):
      hero = self.create_hero()
      self.team_one.append(hero)

  def team_battle(self):
    '''Battle team_one and team_two together.'''
    for hero in self.team_one:
        for opponent in self.team_two:
            hero.fight(opponent)

  def show_stats(self):
    '''Prints team statistics to terminal.'''
    print("\n")
    print(self.team_one.name + " statistics: ")
    self.team_one.stats()
    print("\n")
    print(self.team_two.name + " statistics: ")
    self.team_two.stats()
    print("\n")

    team_one_kills = 0
    team_one_deaths = 0
    for hero in self.team_one.heroes:
        team_one_kills += hero.kills
        team_one_deaths += hero.deaths
    if team_one_deaths == 0:
        team_one_deaths = 1
    print(self.team_one.name + " average K/D was: " + str(team_one_kills/team_one_deaths))
    team_two_kills = 0
    team_two_deaths = 0
    for hero in self.team_one.heroes:
        team_two_kills += hero.kills
        team_two_deaths += hero.deaths
    if team_two_deaths == 0:
        team_two_deaths = 1
    print(self.team_one.name + " average K/D was: " + str(team_two_kills/team_two_deaths))

    for hero in self.team_one.heroes:
        if hero.deaths == 0:
            print("survived from " + self.team_one.name + ": " + hero.name)

    for hero in self.team_two.heroes:
        if hero.deaths == 0:
            print("survived from " + self.team_two.name + ": " + hero.name)


if __name__ == "__main__":
    game_is_running = True
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")
        if play_again.lower() == "n":
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()