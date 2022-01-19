"""
Make your own "Choose Your Own Adventure" game. Use conditionals such
as if, else, and elif statements to lay out the logic and the story's
path in your program.

Text Snippets from example:
'You\'re at a crossroad. Where do you want to go? Type "left" or "right"'
'You\'ve come to a lake. There is an island in the middle of the lake. Type
"wait" to wait for a boat. Type "swim" to swim across.'
"You arrive at the island unharmed. There is a house with 3 doors. One red,
one yellow and one blue. Which colour do you choose?"
"It's a room full of fire. Game Over."
"You found the treasure! You Win!"
"You enter a room of beasts. Game Over."
"You chose a door that doesn't exist. Game Over."
"You get attacked by an angry trout. Game Over."
"You fell into a hole. Game Over."

"""
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure.")

direction = input(
    'You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n'
)
if direction == "left":
    print(
        "You've come to a lake. There is an island in the middle of the lake."
    )
    choose = input(
        'Type "wait" to wait for a boat. Type "swim" to swim across.\n'
    )
    if choose == "wait":
        print("You arrive at the island unharmed.")
        choose_door = input(
            "There is a 3 doors: 'red', 'yellow' and 'blue'. Choose the color!"
        )
        if choose_door == "red":
            print("you were attacked by a beast! Sorry! Game Over!")
        elif choose_door == "yellow":
            print("fire room! Sorry! Game Over!")
        elif choose_door == "blue":
            print("You found the treasure! You Win!")
        else:
            print("Choose one of the doors")
    elif choose == "swim":
        print("You were attacked by the lake deminpiac mermaid! Game over!")
    else:
        print(
            'Incorrect choice! Do you want to "wait" for the boat or "swim"?'
        )
elif direction == "right":
    print("Oh no! You fell in a hole with poisonous snakes! Game Over!")
else:
    print('You need to choose "left" or "right" to continue the game!')
