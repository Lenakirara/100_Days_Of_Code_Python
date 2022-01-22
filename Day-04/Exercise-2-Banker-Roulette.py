"""
You are going to write a program that will select a random name from a list of
names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them
inside a List called names. For this to work, you must enter all the names
as names followed by comma then space. e.g. name, name, name

When you run the code, just use a random number as the seed. e.g. 67346 It
doesn't matter what you chose, it's only for our testing code to check your
work.
"""

import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

lenghth_name = len(names)
random_names = random.randint(0, lenghth_name - 1)
get_name_random = names[random_names]
print(f'{get_name_random} is going to buy the meal today!')

# print(random_names)

"""
using choice:

random_name = random.choice(names)
print(f"{random_name} is going to buy the meal today!")
"""
