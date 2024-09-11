import random

# Example bot that will make a random move each frame
class RandomBot:
    def __init__(self):
        pass
    def decide_move(self, board, turn):
        # Return column from 0 to 6.
        return random.randint(0, 6)
    