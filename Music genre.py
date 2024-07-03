#!/usr/bin/env python

import random

def main():
    """Start a music genre guessing game."""
    print("Guess the music genre!")

    music = [
        "pop",
        "rock",
        "rap",
        "country",
        "blues",
        "folk",
        "jazz", "soul"
        ]

    x = random.choice(music)
    print(x)
    guess = None
    chance = 3
    score = 10

#selagi tekaan pemain tak sama dengan guess
    while x != guess: 
      while chance != 0:   #tekaan akan diteruskan sekiranya bilangan chance tak sama dengan 0
        guess = str(input("What music genre am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            print("You got {} points.".format(score))
            break
        else:
            chance=chance-1
            score=score-1
            if chance == 0:
              print("You guessed {}. Unfortunately you got the wrong answer.".format(guess))
              print("You have no more chance.")
              print("Game over")
              break
            else:
              print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
              print("You can choose from the list below")
              print("=========================================")
              print("pop rock rap country blues folk jazz soul")
              print("=========================================")
              print("You have {} more try.".format(chance))
      break      

main()