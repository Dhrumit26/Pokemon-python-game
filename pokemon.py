import random
'''from water import Water
from fire import Fire
from grass import Grass'''

class Pokemon:
    _battle_table = [[1, .5, 2], [2, 1, .5], [.5, 2, 1]] # This is a 2D list that represents the type matchup chart. The indices correspond to the attacker's type and the defender's type, and the values represent the effectiveness multiplier.

    def __init__(self, name, type):
        self._name = name  # Define the constructor method that initializes a new Pokemon instance.
        self._type = type # Set the Pokemon's name attribute.
        self._hp = 25 # Set the Pokemon's initial HP attribute.

    def hp(self):
        return self._hp  # Define a method that returns the Pokemon's current HP.

    def get_normal_menu(self): # Define a method that returns the normal moves available to the Pokemon.
        return "1. Slam\n2. Tackle"

    def _normal_move(self, opponent, move): # Define a method for the Pokemon's normal moves.
        if move == "slam":
            return self._slam(opponent)
        elif move == "tackle":
            return self._tackle(opponent)
        else:
            return ""

    def _slam(self, opponent):# Define a method for the Slam move.
        dmg = random.randint(1, 8)
        opponent_type = opponent._type
        multiplier = Pokemon._battle_table[self._type][opponent_type]
        total_dmg = int(dmg * multiplier)
        opponent._take_damage(total_dmg)
        # Return a string that describes the move and the amount of damage dealt, along with a message indicating whether the move was effective or not.
        return f"{self._name} uses Slam on {opponent._name}. It does {total_dmg} damage. Effective!" if multiplier == 2 else f"{self._name} uses Slam on {opponent._name}. It does {total_dmg} damage. \nIt was not very effective.",total_dmg

    def _tackle(self, opponent): # Define a method for the Tackle move.
        dmg = random.randint(3, 6)# Generate a random integer between 3 and 6 for the damage.
        opponent_type = opponent._type
        multiplier = Pokemon._battle_table[self._type][opponent_type]
        total_dmg = int(dmg * multiplier)# Calculate the total damage by multiplying the base damage by the effectiveness multiplier and rounding down to the nearest integer
        opponent._take_damage(total_dmg)
        return f"{self._name} uses Tackle on {opponent._name}. It does {total_dmg} damage. Effective!" if multiplier == 2 else f"{self._name} uses Tackle on {opponent._name}. It does {total_dmg} damage. \nIt was not very effective.",total_dmg

    def get_special_menu(self):
        pass
        

    def _special_move(self, opponent, move):
        pass

    def attack(self, opponent, move_type, move): #This method represents the attack of the Pokemon on its opponent.
        #It takes in the opponent object, the move_type, and the move as arguments.
        if move_type == "normal": 
        #If the move_type is "normal", it calls the _normal_move method with the opponent and move as arguments and returns the output.
            return self._normal_move(opponent, move) 
        elif move_type == "special":
        #If the move_type is "special", it calls the _special_move method with the opponent and move as arguments and returns the output.
            return self._special_move(opponent, move)
        else:
            return ""

    def __str__(self):
        return f"{self._name}: {self._hp}/25"

    def _take_damage(self, dmg):
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0
