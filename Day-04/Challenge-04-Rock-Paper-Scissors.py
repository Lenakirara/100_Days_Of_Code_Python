"""
Make a rock, paper, scissors game.

Inside the main.py file, you'll find the ASCII art for the hand signals
already saved to a corresponding variable: rock, paper, and scissors.
This will make it easy to print them out to the console.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine
the winner (or a draw).
And also how you will give feedback to the player.
"""
import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("*** Welcome to the Rock Paper Scissors Game ***")
print("\n")
choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "
    )
)

itens = ("rock", "paper", "scissors")
random_game = random.randint(0, 2)
# print(random_game)

if choice < 0 or choice > 2:
    print(
        "You type invalid number. Sorry! You Lose!"
    )
else:
    print(f"You played {itens[choice]}\n")

    if random_game == 0:
        print(f"Computer Choose {itens[random_game]}")
        print(f"{rock}")
        if choice == 0:
            print(f"{rock}")
            print("DRAWN!")
        elif choice == 1:
            print(f"{paper}")
            print("YOU WIN!")
        elif choice == 2:
            print(f"{scissors}")
            print("YOU LOSE!")

    elif random_game == 1:
        print(f"Computer Choose {itens[random_game]}")
        print(f"{paper}")
        if choice == 1:
            print(f"{paper}")
            print("DRAWN!")
        elif choice == 0:
            print(f"{rock}")
            print("YOU WIN!!")
        elif choice == 2:
            print(f"{scissors}")
            print("YOU LOSE!")

    elif random_game == 2:
        print(f"Computer Choose {itens[random_game]}")
        print(f"{scissors}")
        if choice == 2:
            print(f"{scissors}")
            print("DRAWN!")
        elif choice == 0:
            print(f"{rock}")
            print("YOU WIN!!")
        elif choice == 1:
            print(f"{paper}")
            print("YOU LOSE!")
