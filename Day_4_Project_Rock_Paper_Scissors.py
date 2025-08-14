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


choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
)

the_choice = [rock, paper, scissors]

random_index = random.randint(0, 2)

computer_choice = the_choice[random_index]
your_choice = the_choice[choice]

if your_choice == computer_choice:
    print("Your choice: " + "\n" + your_choice)
    print("Computer choice: " + "\n" + computer_choice)
    print("DRAWN")

elif your_choice == rock and computer_choice == paper:
    print("Your choice: " + "\n" + your_choice)
    print("Computer choice: " + "\n" + computer_choice)
    print("COMPUTER WIN")

elif your_choice == paper and computer_choice == scissors:
    print("Your choice: " + "\n" + your_choice)
    print("Computer choice: " + "\n" + computer_choice)
    print("COMPUTER WIN")

elif your_choice == scissors and computer_choice == rock:
    print("Your choice: " + "\n" + your_choice)
    print("Computer choice: " + "\n" + computer_choice)
    print("COMPUTER WIN")

else:
    print("Your choice: " + "\n" + your_choice)
    print("Computer choice: " + "\n" + computer_choice)
    print("YOU WIN")
