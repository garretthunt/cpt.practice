# ROCK PAPER SCISSORS TOURNAMENT - GARRETT HUNT, ALEX NIKIFOROV
# Rock-Paper-Scissors tournament — Stores match history in a list; a procedure runs multiple rounds using iteration and selection to determine a champion.
import random

rock = 1
paper = 2
scissors = 3

opponent = random.randint(1, 3)

rounds = int(input("Enter the amount of rounds you would like to play"))

for round in range(rounds):
    initial_player = (input("Enter your guess out of rock, paper, or scissors: "))
    player = initial_player.lower
    opponent = random.randint(1, 3)
    if opponent == rock:
            if player == 