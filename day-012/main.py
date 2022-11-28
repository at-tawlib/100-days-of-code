import random 
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS =  5

# function to check user's guess against actual answer
def check_answer(guess, answer, turns):
  """checks the answer against guess. Returns the numbe of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns -1 
  elif guess < answer:
    print("Too low.")
    return turns -1 
  else:
    print(f"You got it! The answer is {answer}")

# make function to set difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS


def game():
  print(logo)
  # choose a random number between 1 and 100    
  print("Welcome to the Number Guessing Game")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)
  print(f"Psst, the correct answer is {answer}")
  
  turns = set_difficulty()

  # repeat the guessing functionality if they get it wrong
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    # let the user guess a numbe
    guess = int(input("Make a guess: "))

    # track the numbe of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose. ")
      return
    elif guess != answer:
      print("Guess again. ")

########################
#start the game
game()
