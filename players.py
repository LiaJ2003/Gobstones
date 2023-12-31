class Player:
    def __init__(self, marbles):
        self.marbles = marbles
        self.points = 0

    def throwMarble(self):
        marble = self.marbles[0]
        