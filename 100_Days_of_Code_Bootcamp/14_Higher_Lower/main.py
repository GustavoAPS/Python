import art
import game_data
import random

print(art.logo)

def higherLower(n,score):
  print("-----------------------------")
  print(f"Score: {score}")
  b = random.randint(0,49)
  
  while b == n:
    b = random.randint(0,49)

  print("Profile A")
  print(game_data.data[n]["name"])
  print(game_data.data[n]["description"])
  print(game_data.data[n]["country"])

  print(art.vs)
  print("Profile B")
  print(game_data.data[b]["name"])
  print(game_data.data[b]["description"])
  print(game_data.data[b]["country"])
  
  option = input("\nA or B?")

  if option == "a" or option == "A":
    if game_data.data[n]["follower_count"] > game_data.data[b]["follower_count"]:
      higherLower(n,(score+1))
    else:
      return
  if option == "b" or option == "B":
    if game_data.data[n]["follower_count"] < game_data.data[b]["follower_count"]:
      higherLower(b,(score+1))
    else:
      return
  else:
    return

n = random.randint(0,49)
higherLower(n,0)
print("Game Over")
