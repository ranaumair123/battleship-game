import random


hit = []
miss = []
comp = []
shots = 0
sank = []


def show_board(hit, miss, comp):
    print("Welcome to Battleship game")
    print("Rules of the Game")
    print("1:You have 50 Shots to destory 2 enemy ships")
    print("2:x on the board mean you missed the ship")
    print("3:o on the board mean you hit a part of ship")
    print("4:O on the board mean you destroyed the ship")

    print("SHOTS USED")
    print(shots)
    print("SHIPS DESTROYED")
    print(len(sank))

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
        print(x, "", row)


# Function to get a shot from the user
def get_shot():
    show_board(hit, miss, comp)
    guesses = hit + miss + comp
    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter your guess for example 00 , 10, 99:\n")
            if not shot.isdigit():
                raise ValueError("Incorrect, please enter only numbers")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("Incorrect number, please try again")
            elif shot in guesses:
                print("Incorrect number, this is used before")
            else:
                ok = "y"
        except ValueError as e:
            print(e)
    return shot

# Function to check if a shot hits a boat
def check_shot(shot, bt1, bt2, hit, miss, comp):
    if shot in bt1:
        bt1.remove(shot)
        if len(bt1) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
            sank.append(1)

    elif shot in bt2:
        bt2.remove(shot)
        if len(bt2) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
            sank.append(1)
    else:
        miss.append(shot)
    return bt1, bt2, hit, miss, comp
# this will generate boat 1 with 3 coordinates


while True:
    coordinate = random.randint(0, 96)
    horizontal = random.choice([True, False])
    if horizontal:
        bt1 = [coordinate, coordinate+1, coordinate+2]
    else:
        bt1 = [coordinate, coordinate+10, coordinate+20]
    if all(coord < 100 for coord in bt1):
        break

# this will generate boat 2 with 4 coordinates
while True:
    coordinate = random.randint(0, 96)
    horizontal = random.choice([True, False])
    if horizontal:
        bt2 = [coordinate, coordinate+1, coordinate+2, coordinate+3]
    else:
        bt2 = [coordinate, coordinate+10, coordinate+20, coordinate+30]
    if all(coord < 100 for coord in bt2):
        break


# i in range will decide numbe of shots
for i in range(50):
    guesses = hit + miss + comp
    shot = get_shot()
    bt1, bt2, hit, miss, comp = check_shot(shot, bt1, bt2, hit, miss, comp)
    show_board(hit, miss, comp,)
    shots += 1
    if len(bt1) < 1 and len(bt2) < 1:
        print("you won")
        print("game over")
    elif shots == 50:
        print("Shots finished")
        print("you lost")
        break
