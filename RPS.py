import random
from collections import defaultdict

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    # Initialize transition probabilities
    transition_matrix = defaultdict(lambda: {"R": 0, "P": 0, "S": 0})
    
    # Populate transition matrix based on history
    for i in range(len(opponent_history) - 1):
        current_move = opponent_history[i]
        next_move = opponent_history[i + 1]
        transition_matrix[current_move][next_move] += 1
    
    # Predict the next move
    if len(opponent_history) > 1:
        last_move = opponent_history[-1]
        predicted_move = max(transition_matrix[last_move], key=transition_matrix[last_move].get)
    else:
        predicted_move = random.choice(["R", "P", "S"])
    
    # Counter the predicted move
    ideal_response = {"R": "P", "P": "S", "S": "R"}
    return ideal_response[predicted_move]
