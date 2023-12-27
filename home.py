from cmu_graphics import *
from buttons import Button

def home_onAppStart(app):
    print('In home_onAppStart')
    app.start = False
    app.contPoss = False
    app.cont = False
    app.help = False
    app.settings = False
    buttons(app)

def home_onScreenActivate(app):
    print('In home_onScreenActivate')

def buttons(app):
    app.beginB = Button(550, 200, 500, 100)
    app.contB = Button(550, 350, 500, 100)
    app.helpB = Button(550, 500, 500, 100)
    app.settingsB = Button(550, 650, 500, 100)

def home_onMousePress(app, mouseX, mouseY):
    #initial game settings
    if app.beginB.isClicked(mouseX, mouseY):
        #app.start = True
        setActiveScreen('newgame')
    if app.contB.isClicked(mouseX, mouseY) and app.contPoss:
        #app.cont = True
        setActiveScreen('continue')
    if app.helpB.isClicked(mouseX, mouseY):
        #app.help = True
        setActiveScreen('help')
    if app.settingsB.isClicked(mouseX, mouseY):
        #app.settings = True
        setActiveScreen('settings')

    #when in game mode, checking to see if marble is being moved
    for marble in app.marbles:
        if marble.isChosen(mouseX, mouseY):
            marble.chosen = True

def home_onMouseDrag(app, mouseX, mouseY):

    return

def home_onKeyPress(app, key):
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

    
def home_redrawAll(app):
    drawStartScreen(app)



# def onStep(app):
#     for marble in app.movingmarbles:
#         marble

