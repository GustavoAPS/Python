import art

def add(a,b):
  return a+b

def subtract(a,b):
  return a-b

def divide(a,b):
  
  if b == 0:
    return

  return a/b

def multiply(a,b):
  return a*b

operations = {
"+":add,
"-":subtract,
"/":divide,
"*":multiply
}

def print_operations():
  for operation in operations:
    print(operation)

def calculator():

  num_1 = float(input("What is the first number?\n"))
  num_2 = float(input("What is the second number?\n"))

  print_operations()

  symbol = input("Pick an operation from the line above\n")

  result = operations[symbol](num_1,num_2)

  print(result)

  #answer = "y"

  def continue_operations(result):

    answer = input("Continue with this number?(Y or N\n")

    if answer == "n":
      return

    print_operations()
    symbol = input("Pick an operation from the line above\n")
    num_3 = float(input("What is the number to operate?\n"))
    new_result = operations[symbol](result,num_3)
    print(new_result)

    continue_operations(new_result)

  continue_operations(result)

  if input("start a new calculation?(y or n)\n") == "y":
    calculator()

print(art.logo)
calculator()