import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

hands = {
    "User": [],
    "Computer": [],
}

def deal(current_hands, current_turn):
    """Deal a card as well as the initial hand in case no cards have been dealt"""
    if not current_hands["User"]:
        for _ in range(2):
            current_hands ["User"].append(random.choice(cards))
            current_hands ["Computer"].append(random.choice(cards))
    else:
        current_hands[current_turn].append(random.choice(cards))

def calculate(current_hands, current_turn):
    """Calculates the score of a hand"""
    if sum(current_hands[current_turn]) > 21:
        if 11 in current_hands[current_turn]:
            to_replace = current_hands[current_turn].index(11)
            current_hands[current_turn][to_replace] = 1
    return sum(current_hands[current_turn])

def hands_description(current_hands, current_turn):
    """Returns a string describing the cards present in both hands and their respective score"""
    if current_turn == "User":
        return (f"Your cards: {current_hands["User"]}, current score: {calculate(current_hands, "User")}"
                f"\nComputer's first card: [{11 if current_hands["Computer"][0] == 1 else current_hands["Computer"][0]}]")
    else:
        return(f"Your final hand: {current_hands["User"]}, final score: {calculate(current_hands, "User")}"
               f"\nComputer's final hand: {current_hands["Computer"]}, final score {calculate(current_hands,"Computer")}")

def play_game():
    """Starts a new game"""
    if input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == "y".lower():
        print(art.logo)
        hands["User"] = []
        hands["Computer"] = []
        deal(hands, "User")
        if calculate(hands, "Computer") == 21:
            print (f"{hands_description(hands, "Computer")}\nComputer got a blackjack. You lose!\n")
            play_game()
        elif calculate(hands, "User") == 21:
            print(f"{hands_description(hands, "Computer")}\nYou got 21, You win!\n")
            play_game()
        else:
            calculate(hands,"User")
            print (f"{hands_description(hands, "User")}")
            while input("Type 'y' to get another card 'n' to pass: ") == "y":
                deal(hands,"User")
                if calculate(hands, "User") > 21:
                    print(f"{hands_description(hands, "Computer")}\nYou went over, you lose!\n")
                    play_game()
                else:
                    print(f"{hands_description(hands, "User")}")
            while calculate(hands, "Computer") < 17:
                deal(hands, "Computer")
                if calculate(hands, "Computer") == 21:
                    print(f"{hands_description(hands, "Computer")}\nComputer got a blackjack. You lose!\n")
                    play_game()
                elif calculate(hands, "Computer") > 21:
                    print(f"{hands_description(hands, "Computer")}\nComputer went over, You win!\n")
                    play_game()
            if calculate(hands, "User") == 21:
                print(f"{hands_description(hands, "Computer")}\nYou got 21, You win!\n")
                play_game()
            elif calculate(hands, "User") < calculate(hands, "Computer"):
                print(f"{hands_description(hands, "Computer")}\nYou lose!\n")
                play_game()
            elif calculate(hands, "User") > calculate(hands, "Computer"):
                print(f"{hands_description(hands, "Computer")}\nYou win!\n")
                play_game()
            else:
                print(f"{hands_description(hands, "Computer")}\nIt's a draw!\n")
                play_game()

play_game()


