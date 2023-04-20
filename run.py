# Import the randint function from the random module
from random import randint

# Board for holding ship locations
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 8 for i in range(8)]

# Function to print the game board
def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

# Dictionary to map letters to numbers for column input
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

# Function to create the ships on the board
def create_ships(board):
    for ship in range(5):
        # Get a random row and column for the ship location
        ship_row, ship_column = randint(0,7), randint(0,7)
        # Check if a ship already exists at that location, if so, get new location
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        # Place the ship on the board
        board[ship_row][ship_column] = "X"

# Function to get the row and column input from the player
def get_ship_location():
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

# Function to count the number of hit ships
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

# Main game loop
if __name__ == "__main__":
    # Create the ships on the hidden board
    create_ships(HIDDEN_BOARD)
    # Set the number of turns to 10 and score to 0
    turns = 10
    score = 0
    while turns > 0:
        # Print the guess board and get the row and column input from the player
        print('Guess a battleship location')
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        # Check if the player has already guessed that location
        if GUESS_BOARD[row][column] == "-":
            print("You guessed that one already.")
        # Check if the player has hit a ship
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit")
            GUESS_BOARD[row][column] = "X" 
            score += 1
            turns -= 1  
        # If the player missed the ship
        else:
            print("MISS!")
            GUESS_BOARD[row][column] = "-"  
            turns -= 1     
        if count_hit_ships(GUESS_BOARD) == 5:
            print("You win!")
            break
        print("You have " + str(turns) + " turns left and your score is " + str(score))
        if turns == 0:
            print("GAME OVER")

    