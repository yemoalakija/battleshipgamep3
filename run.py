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


# This function generates 3 game fields: "player", "opponent" whicih is the
# computer, and "player_guesses"; and places ships on the "player" and
# "oppponent" fields. The function calls the "create_field" function to create
# the game field, and the "place_ships" function to randomly place ships on the
# field.
def create_fields():
    global player, opponent, player_guesses
    player = battle_ground()
    opponent = battle_ground()
    player_guesses = battle_ground()
    for i in range(4):
        generate_random_number(player)


# This function prompts the user to guess a location on the opponent's field
# to attack. The location is specified by a column and a row, which are first
# validated for correctness, then converted into zero-indexed values. If the
# user already fired at that location, the function will ask them to choose
# another location. If the guess is a hit, the function will print a message
# to celebrate the success, otherwise it will print a message to show the miss.
def player_guess():
    print("This is the opponent's field: ")
    print_battle(player_guesses)
    repeat = True
    # check if the data is valid
    while repeat:
        col = input("Enter the column you'd like to fire at (1-5): \n")
        if not check_valid_input(col):
            continue
        row = input("Enter the row you'd like to fire at (1-5): \n")
        if not check_valid_input(row):
            continue
        # one is minus as the players enter between 1 to 5.
        guess_col = int(col) - 1
        guess_row = int(row) - 1
        # This check if the spot has been chosen before.
        if player_guesses[guess_row][guess_col] in [" * ", " # "]:
            print("You already fired at that location.😕 Try again.")
        else:
            repeat = False
        # This checks if the spot is a hit or not and show result.
    if opponent[guess_row][guess_col] == " O ":
        player_guesses[guess_row][guess_col] = " # "
        print("\nCongratulations! You hit a ship! 🥳")
    else:
        player_guesses[guess_row][guess_col] = " * "
        print("\nOops! You missed.☹️")


# With this function, the opponent generates random coordinates to make a guess
# at the player's field. It generates two random numbers, guess_col and
# guess_row, which will be used as the coordinates for the computer's guess.
# The function random_num(comp) is used to generate these numbers. The code
# enters a while loop that will repeat as long as the repeat flag is True.
# Inside the loop, the code checks if the element in the user's board at the
# guessed coordinates (user[guess_row][guess_col]) is equal to either " * " or
# " # ". If that's the case, it generates new random coordinates and goes back
# to step. If the element in the user's board is not equal to either " * " or
# " # ", the repeat flag is set to False and the loop is exited. The code
# prints the coordinates that the computer has chosen. The code then checks
# if the element in the user's board at the chosen coordinates is equal to "o".
# If it is, it changes the element to " # " to indicate a hit and prints a
# message. If the element in the user's board is not equal to " o ", it changes
# the element to " * " to indicate a miss and prints a message.
def opponent_guess():
    print("\n\nOpponent's turn now.")
    repeat = True
    while repeat:
        # This checks if the spot had been chosen before.
        guess_col = random.randint(0, 4)
        guess_row = random.randint(0, 4)
        if player[guess_row][guess_col] in (" * ", " # "):
            guess_col = generate_random_number(opponent)
            guess_row = generate_random_number(opponent)
        else:
            repeat = False
    # This function shows the player what the opponent chose with result.
    print(f"The opponent chose {guess_col + 1}, {guess_row + 1}")
    if player[guess_row][guess_col] == " O ":
        player[guess_row][guess_col] = " # "
        print("A hit! ☹️")
    else:
        player[guess_row][guess_col] = " * "
        print("It's a missed! YAY! 😀")


# The play_game function sets up the game by calling two functions:
# create_fields and start. The create_fields function creates the grids that
# represent the player's field and the opponent's field, while the start
# function displays a message to welcome the player. The game loop begins with
# the turn count set to 0 and continues for 10 turns or until one player has
# successfully hit all of the other player's ships (indicated by 4 successful
# hits). On each turn, the player (user) makes a guess by calling the
# player_guess function, which allows them to select a square on the computer's
# field to attack. The field displaying the player's guesses is then printed
# with the create_field function. The computer makes its guess by calling the
# opponent_guess function, which randomly selects a square on the player's
# field to attack. The player's field is then created, and the loop continues
# for 10 turns or until one player has 4 successful hits.
def play_game():
    create_fields()
    start()
    turn = 0
    while turn < 10:
        print(f"\nTurn {turn +1}/10 \n")
        player_guess()
        print_battle(player_guesses)
        input("\nPress Enter to continue...")
        opponent_guess()
        print("\nYour field: ")
        print_battle(player)
        input("\nPress Enter to continue...")
        turn += 1
        if count_hits(player) == 4 or count_hits(player_guesses) == 4:
            turn = 10
    winner_check_final()


# The check_valid_input function takes in a user input value and checks if it's
# within the range of 1 to 5 (inclusive).If the value is outside of this range,
# the function raises a ValueError with a message, "Invalid input! Choose a
# number between 1 and 5.". The error message is then caught in a try-except
# block and printed to the user with the message, "Error: [error message].
# Please enter an integer between 1 and 5.". Finally, the function returns
# False to indicate that the input was invalid. If the input is within the
# range, the function returns True to indicate that the input is valid.
def check_valid_input(value):
    try:
        if not 1 <= int(value) <= 5:
            raise ValueError("Invalid input! Choose a number between 1 and 5.")
    except ValueError as error:
        print(f"Error: {error}")
        print("Please enter an integer between 1 and 5.")
        return False
    return True


# count_hits takes a board as an argument, which is expected to be a list
# representing the player's board. The function counts the number of times the
# string "#" appears in the board, which represents a hit battleship.
# The function returns the sum of all the "#" counts.
def count_hits(board):
    return sum(row.count(" # ") for row in board)


# check_winner checks if there is a winner after ten turns of the game.
# It calls the count_hits function to find the number of hits for the player
# and the opponent, stored in the variables player_hits and opponent_hits
# respectively. The function then compares the two counts and prints a message
# indicating the result of the game. If the number of hits for the player is
# greater than that of the opponent, the player wins. If the number of hits for
# the opponent is greater, the opponent wins. If the number of hits for both
# players is the same, it's a tie.
def winner_check_final():
    player_hits = count_hits(player_guesses)
    opponent_hits = count_hits(opponent)
    if player_hits > opponent_hits:
        print("Congratulations! You WIN! 🥳")
    elif player_hits < opponent_hits:
        print("Sorry, the opponent had more hits! 😔")
    else:
        print("It was a tie!")


# Finally, the code calls the play_game function, which is the main function
# for playing the game.
play_game()