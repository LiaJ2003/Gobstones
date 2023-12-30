class Marbles():
    def __init__(self, x, y, radius, team):
        self.x = x
        self.y = y
        self.radius = radius 
        self.team = team
        self.collide = False

    def newLocation(self, newX, newY):
        self.x = newX
        self.y = newY

    def isChosen(self, mX, mY):
        if mX <= self.x+self.radius and mX >= self.x-self.radius:
            if mY <= self.y+self.radius and mY >= self.y-self.radius:
                self.chosen = True
                return True
        return False
    
