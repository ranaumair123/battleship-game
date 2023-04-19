import random

grid = [[11,  12,  13,  14,  15,  16,  17,  18],
        [21,  22,  23,  24,  25,  26,  27,  28],
        [31,  32,  33,  34,  35,  36,  37,  38],
        [41,  42,  43,  44,  45,  46,  47,  48],
        [51,  52,  53,  54,  55,  56,  57,  58],
        [61,  62,  63,  64,  65,  66,  67,  68],
        [71,  72,  73,  74,  75,  76,  77,  78],
        [81,  82,  83,  84,  85,  86,  87,  88]]
        

for row in grid:
    for item in row:
        print('{:<7}'.format(item), end='')
    print()
# Choose a random item from the grid
random_row = random.choice(grid)
random_item = random.choice(random_row)

# Print the random item
print(f'The randomly chosen item is: {random_item}')

# Ask the user to choose a cell
user_row = int(input('Enter the row number: '))
user_col = int(input('Enter the column number: '))

# Check if the user's choice is valid
if user_row < 1 or user_row > len(grid) or user_col < 1 or user_col > len(grid[0]):
    print('Invalid input! Row and column numbers must be within range.')
else:
    user_choice = grid[user_row-1][user_col-1]
    print(f'Your choice is: {user_choice}')
