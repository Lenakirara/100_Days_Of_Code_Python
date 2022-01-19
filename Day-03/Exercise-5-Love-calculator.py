"""
You are going to write a program that tests the compatibility
between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters
in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.
"""

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

both_names = name1 + name2
name_lower = both_names.lower()
t = name_lower.count("t")
r = name_lower.count("r")
u = name_lower.count("u")
e = name_lower.count("e")
word_true = t + r + u + e

lo = name_lower.count("l")
o = name_lower.count("o")
v = name_lower.count("v")
e = name_lower.count("e")
word_love = lo + o + v + e

score = int(str(word_true) + str(word_love))

if score < 10 or score > 90:
    print(
        f"Your score is {score}, you go together like coke and mentos."
    )
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
