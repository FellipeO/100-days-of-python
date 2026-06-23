import pandas

alpha_df = pandas.read_csv("nato_phonetic_alphabet.csv")

alpha_dict = {row.letter:row.code for (index,row) in alpha_df.iterrows()}
print(alpha_dict)

def generate_phonetic():
    word = input("Type a word: ").upper()
    try:
        alpha_list = [alpha_dict[letter] for letter in word]
    except KeyError:
        print("That's not a word.")
        generate_phonetic()
    else:
        print(alpha_list)

generate_phonetic()