import random
class Ability:
    def __init__(self, name, max_damage) -> None:
        """
        Takes in name: String, max_damage: Integer as parameters
        """
        self.name = name
        self. max_damage = max_damage

    def attack(self):
        """
        Return a attack value that is randomly generated between 0 and max_damage. 
        """
        attack_value = random.randint(0, self.max_damage)
        return attack_value



if __name__ == "__main__":
    ability = Ability("Testing Ability", 20)
    print(ability.name)
    print(ability.attack())