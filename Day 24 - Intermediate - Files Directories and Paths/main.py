with open("Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        name = name.strip()
        with open("Input/Letters/starting_letter.txt") as letter:
            modified_letter = letter.read()
            modified_letter = modified_letter.replace("[name]", name)
        with open(f"Output/ReadyToSend/{name}.txt", mode="w") as new_letter:
           new_letter.write(modified_letter)