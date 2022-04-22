################################
# interface for the Pet object
# ----------
# it's up to you to finish it! 
# feel free to customize it as you please.
################################

# Creates a fancy menu system in the Terminal
from simple_term_menu import TerminalMenu

# Imports the Pet from pet.py
from pet import Pet  

def menu(options):
    "Presents an interactive Terminal menu and returns the user's choice"
    terminal_menu = TerminalMenu(options) #Creates the Terminal Menu 
    option_num = terminal_menu.show() #Get user selected Option 
    return options[option_num]

def pet_simulator():
    "Runs the pet simulator game"
    print("---- Welcome to Pet Simulator ----")
    print("What would you like to name your pet?")
    name = input(" > ")
    my_pet = Pet() #create the pet
    my_pet.set_name(name)
    print("Your pet is ready!")

    play = True
    while play == True:
        options = ["Introduce", "Quit"] #set the menu choices
        option = menu(options)
        if option == 'Introduce':
            my_pet.introduce()
        elif option == 'Quit':
            play = False

    print("--- Leaving Pet Simulator ---")

pet_simulator()
