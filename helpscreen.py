from cmu_graphics import *
#rules and how to play

#pseudo-coding

#rules:
# player goes one at a time, starting with player 1
# each player chooses a marble on their side, place it into playing location 
# then, they choose direction and strength of the marble 
# DEVELOPER SIDE: we calculate the magnitude + the impact it would take
# release, and try to get as close to the "hole" without actually going into it

from buttons import Button

def helpscreen_onAppStart(app):
    print('In helpscreen_onAppStart')
    buttons(app)

def helpscreen_onScreenActivate(app):
    print('In helpscreen_onScreenActivate')

def buttons(app):
    app.homeB = Button(10, 10, 60, 30)

def helpscreen_onMousePress(app, mouseX, mouseY):
    if app.homeB.isClicked(mouseX, mouseY):
        setActiveScreen('home')

def helpscreen_redrawAll(app):
    #homeB
    drawRect(app.homeB.x, app.homeB.y, app.homeB.width, app.homeB.height,
             fill = None, border = "black", borderWidth = 2)
    drawLabel('Home', 20, 25, size = 15, font = 'cinzel', align = 'left')
