##  Project - Hangman game

## Start
 1. Randomly choose a word from the word_list and assign it to a variable called chosen_word.
 2. Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
 3. Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
 4. Create an empty List called display.

> For each letter in the chosen_word, add a " _ " to 'display'.
> So if the chosen_word was "apple", 
> display should be [" _ ",  " _ ",  " _ ",  " _ ",  " _ "] with 5 " _ " representing each letter to guess.
 5.  Loop through each position in the chosen_word;
 > If the letter at that position matches 'guess' then reveal that letter
> in the display at that position. 
> e.g. If the user guessed "p" and the
> chosen word was "apple", then display should be [" _ ", "p", "p", " _ ", " _ "].
 6.  Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
 
 ## Intermediate
 1. Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks (" _ "). Then you can tell the user they've won.
> Check if there are no more " _ " left in 'display'. 
> Then all letters have been guessed.
 2. Create a variable called 'lives' to keep track of the number of lives left. 
 3. If guess is not a letter in the chosen_word
 >     Then reduce 'lives' by 1. 
 >     If lives goes down to 0 then the game should stop and it should print "You lose."
 4. print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

## Advance

 1. Update the word list to use the 'word_list' from hangman_words.py
 2. Import the stages from hangman_art.py and make this error go away.
 3. Import the logo from hangman_art.py and print it at the start of the game.
 4. If the user has entered a letter they've already guessed, print the letter and let them know.
 5. If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
