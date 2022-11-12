from ability import Ability
from hero import Hero

if __name__ == "__main__":
    wonder_woman = Hero('Wonder Woman', 200)
    hulk = Hero('Hulk', 200)
    wonder_woman.fight(hulk)
    ability = Ability("Testing Ability", 20)
    print(ability.name)
    print(ability.attack())