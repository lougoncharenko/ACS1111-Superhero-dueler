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
        if random_number == 0:
            winner = self.name
            loser = opponent.name
        elif random_number == 1:
            winner = opponent.name
            loser = self.name
        print (f"{winner} defeats {loser}!")
        return winner

    
    def add_ability(self,ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
        return: total_damage:Int
        '''
        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self, incoming_damage):
        pass

    def take_damage(self, damage):
        pass

    def is_alive(self):
        pass

if __name__ == "__main__":
    wonder_woman = Hero('Wonder Woman', 200)
    hulk = Hero('Hulk', 200)
    wonder_woman.fight(hulk)
    ability = Ability("Great Debugging", 50)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    print(hero.attack())

    