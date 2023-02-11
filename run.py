import random
from termcolor import colored

player = []
opponent = []
player_guesses = []


# This creates a 2-dimentional list that represent the game board or field as
# I call it. The loop runs 5 times and appends a row of 5 "X" to the "field"
# list, creating a 5x5 game field.
# filled with "X"s
def battle_ground():
    field = []
    for i in range(5):
        row = [" X "] * 5
        field.append(row)
    return field
    

# This function print the battlefield takes a 2-dimenstional list "field" as
# an argument and prints it to the console. The for loop runs over each row in
# "field" and "join" the elements in the row into a string separated with
# spaces in between and display a visual representation of the
# game battlefield.
def print_battle(field):
    for row in field:
        print(" ".join(colored(col, 'blue') if col == " X " else
              colored(col, 'red') if col == " * " else
              colored(col, 'green') if col == " # " else col for col in row))

# This randomly places 4 ships on the game field, represented by the "field"
# argument. The while loop continues to run until 4 ships have been placed in
# the field. A ship is placed at a random location on the field using using the
# generate_random_number function to determine the row and column indices.
# The "field[row][col]" assignment changes the value of the cell at that
# location to " O ", representing a ship. Finally, the for loop counts the
# number of ships on the field by counting the number of occurences of " O "
# ineach row, and the result is stored in the variable "number_of_ships".
def generate_random_number(field):
    return random.randint(0, 4)


# The game starts, with instructions and the player is prompted to insert
# his/her name.
def start():
    print("########## Greetings! You are now ready to play Battleships\
    against the computer. ##########")
    player_name = input("Please enter your player name and press enter: \n")
    print(f"\nHello {player_name}! Your battleship locations will be\
    automatically generated.\
        \nYour task is to locate the 4 battleships on the opponent's field.")
    print("\nIn the game field, 'X' represents empty locations, '*' represents\
    missed shots, and '#' represents hits. Please note that the game grid is\
    \n5 cells wide, and the integers used for targeting are between 1 and 5.")