import random
# Start the game
hit = []
miss = []
comp = []
shots = 0 

def show_board(hit, miss, comp):
    print("Welcome to Batlleship game")
    print("Rules of the Game")
    print("1:You have 50 Shots to  destory 2 enemy ships")
    print("2:x on the board mean you missed the ship")
    print("3:o on the board mean you hit a part of ship")
    print("4:O on the board mean you destroyed the ship")
    
    print("SHOTS USED")
    print(shots)
    
    print("    0  1  2  3  4  5  6  7  8  9")
    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in miss:
                ch = " x "
            elif place in hit:    
                ch = " o "
            elif place in comp:
                ch = " O "
            row = row + ch 
            place = place + 1
        print(x,"",row)


# Function to get a shot from the user
def get_shot():
    show_board(hit, miss, comp,)

    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter your guess: ")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("Incorrect number, please try again")
            elif shot in guesses:
                print("Incorrect number, this is used before")
            else:
                ok = "y"
                break
        except:
            print("Incorrect entry - please enter again")
    return shot

# Function to display the game board

# Function to check if a shot hits a boat
def check_shot(shot, boat1, boat2, hit, miss, comp):
    if shot in boat1:
        boat1.remove(shot)
        if len(boat1) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
    elif shot in boat2:
        boat2.remove(shot)
        if len(boat2) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
    else:
        miss.append(shot)
    return boat1, boat2, hit, miss, comp

# this will generate boat 1 with 3 coordinates
while True:
    start_coordinate = random.randint(0, 96)
    horizontal = random.choice([True, False])
    if horizontal:
        boat1 = [start_coordinate, start_coordinate+1, start_coordinate+2]
    else:
        boat1 = [start_coordinate, start_coordinate+10, start_coordinate+20]
    if all(coord < 100 for coord in boat1):
        break

# this will generate boat 2 with 4 coordinates
while True:
    start_coordinate = random.randint(0, 96)
    horizontal = random.choice([True, False])
    if horizontal:
        boat2 = [start_coordinate, start_coordinate+1, start_coordinate+2, start_coordinate+3]
    else:
        boat2 = [start_coordinate, start_coordinate+10, start_coordinate+20, start_coordinate+30]
    if all(coord < 100 for coord in boat2):
        break



# i in range will decide numbe of shots
for i in range(50):
    guesses = hit + miss + comp
    shot = get_shot()
    boat1, boat2, hit, miss, comp = check_shot(shot, boat1, boat2, hit, miss, comp)
    show_board(hit, miss, comp,)
    shots += 1 
    if len(boat1) < 1 and len(boat2) < 1:
        print("you won")
        print("game over")
        break
