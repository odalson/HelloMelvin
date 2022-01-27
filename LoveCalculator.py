# Create a love calculator to determine the relationship status of two people.

name1 = input("What  is your full name? \n")
name2 = input("What is the name of your partner? \n")
combine_name = name1 + name2
lower_name = combine_name.lower()
# To count the number of times each letter of t, r, u, e, l, o, v, e occurs in the names entered
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
true = t + r + u + e
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
love = l + o + v + e
# Adding the integers of both true and love.
love_score = str(true) + str(love)

if (int(love_score) < 10) or (int(love_score) > 60):
    print(f"Your love score is {love_score}, you go together like coke and mentos. ")
elif (int(love_score) >= 40) and (int(love_score) <= 50):
    print(f"Your love score is {love_score}, you are alright together. ")
else:
    print(f"Your score is {love_score}. ")
