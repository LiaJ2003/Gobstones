from cmu_graphics import *
from marbles import Marbles
from button import Button

def onAppStart(app):
    app.start = False
    app.contPoss = False
    app.cont = False
    app.help = False
    app.settings = False
    buttons(app)

def buttons(app):
    app.beginB = Button(550, 200, 500, 100)
    app.contB = Button(550, 350, 500, 100)
    app.helpB = Button(550, 500, 500, 100)
    app.settingsB = Button(550, 650, 500, 100)

def onMousePress(app, mouseX, mouseY):
    if app.beginB.isClicked(mouseX, mouseY):
        app.start = True
    if app.contB.isClicked(mouseX, mouseY) and app.contPoss:
        app.cont = True
    if app.helpB.isClicked(mouseX, mouseY):
        app.help = True
    if app.settingsB.isClicked(mouseX, mouseY):
        app.settings = True

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

def drawGame(app):
    drawCircle(app.width//2, app.height//2, 300, fill = None, border = "black")
    drawCircle(app.width//2, app.height//2, 200, fill = None, border = "black")
    drawCircle(app.width//2, app.height//2, 100, fill = None, border = "black")

def redrawAll(app):
    if not app.start:
        drawStartScreen(app)
    if app.start:
        drawGame(app)

marble = Marbles(5, 5, 10, "red")
print(marble.x)

runApp(width = 1600, height = 800)
