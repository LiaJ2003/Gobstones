class Player:
    def __init__(self, marbles):
        self.marbles = marbles
        self.points = 0

    def throwMarble(self):
        #chooses which marble to throw
        for mIndex in range(len(self.marbles)):
            curMarble = self.marbles[mIndex]
            #if there's a marble that should be moving, then this would 
            #return the coordinate of the marble to be focused on
            if curMarble.chosen:
                return (curMarble.x, curMarble.y)
        #otherwise, nothing should be moving!
        return None
