'''
Dhrumit Mukeshbhai Savaliya
Rafa Gabriel Adrid

Dhrumit - I completed main.py / fire.py / grass.py / water.py
Rafa Gabriel Adrid - I completed pokemon.py
'''


import random
from pokemon import Pokemon
from water import Water
from fire import Fire
from grass import Grass

def gym_attack(gym_pokemon,gym_pokemon_type,pokemon):
    '''The code also uses a random module to simulate the gym Pokemon's attacks and moves.'''
    # Choose random attack type (normal or special) for the gym Pokemon
    gym_choice_attack = random.randint(1,2)
    gym_choice_mov = random.randint(1,2)
    # If gym Pokemon chooses normal attack type, randomly select a normal move for the gym Pokemon
    if gym_choice_attack == 1:
        gym_choice_mov = random.randint(1,2)
        if gym_choice_mov == 1:
            mov_opp,dmg_opp = gym_pokemon.attack(pokemon,"normal","slam")
        elif gym_choice_mov == 2:
            mov_opp,dmg_opp = gym_pokemon.attack(pokemon,"normal","tackle") 
    # If gym Pokemon chooses special attack type, randomly select a special move for the gym Pokemon       
    elif gym_choice_attack == 2:
        if gym_choice_mov == 1:
            mov_opp,dmg_opp = gym_pokemon_type._special_move(pokemon,1)
        elif gym_choice_mov == 2:
            mov_opp,dmg_opp = gym_pokemon_type._special_move(pokemon,2)
    return mov_opp,dmg_opp      

def main():
    # Prompt user to choose a pokemon for the battle
    print ("PROF OAK:  Hello Trainer!\nToday you're off to fight your first gym battle of 1 vs. 3 GRASS pokemon.\nSelect the pokemon that you will fight with. ")
    print("1. I choose you, Charmander. \n2. Squirtle!  GO! \n3. We can do it, Bulbasaur!")
    # Assign the chosen pokemon and corresponding Pokemon class instance to variables
    user = input("Please choose a pokemon: ")
    while user not in ['1','2','3']:
        print("Invalid Input")
        user = input("Please choose a pokemon: ")

    if user == '1':
        user_pokemon = Fire("Charmander")
        pokemon = Pokemon("Charmander",0)
    elif user == '2':
        user_pokemon = Water("Squirtle")
        pokemon = Pokemon("Squirtle",1)
    elif user == '3':
        user_pokemon = Grass("Bulbasaur")
        pokemon = Pokemon("Bulbasaur",2)
    else:
        print("Invalid Input")
    # Set the initial health points of user's pokemon and the first gym pokemon
    user_pokemon_hp = int(pokemon._hp)
    print("  -- GYM BATTLE -- ")
    # Create a list of gym pokemon to fight against
    gym_grass_pokemom = ["Oddish","Bellsprout","Chikorita"]
    # Iterate through each gym pokemon in the list
    for i in range(len(gym_grass_pokemom)):
        poke = gym_grass_pokemom[i]
        # Assign the current gym pokemon and corresponding Grass class instance to variables
        gym_pokemon_type = Grass(poke)
        gym_pokemon = Pokemon(poke,2)
        gym_pokemon_hp = gym_pokemon._hp
        bool = True
        # Loop until either the user's pokemon or the current gym pokemon's health points reach zero
        while gym_pokemon_hp > 0 and user_pokemon_hp > 0:
            print()
            # Prompt the user to choose an attack type for their 
            print("GYM LEADER: I choose you:")
            #It prints the name and HP of both Pokemon before the battle starts
            print(f"{gym_pokemon._name} HP: {gym_pokemon_hp}/25")
            print()
            print(f'{pokemon._name} HP: {user_pokemon_hp}/25')
            #Then it prompts the user to choose an attack type: Normal or Special
            print("Choose an Attack Type: \n1. Normal \n2. Special ")
            user_attack = input("Enter attack type: ")
            while user_attack not in ['1','2']:
                print("Invalid Input")
                user_attack = input("Enter attack type: ")
            #This code block starts the battle between the user's selected Pokemon and the Gym Leader's Pokemon
            if user_attack == '1': 
                print("Choose a Move: ")
                print(pokemon.get_normal_menu())
                move = input("Enter move: ")
                while move not in ['1','2']:
                    print("Invalid Input")
                    move = input("Enter move: ")
                #If the user selects Normal attack, it prints the available Normal moves and prompts the user to choose a move
                if move == '1':
                    mov,dmg = pokemon.attack(gym_pokemon,"normal","slam")
                    print(mov)
                    gym_pokemon_hp -= int(dmg)
                    gym_move,poke_dmg = gym_attack(gym_pokemon,gym_pokemon_type,pokemon)
                    print(gym_move)
                    user_pokemon_hp -= poke_dmg
                #If the user selects Special attack, it prints the available Special moves and prompts the user to choose a move
                if move == '2':
                    mov,dmg = pokemon.attack(gym_pokemon,"normal","tackle")
                    print(mov)
                    gym_pokemon_hp -= int(dmg)
                #If the user selects Special attack, it prints the available Special moves and prompts the user to choose a move
                    gym_move,poke_dmg = gym_attack(gym_pokemon,gym_pokemon_type,pokemon)
                    print(gym_move)
                    user_pokemon_hp -= poke_dmg
            elif user_attack == '2':
                print("Choose a Move: ")
                print(user_pokemon.get_special_menu())
                sp_move = input("Enter move: ")
                while sp_move not in ['1','2']:
                    print("Invalid Input")
                    sp_move = input("Enter move: ")
                if sp_move == '1':
                    sp_mov,sp_dmg = user_pokemon._special_move(gym_pokemon,1)
                    print(sp_mov)
                    gym_pokemon_hp -= int(sp_dmg)
                    gym_move,poke_dmg = gym_attack(gym_pokemon,gym_pokemon_type,pokemon)
                    print(gym_move)
                    user_pokemon_hp -= poke_dmg
                elif sp_move == '2':
                    sp_mov,sp_dmg = user_pokemon._special_move(gym_pokemon,2)
                    print(sp_mov)
                    gym_pokemon_hp -= int(sp_dmg)
                    gym_move,poke_dmg = gym_attack(gym_pokemon,gym_pokemon_type,pokemon)
                    print(gym_move)
                    user_pokemon_hp -= poke_dmg
            
            if user_pokemon_hp <= 0:
                #If the user's Pokemon HP reaches 0, the game ends and the user loses
                print()
                print(f"YOU LOSS! {gym_pokemon._name} defeat {user_pokemon._name} !!!!!!!!!!")
                break
                
            if gym_pokemon_hp <= 0:
                #If the Gym Leader's Pokemon HP reaches 0, the game ends and the user wins.
                print()
                print(f"YOU WON!  You defeated {gym_pokemon._name} !!!!!!!! ") 
                 




main()