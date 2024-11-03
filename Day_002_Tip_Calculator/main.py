
print("Welcome to the tip calculator!")
total = float(input("What was the total bill? €"))
tip = int(input("How much tip would you like to give? 10, 12 or 15: "))
people = int(input("How many people to split the bill? "))
result = (total * tip / 100 + total) / people
print("Each person should pay: €" + str(round(result, 2)))
