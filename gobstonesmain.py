from cmu_graphics import *
from marbles import Marble
from button import Button

def onAppStart(app):
    app.start = False
    app.contPoss = False
    app.cont = False
    app.help = False
    app.settings = False
    buttons(app)
    players(app)
    marbles(app)

def players(app):
    #player 1
    app.player1Name = "Player 1"
    app.player1C = "red"

    #player 2
    app.player2Name = "Player 2"
    app.player2C = "blue"

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
    app.beginB = Button(550, 200, 500, 100)
    app.contB = Button(550, 350, 500, 100)
    app.helpB = Button(550, 500, 500, 100)
    app.settingsB = Button(550, 650, 500, 100)

def onMousePress(app, mouseX, mouseY):
    #initial game settings
    if app.beginB.isClicked(mouseX, mouseY):
        app.start = True
    if app.contB.isClicked(mouseX, mouseY) and app.contPoss:
        app.cont = True
    if app.helpB.isClicked(mouseX, mouseY):
        app.help = True
    if app.settingsB.isClicked(mouseX, mouseY):
        app.settings = True

    #when in game mode, checking to see if marble is being moved
    for marble in app.marbles:
        if marble.isChosen(mouseX, mouseY):
            marble.chosen = True

def onMouseDrag(app, mouseX, mouseY):

    return

def onKeyPress(app, key):
    if key == "r":
        app.start = False
        app.cont = False
        app.help = False
        app.settings = False

def drawStartScreen(app):
    drawLabel("Gobstones", 800, 100, size=80, font='cinzel')
    drawRect(app.beginB.x, app.beginB.y, app.beginB.width, app.beginB.height,
             fill = "maroon")
    drawLabel("New Game", app.beginB.x + app.beginB.width//2,
              app.beginB.y + app.beginB.height//2, size=24, font='cinzel',
              fill = "white")
    drawRect(app.contB.x, app.contB.y, app.contB.width, app.contB.height,
             fill = "gold")
    drawLabel("Continue", app.contB.x + app.contB.width//2,
              app.contB.y + app.contB.height//2, size=24, font='cinzel',
              fill = "white")
    drawRect(app.helpB.x, app.helpB.y, app.helpB.width, app.helpB.height,
             fill = "darkblue")
    drawLabel("Help", app.helpB.x + app.helpB.width//2,
              app.helpB.y + app.helpB.height//2, size=24, font='cinzel',
              fill = "white")
    drawRect(app.settingsB.x, app.settingsB.y, app.settingsB.width, 
             app.settingsB.height, fill = "darkgreen")
    drawLabel("Settings", app.settingsB.x + app.settingsB.width//2,
              app.settingsB.y + app.settingsB.height//2, size=24, font='cinzel',
              fill = "white")

def drawSnakeGame(app):
    drawCircle(app.width//2, app.height//2, 300, fill = None, border = "black")
    drawCircle(app.width//2, app.height//2, 200, fill = None, border = "black")
    drawCircle(app.width//2, app.height//2, 100, fill = None, border = "black")

def drawMarbles(app):
    drawLabel(app.player1Name, 160, 60, size=30, font="cinzel")
    for marble in app.player1M:
        drawCircle(marble.x, marble.y, marble.radius, fill = app.player1C)
    
    drawLabel(app.player2Name, app.width-220, 60, size=30, font="cinzel")
    for marble in app.player2M:
        drawCircle(marble.x, marble.y, marble.radius, fill = app.player2C)


def redrawAll(app):
    if not app.start:
        drawStartScreen(app)
    if app.start:
        drawSnakeGame(app)
        drawMarbles(app)

# def onStep(app):
#     for marble in app.movingmarbles:
#         marble


runApp(width = 1600, height = 800)
