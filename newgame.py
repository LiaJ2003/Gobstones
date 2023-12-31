from cmu_graphics import *
from marbles import Marble
from buttons import Button

def newgame_onAppStart(app):
    print('In newgame_onAppStart')
    buttons(app)
    players(app)
    marbles(app)

    app.gameOver = False
    app.p1Turn = True
    app.p2Turn = False

    app.boardLeft = 400
    app.boardTop = 50
    app.boardWidth = 700
    app.boardHeight = 700

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
    app.p1m1 = Marble(player1X, 120, 25, app.player1Name)
    app.p1m2 = Marble(player1X, 230, 25, app.player1Name)
    app.p1m3 = Marble(player1X, 340, 25, app.player1Name)
    app.p1m4 = Marble(player1X, 450, 25, app.player1Name)

    app.player1M = [app.p1m1, app.p1m2, app.p1m3, app.p1m4]

    # player 2 marbles
    player2X = app.width - 150 #kept going off the screen for me
    app.p2m1 = Marble(player2X, 120, 25, app.player2Name)
    app.p2m2 = Marble(player2X, 230, 25, app.player2Name)
    app.p2m3 = Marble(player2X, 340, 25, app.player2Name)
    app.p2m4 = Marble(player2X, 450, 25, app.player2Name)

    app.player2M = [app.p2m1, app.p2m2, app.p2m3, app.p2m4]

    # total marbles
    app.marbles = app.player1M + app.player2M


def buttons(app):
    app.homeB = Button(10, 10, 60, 30)
    
def drawConfirmButton(app):
    #confirming to make sure that player wants to place here
    for marble in app.marbles:
        if marble.confirm == False and marble.dragging == False and marble.chosen:
            marble.confirmButton.x = marble.x - 30  
            marble.confirmButton.y = marble.y + marble.radius + 10 
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

#drawing board boundaries to click into later
def drawInnerBoard(app):
    innerBoardLeft = app.boardLeft + 2 * app.p1m1.radius
    innerBoardTop = app.boardTop + 2 * app.p1m1.radius

    drawRect(innerBoardLeft, innerBoardTop,
             app.boardWidth - 4 * app.p1m1.radius, app.boardHeight - 4 * app.p1m1.radius,
             fill=None, border="black", borderWidth=2)



def newgame_redrawAll(app):
    drawSnakeGame(app)
    drawMarbles(app)
    drawBoard(app)
    drawInnerBoard(app)
    
    for marble in app.marbles:
        if marble.checkConfirm:
            drawConfirmButton(app)
    
    #homeB
    drawRect(app.homeB.x, app.homeB.y, app.homeB.width, app.homeB.height,
             fill = None, border = "black", borderWidth = 2)
    drawLabel('Home', 20, 25, size = 15, font = 'cinzel', align = 'left')

def newgame_onMousePress(app, mouseX, mouseY):
    if app.homeB.isClicked(mouseX, mouseY):
        setActiveScreen('home')

    for marble in app.marbles:
        #checking if the marble is chosen
        if marble.isChosen(mouseX, mouseY):
            #if so, then marble should be able to be moved
            marble.dragging = True
            marble.moving = True
            #if not confirmed, then it's currently chosen/can still be moved
            if not marble.confirm and marble.inBoundary(app):
                marble.chosen = True
        else:
            marble.moving = False

        if (marble.confirmButton.isClicked(mouseX, mouseY) and marble.chosen):
            marble.confirm = True

# def newgame_onStep(app):
#     for marble in app.marbles:
#         if marble.confirm:
#             marble.moving = False

def newgame_onMouseDrag(app, mouseX, mouseY):
    for marble in app.marbles:
        marble.updatePosition(mouseX, mouseY, app)

def newgame_onMouseRelease(app, mouseX, mouseY):
    for marble in app.marbles:
        if marble.dragging:
            marble.checkConfirm = True
            marble.dragging = False
            
