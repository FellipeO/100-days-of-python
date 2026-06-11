import random
import art

def choose_difficulty():
    choice = input("Choose a difficulty: Type 'easy' or 'hard': ".lower())
    if choice != "easy" and choice != "hard":
        print ("Invalid option.\n")
        choose_difficulty()
    elif choice == "easy":
        return 10
    else:
        return 5

def number_comparison (num, guess_num):
    if num == guess_num:
        return True
    elif num > guess_num:
        print("Too low")
        return False
    else:
        print("Too high")
        return False

print(f"{art.logo}\nWelcome to the number guessing game!\nThere's a number between 1 and 100 you have to guess.")
number = random.choice(range(1,100))
attempts = choose_difficulty()
win = False

while attempts > 0 and not win:
    guess = int(input(f"You have {attempts} attempts left.\nMake a guess: "))
    win = number_comparison(number, guess)
    attempts -= 1

if win:
    print(f"You got it! The answer was {number}")
else:
    print(f"You lose. No more guesses, the answer was {number}!")

