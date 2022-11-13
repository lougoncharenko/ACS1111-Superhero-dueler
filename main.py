from ability import Ability
from hero import Hero

if __name__ == "__main__":
    wonder_woman = Hero('Wonder Woman', 200)
    hulk = Hero('Hulk', 200)
    wonder_woman.fight(hulk)
    ability = Ability("Great Debugging", 50)
    wonder_woman.add_ability(ability)
    print(wonder_woman.attack())