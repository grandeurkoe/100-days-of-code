import pandas

nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_data.iterrows()}

word_input = input("Enter a word: ").upper()
word_letter = list(word_input)

nato_word_list = [nato_alphabet_dict[letter] for letter in word_letter if letter in nato_alphabet_dict.keys()]
print(nato_word_list)
