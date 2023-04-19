import random



player_grid =   [[11,  12,  13,  14,  15,  16,  17,  18],
                 [21,  22,  23,  24,  25,  26,  27,  28],
                 [31,  32,  33,  34,  35,  36,  37,  38],
                 [41,  42,  43,  44,  45,  46,  47,  48],
                 [51,  52,  53,  54,  55,  56,  57,  58],
                 [61,  62,  63,  64,  65,  66,  67,  68],
                 [71,  72,  73,  74,  75,  76,  77,  78],
                 [81,  82,  83,  84,  85,  86,  87,  88]]


computer_grid = [[11,  12,  13,  14,  15,  16,  17,  18],
                 [21,  22,  23,  24,  25,  26,  27,  28],
                 [31,  32,  33,  34,  35,  36,  37,  38],
                 [41,  42,  43,  44,  45,  46,  47,  48],
                 [51,  52,  53,  54,  55,  56,  57,  58],
                 [61,  62,  63,  64,  65,  66,  67,  68],
                 [71,  72,  73,  74,  75,  76,  77,  78],
                 [81,  82,  83,  84,  85,  86,  87,  88]]

for i in range(7):
    print(f'Turn {i+1}:')
    
    print('Player Board')
    for row in player_grid:
        for item in row:
            print('{:<7}'.format(item), end='')
        print()
        
    # Choose a random item from the grid
    random_row = random.choice(player_grid)
    random_item = random.choice(random_row)
    # this is to see computer choice
    print(f'The randomly chosen item is: {random_item}')

    print('Computer Board')
    for row in computer_grid:
        for item in row:
            print('{:<7}'.format(item), end='')
        print()

    # Choose a random item from the grid
    random_row = random.choice(computer_grid)
    random_item = random.choice(random_row)
    # this is to see computer choice
    print(f'The randomly chosen item is: {random_item}')

    

    # Ask the user to choose a cell
    print('GUIDE')
    print('First number in the grid is row and second is column so choose the row and column accordingly')
    print('For Example row 1 and column 1 would be 11 in grid')
    user_row = int(input('Enter the row number: '))
    user_col = int(input('Enter the column number: '))

    # Check if the user's choice is valid
    if user_row < 1 or user_row > len(computer_grid) or user_col < 1 or user_col > len(computer_grid[0]):
        print('Invalid input! Row and column numbers must be within grid.')
    else:
        user_choice = computer_grid[user_row-1][user_col-1]
        print(f'Your choice is: {user_choice}')
        
        # Compare user's choice and computer's choice
        if user_choice == random_item:
            print('Congratulations! You guessed the same number as the computer!')
            computer_grid[user_row-1][user_col-1] = 'X'
        else:
            print('torpedo missed')
            
    print()