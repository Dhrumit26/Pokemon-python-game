from pokemon import Pokemon
import random

class Water(Pokemon):
    def __init__(self, name):
        super().__init__(name, 1)
        
    def get_special_menu(self): #It has a get_special_menu method that returns a string with the options for special moves
        return "1. Water Gun\n2. Bubble Beam"
    
    def _special_move(self, opponent, move): #It has a _special_move method that takes an opponent and a move parameter and calls the corresponding method based on the move selected
        if move == 1:
            return self._water_gun(opponent)
        elif move == 2:
            return self._bubble_beam(opponent)
    
    def _water_gun(self, opponent):
        '''It has a _water_gun method that takes an opponent, generates a random damage between 1 and 6, 
        calculates the effectiveness of the move based on the battle table defined in the Pokemon class, 
        takes the total damage by multiplying the random damage with effectiveness, and updates the 
        opponent's health by calling the _take_damage method of the Pokemon class. It returns a string 
        with the details of the move and the total damage caused.'''
        damage = random.randint(1, 6)
        effectiveness = Pokemon._battle_table[self._type][opponent._type]
        total_damage = int(damage * effectiveness)
        opponent._take_damage(total_damage)
        return f"{self._name} used Water Gun! {opponent._name} took {total_damage} damage.\nIt was SUPER EFFECTIVE! ",total_damage
    
    def _bubble_beam(self, opponent):
        '''It has a _bubble_beam method that takes an opponent, generates a random damage between 3 and 4, 
        calculates the effectiveness of the move based on the battle table defined in the Pokemon class, 
        takes the total damage by multiplying the random damage with effectiveness, and updates the opponent's 
        health by calling the _take_damage method of the Pokemon class. It returns a string with the details 
        of the move and the total damage caused.'''
        damage = random.randint(3, 4)
        effectiveness = Pokemon._battle_table[self._type][opponent._type]
        total_damage = int(damage * effectiveness)
        opponent._take_damage(total_damage)
        return f"{self._name} used Bubble Beam! {opponent._name} took {total_damage} damage.\nIt was SUPER EFFECTIVE! ",total_damage