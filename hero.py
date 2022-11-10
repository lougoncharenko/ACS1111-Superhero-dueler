import random

class Hero:
    def __init__(self, name, starting_health):
        '''
        Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
    
    def fight(self, opponent):
        random_number = random.randint(0,1)
        print(type (random_number))
        winner = ''
        if random_number == 0:
            winner = self.name
        elif random_number == 1:
            winner = opponent
        print (f"{winner} wins!")
        return winner

       
        
        


if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    my_hero.fight()
    