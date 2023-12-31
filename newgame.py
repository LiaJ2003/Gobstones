from cmu_graphics import *
import math
from marbles import Marble
from buttons import Button

def newgame_onAppStart(app):
    print('In newgame_onAppStart')
    buttons(app)
    players(app)
    marbles(app)

    app.gameOver = False
    app.p1Turn = True
    #app.p2Turn = False
    app.playingMarble = None

    app.boardLeft = 400
    app.boardTop = 50
    app.boardWidth = 700
    app.boardHeight = 700

    app.mouseX = 0
    app.mouseY = 0
    app.marblesToRemove = []

def newgame_onScreenActivate(app):
    print('In newgame_onScreenActivate')

def players(app):
    #player 1
    app.player1Name = "Player 1"

    #player 2
    app.player2Name = "Player 2"


def marbles(app):
    # player 1 marbles
    player1X = 60  
    app.p1m1 = Marble(player1X, 120, 20, app.player1Name)
    app.p1m2 = Marble(player1X, 230, 20, app.player1Name)
    app.p1m3 = Marble(player1X, 340, 20, app.player1Name)
    app.p1m4 = Marble(player1X, 450, 20, app.player1Name)

    app.player1M = [app.p1m1, app.p1m2, app.p1m3, app.p1m4]

    # player 2 marbles
    player2X = app.width - 150 #kept going off the screen for me
    app.p2m1 = Marble(player2X, 120, 20, app.player2Name)
    app.p2m2 = Marble(player2X, 230, 20, app.player2Name)
    app.p2m3 = Marble(player2X, 340, 20, app.player2Name)
    app.p2m4 = Marble(player2X, 450, 20, app.player2Name)

    app.player2M = [app.p2m1, app.p2m2, app.p2m3, app.p2m4]

    # total marbles
    app.marbles = app.player1M + app.player2M


def buttons(app):
    app.homeB = Button(10, 10, 60, 30)
    
def drawConfirmButton(app):
    for marble in app.marbles:
        if marble.confirm == False and marble.dragging == False and marble.chosen:
            marble.confirmButton.x = marble.x - 30  # Adjust the position as needed
            marble.confirmButton.y = marble.y + marble.radius + 10  # Adjust the position as needed
            drawRect(marble.confirmButton.x, marble.confirmButton.y,
                     marble.confirmButton.width, marble.confirmButton.height,
                     fill="lightgreen", border="black")
            labelX = marble.confirmButton.x + marble.confirmButton.width / 2
            labelY = marble.confirmButton.y + marble.confirmButton.height / 2
            drawLabel("Confirm", labelX, labelY,
                      size=12, font="cinzel")


def drawSnakeGame(app):
    drawCircle(app.boardLeft + app.boardWidth // 2, app.boardTop + app.boardHeight // 2, 300, fill=None, border="black")
    drawCircle(app.boardLeft + app.boardWidth // 2, app.boardTop + app.boardHeight // 2, 200, fill=None, border="black")
    drawCircle(app.boardLeft + app.boardWidth // 2, app.boardTop + app.boardHeight // 2, 100, fill=None, border="black")
    drawCircle(app.boardLeft + app.boardWidth // 2, app.boardTop + app.boardHeight // 2, 50, fill='black', border="black")

def drawMarbles(app):
    drawLabel(app.player1Name, 160, 60, size=30, fill = app.p1Color, font="cinzel")
    for marble in app.player1M:
        if marble not in app.marblesToRemove:
            drawCircle(marble.x, marble.y, marble.radius, fill = app.p1Color)
    
    drawLabel(app.player2Name, app.width-220, 60, size=30, fill = app.p2Color, font="cinzel")
    for marble in app.player2M:
        if marble not in app.marblesToRemove:
            drawCircle(marble.x, marble.y, marble.radius, fill = app.p2Color)

def drawBoard(app):
    drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
             fill=None, border="black", borderWidth=2)

def drawInnerBoard(app):
    innerBoardLeft = app.boardLeft + 2 * app.p1m1.radius
    innerBoardTop = app.boardTop + 2 * app.p1m1.radius

    drawRect(innerBoardLeft, innerBoardTop,
             app.boardWidth - 4 * app.p1m1.radius, app.boardHeight - 4 * app.p1m1.radius,
             fill=None, border="black", borderWidth=2)

def drawLaunch(app):
    for marble in app.marbles:
        # if marble.confirm and marble.launching == False and marble.move == False:
        #     labelX = marble.confirmButton.x + marble.confirmButton.width / 2
        #     labelY = marble.confirmButton.y + marble.confirmButton.height / 2
        #     drawLabel("Click and drag to launch!", labelX, labelY,
        #             size=12, font="cinzel")
        if marble.launching:
                # draw the launching dots
                directionX = marble.x - app.mouseX
                directionY = marble.y - app.mouseY
                length = ((directionX ** 2) + (directionY ** 2)) ** 0.5
                spacedDirectionX = directionX / length
                spacedDirectionY = directionY / length

                stepSize = length / 11  

                for i in range(1, 11):
                    circleX = marble.x + i * stepSize * spacedDirectionX
                    circleY = marble.y + i * stepSize * spacedDirectionY
                    drawCircle(circleX, circleY, 5, fill="lightgrey")  



def newgame_redrawAll(app):
    drawSnakeGame(app)
    drawMarbles(app)
    drawBoard(app)
    #drawInnerBoard(app)
    drawConfirmButton(app)
    drawLaunch(app)
    
    #homeB
    drawRect(app.homeB.x, app.homeB.y, app.homeB.width, app.homeB.height,
             fill = None, border = "black", borderWidth = 2)
    drawLabel('Home', 20, 25, size = 15, font = 'cinzel', align = 'left')

    #player turn
    if app.p1Turn: 
        drawLabel("Player 1's Turn", 800, 25, size = 25, font = 'cinzel', fill = app.p1Color)
    else:
        drawLabel("Player 2's Turn", 800, 25, size = 25, font = 'cinzel', fill = app.p2Color)
    
def newgame_onMousePress(app, mouseX, mouseY):
    if app.homeB.isClicked(mouseX, mouseY):
        setActiveScreen('home')
    if app.p1Turn:
        for marble in app.player1M:
            #if it's used it can't be used again
            if (marble.isChosen(mouseX, mouseY) and marble.confirm == False and 
            (app.playingMarble == None or app.playingMarble == marble) and not marble.used):
                marble.dragging = True
                marble.chosen = True
                app.playingMarble = marble
            if marble.confirmButton.isClicked(mouseX, mouseY) and marble.chosen:
                marble.confirm = True
    else:
        for marble in app.player2M:
            #if it's used it can't be used again
            if (marble.isChosen(mouseX, mouseY) and marble.confirm == False and 
            (app.playingMarble == None or app.playingMarble == marble) and not marble.used):
                marble.dragging = True
                marble.chosen = True
                app.playingMarble = marble
            if marble.confirmButton.isClicked(mouseX, mouseY) and marble.chosen:
                marble.confirm = True

    
            

def newgame_onMouseDrag(app, mouseX, mouseY):
    for marble in app.marbles:
        if marble.dragging and not marble.used:
            marble.updatePosition(mouseX, mouseY, app)
        if marble.confirm and not marble.used:
            marble.launching = True
            app.mouseX = mouseX
            app.mouseY = mouseY
            print(f"{app.mouseX}, {app.mouseY}")

def newgame_onMouseRelease(app, mouseX, mouseY):
    for marble in app.marbles:
        if marble.dragging:
            marble.dragging = False
        if marble.launching:
            marble.launching = False
            marble.move = True
            marble.used = True
            app.p1Turn = not app.p1Turn

            directionX = marble.x - app.mouseX
            directionY = marble.y - app.mouseY

            length = ((directionX ** 2) + (directionY ** 2)) ** 0.5
            spacedDirectionX = directionX / length
            spacedDirectionY = directionY / length
            
            #SET SPEED MULTIPLIER
            marble.speed = length * 0.05  
            marble.angle = math.atan2(spacedDirectionY, spacedDirectionX)
    app.playingMarble = None

def newgame_onStep(app):
    for marble in app.marbles:
        if marble.move:
            marble.x += marble.speed * math.cos(marble.angle)
            marble.y += marble.speed * math.sin(marble.angle)

            #check if marble is outside of board
            if (marble.x < app.boardLeft or marble.x > app.boardLeft + app.boardWidth or
                marble.y < app.boardTop or marble.y > app.boardTop +app.boardHeight):
                app.marblesToRemove.append(marble)
            if ((marble.x - app.boardLeft - app.boardWidth // 2) ** 2 + 
            (marble.y - app.boardTop - app.boardHeight // 2) ** 2 <= 50 ** 2):
                app.marblesToRemove.append(marble)

            #SPEED DECAY
            marble.speed *= 0.97  

            if marble.speed < 0.5:
                marble.move = False
                marble.chosen = False
                marble.speed = 0

