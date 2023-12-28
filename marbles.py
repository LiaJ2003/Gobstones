from buttons import Button
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
        self.dragging = False
        self.confirm = False #to confirm location
        self.confirmButton = Button(x, y, 60, 30)

    def isChosen(self, mX, mY):
        if mX <= self.x+self.radius and mX >= self.x-self.radius:
            if mY <= self.y+self.radius and mY >= self.y-self.radius:
                return True
        return False
    
    def getNewSpeed(self):
        #have set acceleration
        return self.speed

    def updatePosition(self, mouseX, mouseY, app):
        if self.dragging:
            new_x = max(app.boardLeft + self.radius,
                        min(mouseX, app.boardLeft + app.boardWidth - self.radius))
            new_y = max(app.boardTop + self.radius,
                        min(mouseY, app.boardTop + app.boardHeight - self.radius))
            
            innerBoardLeft = (app.width - app.boardWidth + 4 * self.radius) // 2
            innerBoardTop = (app.height - app.boardHeight + 4 * self.radius) // 2
            innerBoardRight = innerBoardLeft + app.boardWidth - 4 * self.radius
            innerBoardBottom = innerBoardTop + app.boardHeight - 4 * self.radius

            if innerBoardLeft <= new_x <= innerBoardRight and innerBoardTop <= new_y <= innerBoardBottom:
                #no updating poition if its insider the inner board
                return

            self.x = new_x
            self.y = new_y