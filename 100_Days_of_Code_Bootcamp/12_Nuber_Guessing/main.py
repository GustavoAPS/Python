#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import art

def guess_game():

  print (art.logo)
  print("Wellcome to the number guessing game")
  print("I'm thinking in a number between 1 and 100")
  dificulty = input("type the dificulty 'easy' or 'hard'\n")

  number_chosen = random.randint(1,100)
  player_won = False
  attempts = 0

  if(dificulty == "hard"):
    attempts = 5
  else:
    attempts = 10

  for n in range(0,attempts):
    
    if (player_won == False):

    print(f"{attempts - n} Turns remaining ")

      number_guessed = int(input("What number do you chose?\n"))

      if(number_guessed == number_chosen):
        player_won = True

      elif(number_guessed > number_chosen):
        print("Too high.")

      else:
        print("Too low.")

  if (player_won == True):
    print("You Won")
  else:
    print("You lose")

guess_game()