# Higher or Lower

import random  #type: ignore
from game_data import data


def generate_choice():
  """generate data"""
  a = random.choice(data)
  b = random.choice(data)
  if a == b:
    while a == b:
      b = random.choice(data)
  return a, b

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
  if answer == 'a':
    return a > b
  elif answer == 'b':
    return b > a
    
def game():
  score = 0
  checker = False
  select = generate_choice()
  a = select[0]
  b = select[1]
  while True:
    if checker:
      # B becomes A. New B appears
      a = b
      b = generate_choice()[1]
      while a == b:
        b = generate_choice()[1]
      
    print(f"Compare A: {formatter(a)}")
    print(f"Against B: {formatter(b)}")
    answer = input("Who has more followers? Type 'A' or 'B'. ").lower()
    checker = compare(a, b, answer)
    # If correct show score or add a point
    if checker:
      score += 1
    else:
      print(f"Your final score is {score}.")
      break
  
game()