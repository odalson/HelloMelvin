
print("*" * 3 + " Welcome to your tip Calculator " + "*" * 3)
bill = input("What is your total bill? ")
percent = input("What percentage tip would you like to give? ")
split = input("How many people will be splitting the bill? ")
# Calculate the percentage tip
percent_tip = 100 + float(int(percent))
# Calculate the total bill with the percentage tip
total_bill = (float(percent_tip) * float(bill))/100
# Divide the payment among the people
payment = float(total_bill) / int(split)
pay = round(float(payment), 2)
print("Each person should pay: " + "$" + str(pay))
