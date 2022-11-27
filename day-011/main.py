import random
from art import logo
#from replit import clear

# returns a random card from the deck
def deal_card():
  """returns a random card from deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#takes a List of cards as input and returns the score. 
def calculate_score(cards):
  """takes list of cards and return the sum"""
  # check for a blackjack (a hand with only 2 cards and sum 21) and return 0
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  # check for ace(11) if score greater than 21 i.e. replace it with 1
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)  
  return sum(cards)

def compare(user_score, computer_score):
  """compares user and computer score"""
  if user_score == computer_score:
    return "Draw "
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Opponent went over. You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"

def play_game():
  
  print(logo)
  
  user_cards = []
  computer_cards = []
  is_game_over = False
  # deal two cards for both user and computer
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    #calculate score
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's first card: {computer_cards[0]}")
    
    # If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends else ask user to continue the game
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
      print("Game Over")
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  # computer plays now
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"  Your final hand:       {user_cards}, final score: {user_score}")
  print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))



while input("Do you want to play a game of Blackjack? Type 'y' o 'n':  ") == "y" :
  #clear()
  play_game()
