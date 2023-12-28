from cmu_graphics import *
#rules and how to play

def helpscreen_onAppStart(app):
    app.returnX = app.width//2
    app.returnY = app.height - 20

def helpscreen_onMousePress(app, mouseX, mouseY):
    #returns to the original home screen; again will need to connect
    
    return

def helpscreen_redrawAll(app):
    #draw elements of help screen, similar to before
    return

#pseudo-coding

#rules:
# player goes one at a time, starting with player 1
# each player chooses a marble on their side, place it into playing location 
# then, they choose direction and strength of the marble 
# DEVELOPER SIDE: we calculate the magnitude + the impact it would take
# release, and try to get as close to the "hole" without actually going into it

