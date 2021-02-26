print("Welcome to the Tip Calculator")
bill = int(input("What was the total bill? $"))
tip = int(input("What precentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

#math operation
tip_percentage = tip / 100
tip_val = tip_percentage * bill
total_val = bill + tip_val
bill_each = total_val / people
finalamount = round(bill_each, 3)
finalamount = "{:.2f}".format(bill_each)
print(f"Each person should pay: ${finalamount}")