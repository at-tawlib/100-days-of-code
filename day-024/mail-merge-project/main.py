# get names into names list
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

# get contents of starting_letter
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    # create letter for each name
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as complete_letter:
            complete_letter.write(new_letter)
