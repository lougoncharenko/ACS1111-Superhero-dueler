class Team ():
    """
    Team class does not inherit hero, rather contains Hero objects
    This concept is known as aggregation in OOP
    Initialize your team with its team name and an empty list of heroes
    """
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        '''
        Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
            else: 
                print(f'{name} does not exist on this team')
    
    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print(hero.name)