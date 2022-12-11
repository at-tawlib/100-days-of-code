student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# 1. Create a dictionary in this format:  {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_letter = data.letter.to_list()
nato_code = data.code.to_list()
nato_dict = {}
i = 0
for letter in nato_letter:
    nato_dict[letter] = nato_code[i]
    i += 1
# 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
split_word = []
split_word[:0] = word
nato_final = []
for char in split_word:
    nato_final.append(nato_dict[char.upper()])
print(nato_final)
