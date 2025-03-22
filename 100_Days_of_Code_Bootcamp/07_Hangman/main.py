import random
import hangman_art
import hangman_words

#word_list = ["aardvark", "baboon", "bicurioso"]
chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for letter in chosen_word:
  display.append("_")

print(hangman_art.stages[6])

print(display)

won = False
lose = False
lifes = 7

while (not  won) and (not lose): 

  guess = input("Guess a letter: ").lower()
  counter = 0

  lost_life = True

  for letter in chosen_word:
      if letter == guess:
          display[counter] = letter
          lost_life = False
      counter += 1

  if lost_life:
    lifes -= 1
  
  print(f"{display} You have {lifes} lifes left")
  print(hangman_art.stages[lifes-1])

  if lifes <= 0:
    lose = True
  else:
    won = True
    counter = 0

    for letter in chosen_word:
      if not(letter == display[counter]):
        won = False
      counter += 1

if won:
  print("You won")

if lose:
  print("You lose")