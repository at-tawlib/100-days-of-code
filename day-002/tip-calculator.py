#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print("Welcome ot the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_bill = bill + ((bill * tip_percentage) / 100)
num_of_people = int(input("How many people to split the bill? "))
amount_to_pay = round(total_bill / num_of_people, 2)
message = f"Each person should pay: ${amount_to_pay}"
print(message)