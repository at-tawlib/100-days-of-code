# get contents of starting_letter
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

names = []
# get names into names list
with open("./Input/Names/invited_names.txt") as file:
    contents = file.readlines()
    for line in contents:
        names.append(line.rstrip())

# create letter for each name
for name in names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(letter.replace("[name]", name))
