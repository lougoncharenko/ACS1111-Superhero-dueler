from ability import Ability
from armor import Armor
from hero import Hero

if __name__ == "__main__":
    wonder_woman = Hero('Wonder Woman', 200)
    hulk = Hero('Hulk', 200)
    wonder_woman.fight(hulk)
    ability = Ability("Great Debugging", 50)
    wonder_woman.add_ability(ability)
    print(wonder_woman.attack())
    armor = Armor("Debugging Shield", 10)
    wonder_woman.add_armor(armor)
    print(wonder_woman.defend())
