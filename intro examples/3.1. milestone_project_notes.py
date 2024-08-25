## Validating user input 

def user_choice(): 

    choice = 'WRONG'
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number between 1 and 10: ")

        if choice.isdigit() == False:
            print("Invalid type! Please enter a number.")
        if choice.isdigit() == True:
            if int(choice) in range(0,10):
                within_range = True
            else:  
                within_range = False
                print("Invalid range! Please enter a number between 1 and 10.")

    return int(choice)

user_choice()


## A user can choose a "position" in an existing list and replace it with a value of their choice.

# game_list = [0,1,2]

def display_game(game_list):
    print("Here is the current state of the game:")
    print(game_list)

#display_game(game_list)

def position_choice():
    choice = 'WRONG'

    while choice not in ['0', '1', '2']:
        choice = input("Please choose a position (0, 1, or 2): ")

        if choice not in ['0', '1', '2']:
            print("Invalid choice. Please try again.")
    	
    return int(choice)

position_choice()

def replacement_choice(game_list,position):
    
    user_placement = input("Type a string to place at the position: ")
    
    game_list[position] = user_placement
    
    return game_list


def gameon_choice():
    
    choice = 'wrong'
    
    while choice not in ['Y','N']:
        choice = input("Would you like to keep playing? Y or N: ")
        if choice not in ['Y','N']:
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")
            
    # Optionally you can clear everything after running the function
    # clear_output()
    
    if choice == "Y":
        return True
    else:
        return False
    

# Variable to keep game playing
game_on = True

# First Game List
game_list = [0,1,2]



while game_on:
    
    display_game(game_list)
    
    position = position_choice()
    
    game_list = replacement_choice(game_list,position)
    
    display_game(game_list)
    
    game_on = gameon_choice()