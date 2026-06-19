import pandas

alpha_df = pandas.read_csv("nato_phonetic_alphabet.csv")

alpha_dict = {row.letter:row.code for (index,row) in alpha_df.iterrows()}
print(alpha_dict)

word = input("Type a word: ").upper()
alpha_list = [alpha_dict[letter] for letter in word]

print(alpha_list)

