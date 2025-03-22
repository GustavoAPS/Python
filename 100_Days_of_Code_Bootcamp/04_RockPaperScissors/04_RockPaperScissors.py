import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choise = int(input("What do you chose?\n1 - Rock\n2 - Paper\n3 - Scissors\n"))

computer_choise = random.randint(1,3)

print("You")

if(player_choise == 1):
  print(rock)
elif(player_choise == 2):
  print(paper)
else:
  print(scissors)

print("Computer")

if(computer_choise == 1):
  print(rock)
elif(computer_choise == 2):
  print(paper)
else:
  print(scissors)

if(computer_choise == player_choise):
  print("Draw")
elif(computer_choise == 1 and player_choise == 2):
  print("You Won!")
elif(computer_choise == 1 and player_choise == 3):
  print("You Lose")
elif(computer_choise == 2 and player_choise == 1):
  print("You Lose")
elif(computer_choise == 2 and player_choise == 3):
  print("You Won")
elif(computer_choise == 3 and player_choise == 1):
  print("You Won")
elif(computer_choise == 3 and player_choise == 2):
  print("You Lose")