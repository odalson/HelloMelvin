# This program is meant to tell you the number of days, weeks and months you have left if you are to live for 90years.
name = input("Please enter your first name only: ")
age = input("Please enter your current age in whole number: ")
left_age = 90 - int(age)
left_days = 365 * left_age
left_weeks = 52 * left_age
left_months = 12 * left_age
print(f"{name}, you have {left_days} days, {left_weeks} weeks, {left_months} months till 90years")
