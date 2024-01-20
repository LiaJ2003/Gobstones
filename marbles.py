from buttons import Button
import copy
class Marble():
    def __init__(self, x, y, radius, team):
        self.x = x
        self.y = y
        self.radius = radius
        self.team = team
        self.angle = 0
        self.speed = 0
        self.chosen = False
        self.collide = False
        self.dragging = False
        self.confirm = False #to confirm location
        self.confirmButton = Button(x, y, 60, 30)
        self.launching = False
        self.move = False #when it's moving on onStep (animation)
        self.used = False #cannot be used again
        self.done = False
        self.putBack = False
        self.stop = False
        self.alive = True

    def isChosen(self, mX, mY):
        if mX <= self.x+self.radius and mX >= self.x-self.radius:
            if mY <= self.y+self.radius and mY >= self.y-self.radius:
                return True
        return False
    
    # def getNewSpeed(self):
    #     #have set acceleration
    #     return self.speed

    def distance_from_x(self, x, mouseX):
        return abs(mouseX - x)

    def distance_from_y(self, y, mouseY):
        return abs(mouseY -y)

    def getClosest(self, options, distance_function, target):
        min_option = options[0]
        min_distance = distance_function(min_option, target)

        copied = copy.deepcopy(options)
        for option in copied:
            distance = distance_function(option, target)
            if distance < min_distance:
                min_option = option
                min_distance = distance

        return min_option

    def getClosestSide(self, mouseX, mouseY, app):
        xOptions = [420, 1080] #app.boardLeft+self.radius, app.boardLeft+app.boardWidth-app.radius
        yOptions = [70, 730] #app.boardTop+self.radius, app.boardTop+app.boardHeight-app.radius

        closestX = self.getClosest(xOptions, self.distance_from_x, mouseX)
        closestY = self.getClosest(yOptions, self.distance_from_y, mouseY)

        if abs(mouseX - closestX) < abs(mouseY - closestY):
            self.x = closestX
            self.y = max(70, min(730, mouseY))
        else:
            self.x = max(420, min(1080, mouseX))
            self.y = closestY


    def updatePosition(self, mouseX, mouseY, app):
        if self.dragging:
            self.getClosestSide(mouseX, mouseY, app)

    def __repr__(self):
        return f"Marble at {self.x},{self.y} with {self.angle} degrees"
    



