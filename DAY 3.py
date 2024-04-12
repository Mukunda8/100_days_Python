# #Interactive code 1
# print("Welcome to theme park!!")
# height = int(input("Enter your height : "))
# if height > 120:
#     print("You can ride.")
# else:
#     print("You cant ride.")
    
# #Interactive code 2
# Num = int(input("Enter your number : "))
# if Num%2 == 0:
#     print("Its even.")
# else:
#     print("Its odd.")
    
# #Interactive code 3
# print("Welcome to theme park!!")
# height = int(input("Enter your height : "))
# if height > 120:
#     print("You can ride.")
#     age = int(input("Enter your age : "))
#     if age >= 18:
#         print("The ticket costs you $12.")
#     else:
#         print("The ticket costs you $7.")
# else:
#     print("You cant ride.")

# #Interactive code 4
# print("Welcome to BMI calculator.")
# height = input("Enter your height.")
# weight = input("Enter your weight.")
# BMI = int(weight)/(float(height)**2)
# if BMI < 18.5:
#     print(f"Your BMI is {BMI} you are underweight.")
# elif 18.5 < BMI <25:
#     print(f"Your BMI is {BMI} are normal.")
# elif 25 < BMI < 30:
#     print(f"Your BMI is {BMI} are slightly overweight.")
# elif 30 < BMI < 35:
#     print(f"Your BMI is {BMI} are obese.")
# elif BMI > 35:
#     print(f"Your BMI is {BMI} are clinically obese.")

##Interactive code 5
# print("Welcome to leap year calculator.")
# year = int(input("Enter your year."))
# if year%4 == 0:
#     if year%100 == 0:
#         if year%400 == 0:
#             print("Its a leap year.")
#         else:
#             print("Its not a leap year.")
#     else:
#         print("Its a leap year.")
# else:
#     print("Its not a leap year.")            

# #Interactive code 6
# print("Welcome to Python Pizza shop!!")
# size = input("Enter the size of pizza. S or M or L.")
# pprn = input("Do you want to add peparoni on this pizza? Y or N.")
# cheese = input("Do you want to add cheese to this pizza? Y or N.")
# cost = 0
# if size == "S":
#     cost += 15
#     if pprn == "Y":
#         cost += 2
# elif size == "M":
#     cost += 20
#     if pprn == "Y":
#         cost += 3
# elif size == "L":
#     cost += 25
#     if pprn == "Y":
#         cost += 3
# if cheese == "Y":
#     cost += 1  
# print(f"Your total bill is ${cost}")

# #Interactive code 7
# print("Welcome to love calculator!!")
# name1 = input("Enter your name : ")
# name2 = input("Enter another name : ")
# Total_name = name1+name2
# tn = Total_name.lower()
# T = tn.count("t")
# R = tn.count("r")
# U = tn.count("u")
# E = tn.count("e")
# L = tn.count("l")
# O = tn.count("o")
# V = tn.count("v")
# first_digit = T + R + U + E
# second_digit = L + O + V + E
# print(f"Your love score is {first_digit}{second_digit}")
# score = int(str(first_digit)+str(second_digit))
# if (score < 10) or (score > 90):
#     print("You are like coke and mentos.")
# elif (score >= 40) or (score <= 50):
#     print("You are alright togeather.")
# else:
#     print("You are perfect.")
