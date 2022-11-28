#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
print(logo)

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")

choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
if choice == "easy":
  attempts = 10
else:
  attempts = 5

number = random.randint(1,100)
# to test 
print(number)

should_continue = True
while attempts > 0 and should_continue:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess > number:
    print("Too high")
    print("Guess again")
    attempts -= 1
  elif guess < number:
    print("Too low")
    print("Guess again")
    attempts -= 1
  else:
    print("You guessed the right number.")
    should_continue = False
