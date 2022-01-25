# Create an automatic pizza order program.
print("*" * 5 + " WELCOME TO MEL'S PIZZA DELIVERIES " + "*" * 5)
print("S - Small   M - Medium   L - Large   Y - Yes   N - No ")
size = input("What size of pizza do you want? L  M  S ")
add_pepperoni = input("Do you want pepperoni added? Y  N ")
extra_cheese = input("Do you want extra cheese?  Y  N ")
bill = 0
if size == "L":
    bill = 25
    print("Large Pizza cost $25. ")
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")
elif size == "M":
    bill = 20
    print("Medium pizza cost $20. ")
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")
else:
    bill = 15
    print("Small pizza cost $15. ")
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")

print(" Thanks for your patronage!!! ")







