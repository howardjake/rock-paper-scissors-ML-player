# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

# Note: This player function uses some pre-training with a randomized version of "quincy"'s algorithm and a Markov Model to win. You may need to increase the game iterations to get above 60% on "abbey". 

import random

def player(prev_play, opponent_history=[], play_order={}):

  # Pretrain our player using the "quincy" player algorithm
  counter = 0
  if not opponent_history:
    while True:
      counter += 1
      train_last_five = "".join(opponent_history[-5:])
      play_order[train_last_five] = play_order.get(train_last_five, 0) + 1
      choices = ["R", "R", "P", "P", "S", "S"]
      
      randomizer = bool(random.getrandbits(1))
      if randomizer:
        opponent_history.append(choices[counter % len(choices)])
      else:
        opponent_history.append(random.choice(choices))
        
      if counter == 1000:
        break

  # Options for next move
  poss_next = ['R', 'P', 'S']
  # Winning Args
  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

  # if There is no Previous Play set that to "R"
  if not prev_play:
    prev_play = 'R'
  # this is prediction for ops next move
  prediction = "S"

  # Add Prev play to opponents history
  opponent_history.append(prev_play)

  #Grab the last 5 plays
  last_five = "".join(opponent_history[-5:])
  # increment the count of that last_five move instance by one
  play_order[last_five] = play_order.get(last_five, 0) + 1

  # Create a list of the next possible outcomes ex. 'previous 4 plays + possible next'
  potential_plays = []
  for v in poss_next:
    potential_plays.append("".join([*opponent_history[-4:], v]))

  # Find those outcomes using our historical data in play_order
  sub_order = {}
  for k in potential_plays:
    if k in play_order:
      sub_order[k] = play_order[k]

  # Set our prediction to the most statiscally likely out of the available outcomes
  if sub_order:
    play_order[last_five] = play_order.get(last_five, 0) + 1
    prediction = max(sub_order, key=sub_order.get)[-1:]

  # Pick the most likely winnnig play
  guess = ideal_response[prediction]

  return guess
