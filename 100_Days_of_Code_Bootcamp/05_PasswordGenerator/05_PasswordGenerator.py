#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

random_list = [nr_numbers,nr_symbols,nr_letters]

#print(random_list)

#numbers, symbols, letters
while random_list[0] > 0 or random_list[1] > 0 or random_list[2] > 0:

  option = random.randint(1,3)

  if option == 1 and random_list[0] > 0:
    password += str(random.choice(numbers))
    random_list[0] -= 1

  if option == 2 and random_list[1] > 0:
    password += str(random.choice(symbols))
    random_list[1] -= 1

  if option == 3 and random_list[2] > 0:
    password += str(random.choice(letters))
    random_list[2] -= 1

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P