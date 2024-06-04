# Higher or Lower

import random  #type: ignore
from replit import clear
from art import logo, vs
from game_data import data

def formatter(choice):
  """format generated data"""
  name = choice['name']
  desc = choice['description']
  country = choice['country']
  return f"{name}, a {desc}, from {country}"

# Compare A vs B
def compare(a, b, answer):
  a = a['follower_count']
  b = b['follower_count']
  if a > b:
    return answer == 'a'
  else:
    return answer == 'b'
    
def game():
  print(logo)
  score = 0
  a = random.choice(data)
  b = random.choice(data)
  checker = False
  continue_game = True
  while continue_game:
    if checker:
      # B becomes A. New B appears after first round
      a = b
      b = random.choice(data)
    while a == b:
      b = random.choice(data)
    
    print(f"Compare A: {formatter(a)}")
    print(vs)
    print(f"Against B: {formatter(b)}")
    answer = input("Who has more followers? Type 'A' or 'B'. ").lower()
  
    clear()
    
    checker = compare(a, b, answer)
    # If correct show score or add a point
    if checker:
      score += 1
      print(f"Your current score is {score}.")
    else:
      print(f"Final score is {score}.")
      continue_game = False
  # Restart game?
  restart_game = input("Play again? 'y' or 'n': ").lower()
  if restart_game == 'y':
    clear()
    game()

game()