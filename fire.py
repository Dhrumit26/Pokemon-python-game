from pokemon import Pokemon
import random

class Fire(Pokemon):
    def __init__(self, name):
        super().__init__(name, 0)
        
    def get_special_menu(self): #It has a get_special_menu method that returns a string with the options for special moves
        return "1. Ember\n2. Fire Blast"
    
    def _special_move(self, opponent, move): #It has a _special_move method that takes an opponent and a move parameter and calls the corresponding method based on the move selected
        if move == 1:
            return self._ember(opponent)
        elif move == 2:
            return self._fire_blast(opponent)
    
    def _ember(self, opponent):
        '''It has an _ember method that takes an opponent, generates a random damage between 1 and 5, 
        calculates the effectiveness of the move based on the battle table defined in the Pokemon class, 
        takes the total damage by multiplying the random damage with effectiveness, and updates the opponent's 
        health by calling the _take_damage method of the Pokemon class. It returns a string with the details 
        of the move and the total damage caused.'''
        damage = random.randint(1, 5)
        effectiveness = Pokemon._battle_table[self._type][opponent._type]
        total_damage = int(damage * effectiveness)
        opponent._take_damage(total_damage)
        return f"{self._name} used Flamethrower! {opponent._name} took {total_damage} damage.\nIt was SUPER EFFECTIVE! ",total_damage
    
    def _fire_blast(self, opponent):
        '''It has a _fire_blast method that takes an opponent, generates a random damage between 3 and 4, 
        calculates the effectiveness of the move based on the battle table defined in the Pokemon class, 
        takes the total damage by multiplying the random damage with effectiveness, and updates the opponent's 
        health by calling the _take_damage method of the Pokemon class. It returns a string with the details of 
        the move and the total damage caused.'''
        damage = random.randint(3, 4)
        effectiveness = Pokemon._battle_table[self._type][opponent._type]
        total_damage = int(damage * effectiveness)
        opponent._take_damage(total_damage)
        return f"{self._name} used Fire Punch! {opponent._name} took {total_damage} damage.\nIt was SUPER EFFECTIVE! ",total_damage





