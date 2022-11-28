#my own version
import art
import random
from game_data import data
#from replit import clear

print(art.logo)

questions = data
# dictionary keys
name = "name"
follower_count = "follower_count"
description = "description"
country = "country"

# selects random question from the list
def select_question():
  """returns randomly selected item from the list"""
  question = random.choice(questions)
  return question

def set_string(question):
  """takes a dictionary item from the list and returns a string of the data"""
  return f"{question[name]}, {question[description]}, {question[country]}."

def check_answer(question_A, question_B):
  """takes questions and return the one with highest follower count"""
  if question_A[follower_count] > question_B[follower_count]:
    return question_A
  elif question_B[follower_count] > question_A[follower_count]:
    return question_B
  else:
    return "Invalid selection"

    
# sets the questions

def play_game():
  score = 0
  question_A = select_question()
  question_B = select_question()
  should_continue = True
  print(art.logo)
  
  while should_continue:
    print(f"Compare A: {set_string((question_A))}")
    print(art.vs)
    print(f"Against B: {set_string(question_B)}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower() 
    if answer == "a":
      answer =  question_A
    elif answer == "b":
      answer =  question_B
    
    #clear()
    print(art.logo) 
    
    if answer == check_answer(question_A, question_B):
      score += 1
      print(f"You're right! Current score: {score}.")
      question_A = answer
      question_B = select_question()
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      should_continue = False

###########################################3
play_game()
