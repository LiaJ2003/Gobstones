from cmu_graphics import *
from marbles import Marble
from buttons import Button

def newgame_onAppStart(app):
    print('In newgame_onAppStart')
    buttons(app)
    players(app)
    marbles(app)

def newgame_onScreenActivate(app):
    print('In newgame_onScreenActivate')

def players(app):
    #player 1
    app.player1Name = "Player 1"

    #player 2
    app.player2Name = "Player 2"


def marbles(app):
    #player 1 marbles
    app.p1m1 = Marble(60, 120, 25, app.player1Name)
    app.p1m2 = Marble(60, 230, 25, app.player1Name)
    app.p1m3 = Marble(60, 340, 25, app.player1Name)
    app.p1m4 = Marble(60, 450, 25, app.player1Name)

    app.player1M = [app.p1m1, app.p1m2, app.p1m3, app.p1m4]
    
    #player 2 marbles
    app.p2m1 = Marble(app.width-110, 120, 25, app.player2Name)
    app.p2m2 = Marble(app.width-110, 230, 25, app.player2Name)
    app.p2m3 = Marble(app.width-110, 340, 25, app.player2Name)
    app.p2m4 = Marble(app.width-110, 450, 25, app.player2Name)

    app.player2M = [app.p2m1, app.p2m2, app.p2m3, app.p2m4]

    #total marbles
    app.marbles = app.player1M + app.player2M

def buttons(app):
    #add home button
    return

def drawSnakeGame(app):
    drawCircle(app.width//2, app.height//2, 300, fill = None, border = "black")
    drawCircle(app.width//2, app.height//2, 200, fill = None, border = "black")
    drawCircle(app.width//2, app.height//2, 100, fill = None, border = "black")

def drawMarbles(app):
    drawLabel(app.player1Name, 160, 60, size=30, fill = app.p1Color, font="cinzel")
    for marble in app.player1M:
        drawCircle(marble.x, marble.y, marble.radius, fill = app.p1Color)
    
    drawLabel(app.player2Name, app.width-220, 60, size=30, fill = app.p2Color, font="cinzel")
    for marble in app.player2M:
        drawCircle(marble.x, marble.y, marble.radius, fill = app.p2Color)

def newgame_redrawAll(app):
    drawSnakeGame(app)
    drawMarbles(app)
