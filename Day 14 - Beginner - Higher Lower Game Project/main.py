import random
import art
from game_data import data

print(art.logo)
current_item = random.choice(data)
score = 0
hit = True

def compare_items(followers_a, followers_b, a_or_b):
    if a_or_b == "A":
        if followers_a > followers_b:
            return True
        else:
            return False
    elif a_or_b == "B":
        if followers_b > followers_a:
            return True
        else:
            return False
    else:
        return False

while hit:
    print(f"Compare A: {current_item["name"]}, a {current_item["description"]}, from {current_item["country"]}")
    print(art.vs)
    next_item = random.choice(data)
    print(f"Against B: {next_item["name"]}, a {next_item["description"]}, from {next_item["country"]}")
    choice = input("Who has more Followers? Type 'A' or 'B'").upper()
    hit = compare_items(current_item["follower_count"], next_item["follower_count"], choice)
    if hit:
        score += 1
        print("\n" * 20)
        print(art.logo)
        print(f"You're right! Current score: {score}")
        current_item = next_item
    else:
        print(f"Sorry that's wrong! Final Score: {score}")



