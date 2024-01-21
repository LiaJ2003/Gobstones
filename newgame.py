from cmu_graphics import *
import math
import time
from marbles import Marble
from buttons import Button

def newgame_onAppStart(app):
    print('In newgame_onAppStart')
    buttons(app)
    players(app)
    marbles(app)

    app.gameOver = False
    app.winner = None
    app.p1Turn = True
    app.turnCount = 0

    app.playingMarble = None

    app.boardLeft = 400
    app.boardTop = 50
    app.boardWidth = 700
    app.boardHeight = 700

    app.mouseX = 0
    app.mouseY = 0
    app.marblesToRemove = []

    app.length = None

    app.drawWinStage = False
    app.dead = None
    app.deadCount = 0

    app.p1Score = 0
    app.p2Score = 0
def newgame_onScreenActivate(app):
    print('In newgame_onScreenActivate')

def players(app):
    #player 1
    app.player1Name = "Player 1"
    app.player1MarbleNum = 4

    #player 2
    app.player2Name = "Player 2"
    app.player2MarbleNum = 4


def marbles(app):
    # player 1 marbles
    player1X = 340
    radius = 15  
    app.p1m1 = Marble(player1X, 100, radius, app.player1Name)
    app.p1m2 = Marble(player1X, 150, radius, app.player1Name)
    app.p1m3 = Marble(player1X, 200, radius, app.player1Name)
    app.p1m4 = Marble(player1X, 250, radius, app.player1Name)

    app.player1M = [app.p1m1, app.p1m2, app.p1m3, app.p1m4]

    # player 2 marbles
    player2X = 1160 
    app.p2m1 = Marble(player2X, 100, radius, app.player2Name)
    app.p2m2 = Marble(player2X, 150, radius, app.player2Name)
    app.p2m3 = Marble(player2X, 200, radius, app.player2Name)
    app.p2m4 = Marble(player2X, 250, radius, app.player2Name)

    app.player2M = [app.p2m1, app.p2m2, app.p2m3, app.p2m4]

    # total marbles
    app.marbles = app.player1M + app.player2M


def buttons(app):
    app.homeB = Button(10, 10, 60, 30)
    
def drawConfirmButton(app, marbleList):
    for marble in marbleList:
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
        drawCircle(marble.x, marble.y, marble.radius, fill = app.p1Color)
    
    drawLabel(app.player2Name, app.width-220, 60, size=30, fill = app.p2Color, font="cinzel")
    for marble in app.player2M:
        drawCircle(marble.x, marble.y, marble.radius, fill = app.p2Color)

def drawBoard(app):
    drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
             fill=None, border="black", borderWidth=2)

def drawLaunch(app):
    for marble in app.marbles:
        if marble.launching:
                # draw the launching dots
                directionX = marble.x - app.mouseX
                directionY = marble.y - app.mouseY
                if marble.confirm:
                    length = distance(directionX, directionY)
                    spacedDirectionX = directionX / length
                    spacedDirectionY = directionY / length

                    stepSize = length / 11  

                    for i in range(1, 11):
                        circleX = marble.x + i * stepSize * spacedDirectionX
                        circleY = marble.y + i * stepSize * spacedDirectionY
                        drawCircle(circleX, circleY, 5, fill="lightgrey")  

def drawWinner(app):
    drawRect(app.width//2, app.height//2, 400, 100, align = 'center', border = "black", fill = "white")
    if app.winner == True:
        drawLabel("Player 1 Wins", 750, app.height//2, size = 50, font = 'cinzel', fill = app.p1Color)
    elif app.winner == False:
        drawLabel("Player 2 Wins", 750,  app.height//2, size = 50, font = 'cinzel', fill = app.p2Color)
    else:
        drawLabel("It's a Tie", 750,  app.height//2, size = 50, font = 'cinzel', fill = "black")
    drawLabel(f"Points: {app.p1Score}", 160, 130, size = 20, fill = "black", font = "cinzel")
    drawLabel(f"Points: {app.p2Score}", app.width-220, 130, size = 20, fill = "black", font = "cinzel")
    

def newgame_redrawAll(app):
    
    drawSnakeGame(app)
    drawMarbles(app)
    drawBoard(app)
    #drawConfirmButton(app)
    drawLaunch(app)
    
    #homeB
    drawRect(app.homeB.x, app.homeB.y, app.homeB.width, app.homeB.height,
             fill = None, border = "black", borderWidth = 2)
    drawLabel('Home', 20, 25, size = 15, font = 'cinzel', align = 'left')

    #player turn
    if app.p1Turn: 
        drawLabel("Player 1's Turn", 750, 25, size = 25, font = 'cinzel', fill = app.p1Color)
        drawConfirmButton(app, app.player1M)
    else:
        drawLabel("Player 2's Turn", 750, 25, size = 25, font = 'cinzel', fill = app.p2Color)
        drawConfirmButton(app, app.player2M)

    if app.gameOver:
        drawWinner(app)

def newgame_onMousePress(app, mouseX, mouseY):
    if app.homeB.isClicked(mouseX, mouseY):
        setActiveScreen('home')
    if app.p1Turn:
        chooseAndConfirm(mouseX, mouseY, app.player1M, app)
    else:
        chooseAndConfirm(mouseX, mouseY, app.player2M, app)

def chooseAndConfirm(mouseX, mouseY, marbleList, app):
    for marble in marbleList:
        if (marble.isChosen(mouseX, mouseY) and marble.confirm == False and 
            (app.playingMarble == None or app.playingMarble == marble) and not marble.used):
                marble.dragging = True
                marble.chosen = True
                app.playingMarble = marble
        if marble.confirmButton.isClicked(mouseX, mouseY) and marble.chosen and marble.confirm == False and not marble.used:
            marble.confirm = True
            
def distance(x, y):
    return ((x ** 2) + (y ** 2)) ** 0.5

def newgame_onMouseDrag(app, mouseX, mouseY):
    for marble in app.marbles:
        if marble.dragging and not marble.used:
            marble.updatePosition(mouseX, mouseY, app)
        if marble.confirm and not marble.used and not marble.dragging:
            marble.launching = True
            app.mouseX = mouseX
            app.mouseY = mouseY
            #print(f"{app.mouseX}, {app.mouseY}")

def newgame_onMouseRelease(app, mouseX, mouseY):
    for marble in app.marbles:
        if marble.dragging:
            marble.dragging = False
        if marble.launching:
            marble.move = True
            marble.used = True
            app.p1Turn = not app.p1Turn
            app.turnCount += 1
            marble.launching = False

            directionX = marble.x - app.mouseX
            directionY = marble.y - app.mouseY

            if marble.confirm:

                length = distance(directionX, directionY)
            
                #SET SPEED MULTIPLIER
                marble.speed = length * 0.05  
                marble.angle = math.atan2(directionY, directionX)

    app.playingMarble = None


def newgame_onStep(app):
    for marble in app.marbles:
        marble.collide = False 
        if marble.move:
            recursiveCollisions(marble, app)
    

    allMarblesUsed = True
    for marble in app.marbles:
        if not marble.used:
            allMarblesUsed = False
            break

    # Check if none of the marbles are moving
    noMovingMarbles = True
    for marble in app.marbles:
        if marble.move:
            noMovingMarbles = False
            break

    if allMarblesUsed and noMovingMarbles and not app.gameOver:
        app.gameOver = True
        decideWinner(app)
        print(app.p1Score)
        print(app.p2Score)
        if app.p1Score > app.p2Score:
            app.winner = True
        elif app.p1Score < app.p2Score:
            app.winner = False
        else:
            app.winner = None

def decideWinner(app):
    for marble in app.player1M:
        if ((marble.x - app.boardLeft - app.boardWidth // 2) ** 2 + 
        (marble.y - app.boardTop - app.boardHeight // 2) ** 2 <= 100 ** 2):
            app.p1Score += 100
        elif((marble.x - app.boardLeft - app.boardWidth // 2) ** 2 + 
        (marble.y - app.boardTop - app.boardHeight // 2) ** 2 <= 200 ** 2):
            app.p1Score += 50     
        else: #wihtin largest one
            app.p1Score += 10
    
    for marble in app.player2M:
        if ((marble.x - app.boardLeft - app.boardWidth // 2) ** 2 + 
        (marble.y - app.boardTop - app.boardHeight // 2) ** 2 <= 100 ** 2):
            app.p2Score += 100
        elif((marble.x - app.boardLeft - app.boardWidth // 2) ** 2 + 
        (marble.y - app.boardTop - app.boardHeight // 2) ** 2 <= 200 ** 2):
            app.p2Score += 50     
        else: #wihtin largest one
            app.p2Score += 10
                


def recursiveCollisions(marble, app, recursion_count=0, max_recursion=5):
    hitMarble = checkMarbleCollision(marble, app)
    
    if hitMarble is not None and marble.collide:
        marble.move = False

        hitMarble.chosen = True
        hitMarble.move = True
        hitMarble.speed = marble.speed
        hitMarble.angle = marble.angle

        time.sleep(0.5) 

        recursiveCollisions(hitMarble, app, recursion_count + 1, max_recursion)
    else:
        executeMarbleMove(marble, app)
        #print("no collisions")

  
def executeMarbleMove(marble, app):
    marble.x += marble.speed * math.cos(marble.angle)
    marble.y += marble.speed * math.sin(marble.angle)
    
    ##  KEEPING FOR NOW BUT NO LONGER NEEDED

    #inner hole
    if ((marble.x - app.boardLeft - app.boardWidth // 2) ** 2 + 
    (marble.y - app.boardTop - app.boardHeight // 2) ** 2 <= 50 ** 2):
        app.deadCount += 1
        app.marblesToRemove.append(marble)
        removeMarble(app, marble)


    #SPEED DECAY
    if marble.alive:
        marble.speed *= 0.97  

    if marble.speed < 0.5:
        marble.move = False
        marble.chosen = False
        marble.speed = 0
        marble.done = True

        # SAME FOR HERE

        if ((marble.x - app.boardLeft - app.boardWidth // 2) ** 2 + 
        (marble.y - app.boardTop - app.boardHeight // 2) ** 2 >= 300 ** 2):
            app.deadCount += 1
            app.marblesToRemove.append(marble)
            removeMarble(app, marble)

def removeMarble(app, marble):
    if not app.p1Turn:
        app.player1M.remove(marble)
    else:
        app.player2M.remove(marble)
    app.marbles.remove(marble)


def checkMarbleCollision(M, app):
    if M.collide: 
        return None

    for marble in app.marbles:
        if marble is not M and not marble.collide:
            length = distance((marble.x - M.x), (marble.y - M.y))
            combinedRadius = marble.radius + M.radius
            #print(f"checking collision: ({marble.x}, {marble.y})")

            if length < combinedRadius:
                marble.collide = True
                M.collide = True
                print(f"collided!")
                return marble
    return None