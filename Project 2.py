#TIP CALCULATOR
print("Welcome to the Tip calculator.")
bill = float(input("Enter your total bill : "))
tip = int(input("What percentage of tip would you like to add? : "))
tipped = (bill+(bill*(tip/100)))
people = int(input("How many people want to split it? : "))
split = tipped/people
final_pay = round(split , 2)
print(f"Each person should pay ${final_pay}.")