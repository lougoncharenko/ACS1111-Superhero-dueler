import random
from ability import Ability
from armor import Armor

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
    
    def fight(self, opponent):
        """
        The fight() method will take an opponent as a parameter. An opponent is another instance of Hero.
        """
        random_number = random.randint(0,1)
        print(type (random_number))
        winner = ''
        loser = ''
        if bool(self.abilities) or bool(opponent.abilities):
            print('draw')
        else:
            print('fight')
        # if random_number == 0:
        #     winner = self.name
        #     loser = opponent.name
        # elif random_number == 1:
        #     winner = opponent.name
        #     loser = self.name
        # print (f"{winner} defeats {loser}!")
        return winner

    
    def add_ability(self,ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def attack(self):
        '''
        Calculate the total damage from all ability attacks.
        return: total_damage:Int
        '''
        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        '''
        Add armor to self.armors
        Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self):
        total_defense = 0

        for armor in self.armors:
            total_defense += armor.block()
        return total_defense

    def take_damage(self, damage):
        '''
        Updates self.current_health to reflect the damage minus the defense.
        '''
        damage -= self.defend()
        print(f"damage points is {damage}")
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
    # ability = Ability("Great Debugging", 50)
    hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # print(hero.attack())
    print(hero.current_health)
    armor = Armor("Debugging Shield", 10)
    hero.add_armor(armor)
    hero.take_damage(50)
    print(hero.current_health)
   


    