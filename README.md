## Bomb Guessing Game (Python)

### Overview

This is a simple command-line game written in Python. The player selects a difficulty level, and a list of numbers is generated. One number is randomly chosen as the "bomb". The goal is to avoid selecting the bomb and survive until only one number remains.

### How the Game Works

The player selects a difficulty level:
Easy → 3 numbers
Medium → 6 numbers
Hard → 10 numbers

A list of numbers is created based on the difficulty.

One number is randomly selected as the bomb.

The player can choose to see a hint (reveals the bomb).

The player keeps selecting numbers:
If the number is not the bomb → it gets removed from the list
If the number is the bomb → the player loses

If only one number remains → the player wins

### Features

Difficulty selection system
Input validation (handles invalid inputs)
Optional hint system
Random bomb placement
Simple and interactive gameplay


### How to Run

Save the file as game.py

Open terminal or command prompt

Run the program:
python game.py

### Example Gameplay

enter your difficulty:
Easy,Medium,hard:
---> easy

The element are: [1, 2, 3]

do you want hint??(y/n): n

enter your choice: 2
that was not the bomb, you live for now
[1, 3]

### Possible Improvements

Add score tracking
Add multiple rounds
Hide hint after one use
Add GUI version
Add sound effects

### Author

Sanju Kumar
