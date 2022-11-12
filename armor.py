import random

class Armor:
    def __init__(self, name, max_block) -> None:
        """
        Takes in name: String, max_block: Integer as parameters
        """
        self.name = name
        self.max_block = max_block

    def block(self):
        """
        Return a block value that is randomly generated between 0 and max_damage. 
        """
        block_value = random.randint(0, self.max_block)
        return block_value


if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  armor = Armor("Debugging Shield", 10)
  print(armor.name)
  print(armor.block())