
# Battleship Game
Battleship game is Pytho terminal game, which runs in Code institute mock terminal on Heroku
Player can try to beat the computer by destroying the computer ship with limited given shots.

<img src = images/mockup.png>

## How to Play
Battleship game is classic game which we used to play on paper. This verison is the same as paper but on computer and the player will play not with friend but computer.

The game i designed have a board of 10x10.
Their are 50 shots means 50 trys to find computer ships.
Their are 2 ship one is 3 cells long and the other is 4 cells long, which are generated ramdomly by computer.
Player have to finds all the cells which contains ships in order to win the game.
If user could not find ship and fire all 50 bullet , user will lose the game.


# Features
## Existing Features
<img src = images/feature2.png>




The main feature of the game is when you miss the ship it put X when you hit ship it put o and when you destory the whole ship the last cell is big O




<img src = images/feature.png>



## Future Features


I want to add another board for user, on which user can place ships and then computer can randomly guess the  ships


## Testing
I tested the code and validated it 
I checked that game is over when the bullets are finished.
I checked when player hit both ship game is over,
I checked that their is X when the hit is missed.
I checked that their is o when ship is hit.
I checked that when the last cell of ship is hit its O.


# Bugs

## Solved bugs
Few lines of codes are very big and wasn't complying with the PEP8 standards.
So i changed the long variables names to small meaningful names

## Remaning bugs
when i deployed code on heroku. when i put alphabet the code give error and stops. but in github terminal its works fine.


## Validator Testing
PEP8
No errors werereturned from https://pep8ci.herokuapp.com/#

## Deployment
I deployed the project in Heroku.com

## Credits
code institue for deployment terminal
wikipedia for game information
youtube for studing different codes