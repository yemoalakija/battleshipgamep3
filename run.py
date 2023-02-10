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
