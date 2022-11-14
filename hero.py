import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health):
        '''
        Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
        '''
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
    
    def fight(self, opponent):
        """
        The fight() method will take an opponent as a parameter. An opponent is another instance of Hero.
        """
        random_number = random.randint(0,1)
        print(type (random_number))
        winner = ''
        loser = ''
        if bool(self.abilities) == False and bool(opponent.abilities) == False:
            print('draw')
        else:
            while self.is_alive() == True and opponent.is_alive() ==True:
                opponent_damage = self.attack()
                opponent.take_damage(opponent.name, opponent_damage)
                self_damage = opponent.attack()
                self.take_damage(self.name, self_damage)
                if self.current_health > opponent.current_health:
                    winner = self.name
                    loser = opponent.name
                else:
                    winner = opponent.name
                    loser = self.name
                self.is_alive()
                opponent.is_alive()
            print(f'{winner} beats {loser}')
            return winner 
            

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def add_armor(self, armor):
        '''
        Add armor to self.armors
        Armor: Armor Object
        '''
        self.armors.append(armor)

    def add_weapon(self, weapon):
        ''' 
        Add weapon to self.abilities
        '''
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths

    def attack(self):
        '''
        Calculate the total damage from all ability attacks.
        return: total_damage:Int
        '''
        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage


    def defend(self):
        total_defense = 0

        for armor in self.armors:
            total_defense += armor.block()
        return total_defense

    def take_damage(self, name, damage):
        '''
        Updates self.current_health to reflect the damage minus the defense.
        '''
        damage -= self.defend()
        self.current_health -= damage

    def is_alive(self):
        '''
        Return True or False depending on whether the hero is alive or not.
        '''
        if self.current_health <= 0:
            return False
        else:
            return True
        

if __name__ == "__main__":
    hero = Hero("Wonder Woman", 200)
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
   


    