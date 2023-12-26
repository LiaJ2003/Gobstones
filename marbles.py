class Marble():
    def __init__(self, x, y, radius, team):
        self.x = x
        self.y = y
        self.radius = radius
        self.team = team
        self.energy = 0
        self.speed = 0
        self.chosen = False
        self.collide = False

    def isChosen(self, mX, mY):
        if mX <= self.x+self.radius and mX >= self.x-self.radius:
            if mY <= self.y+self.radius and mY >= self.y-self.radius:
                return True
        return False
    
    def getNewSpeed(self):
        #have set acceleration
        return self.speed
