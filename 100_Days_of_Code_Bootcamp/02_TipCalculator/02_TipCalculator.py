print("Welcome to the tip calculator\n")

bill = input("What was the total bill?\n")
tip = input("What percentage tip would you like to give? 10,12 or 15? \n")
people = input("How many people to split the bill? \n")

total_bill = (float(bill) + ((float(bill)/100) * float(tip)))
total_value = total_bill / float(people)
individual_value = round(total_value, 2)

print(f"Each pearson should pay {individual_value}$\n")
