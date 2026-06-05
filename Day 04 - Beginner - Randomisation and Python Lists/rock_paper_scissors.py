import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hands = [rock, paper, scissors]
choice = int(input("Type 0 for rock, 1 for paper or 2 for scissors: "))

if choice > 2 or choice < 0:
    print("Invalid number! You lose!")
    exit(0)

computer = random.randint(0,2)

print(f"You chose:\n{hands[choice]}")
print(f"Computer chose:\n{hands[computer]}")

if hands[choice] == hands[computer]:
    print("Draw!")
elif choice == 0:
    if computer == 1:
        print("You lose!")
    else:
        print("You win!")
elif choice == 1:
    if computer == 2:
        print("You lose!")
    else:
        print("You win!")
else:
    if computer == 0:
        print("You lose!")
    else:
        print("You win!")
