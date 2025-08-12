print("Welcome to the tip caculator!")
totalBill = float(input("What was the total bill? $"))
tip = int(input("How much tip you would lile to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
shouldPay = (((totalBill*tip)/100) + totalBill)/people
shouldPay = float(round(shouldPay,2))
print(f"Each person should pay: ${shouldPay}")