import random
import hangman_art

# import and get word_list from hangman_words.py
from hangman_words import word_list

word_list = word_list
# get a random word from the world_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
      
end_of_game = False
lives = 6   # set lives to six to match with the six stages

# Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
#Testing code, shows the word
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks to hold correct guesses
# add "_" for each letter in the chosen_word
display = []
for x in range(word_length):
    display += "_"

# to hold list of all entered words; prevent repetition of words
entered_words = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, let them know else add to entered_words
    if guess not in entered_words:
      entered_words += guess
    else:
      print("Word already guessed")

    # Check whether guessed letter is correct
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"{guess} is is not one of the words")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])
