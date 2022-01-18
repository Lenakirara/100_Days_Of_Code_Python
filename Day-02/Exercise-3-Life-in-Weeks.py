"""
Create a program using maths and f-Strings that tells us how many days, weeks, 
months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time
left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.z
"""

age = input("What is your current age?")

year_difference = 90 - int(age)
days = 365 * year_difference
weeks = 52 * year_difference
months = 12 * year_difference
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
