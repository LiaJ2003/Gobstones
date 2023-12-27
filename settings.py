from cmu_graphics import *
from buttons import Button

def settings_onAppStart(app):
    print('In home_onAppStart')
    
    app.menuWidth = 200
    app.menuHeight = 50
    app.p1BX = 500 #player 1 button's X coordinate
    app.p2BX = 950 #player 2 button's X coordinate
    app.BY = 270
    app.p1MenuSelected = False
    app.p2MenuSelected = False
    app.textColor = 'black'
    app.options = {'Default':(575, 115), 'Gryffindor':(575, 135), 
                   'Hufflepuff':(575, 155), 'Ravenclaw':(575, 175), 
                   'Slytherin':(575, 195)}
    app.optionList = []
    for option in app.options:
        app.optionList += [option]
    app.selectedTheme = app.optionList[0]

    if app.p1MenuSelected == False: #if the menu is not open
        app.clickOtherButtons = True #we can select the other buttons
    else:
        app.clickOtherButtons = False #otherwise we can't when the menu is covering up the buttons
    buttons(app)

def settings_onScreenActivate(app):
    print('In newgame_onScreenActivate')

def settings_redrawAll(app):
    drawLabel("Settings", 800, 100, size=80, font='cinzel')
    drawLabel("Theme", 200, 300, size=60, font='cinzel')
    drawLabel("Player 1", 600, 200, size=60, font='cinzel')
    drawLabel("Player 2", 1050, 200, size=60, font='cinzel')
    drawP1Menu(app)
    drawP2Menu(app)
    if app.p1MenuSelected == False:
        #draw other buttons the dropdown menu covers
        return
    else:
        return
    

def buttons(app):
    app.p1ThemeB = Button(app.p1BX, app.BY, app.menuWidth, app.menuHeight)
    app.p2ThemeB = Button(app.p2BX, app.BY, app.menuWidth, app.menuHeight)

def settings_onMousePress(app, mouseX, mouseY):
    if app.p1ThemeB.isClicked(mouseX, mouseY):
        if not app.p1MenuSelected:
            app.p1MenuSelected = True
        else:
            app.p1MenuSelected = False
    if app.p2ThemeB.isClicked(mouseX, mouseY):
        if not app.p2MenuSelected:
            app.p2MenuSelected = True
        else:
            app.p2MenuSelected = False


def drawP1Menu(app):
    labelX = 540 
    labelY = 295 

    drawLabel(f"{app.selectedTheme}", labelX, labelY, size = 20, align = 'left', 
              fill = app.textColor, font = 'cursive', bold = True)
    if app.p1MenuSelected == True:
        drawRegularPolygon(660, labelY, 10, 3, fill=app.textColor, border=None,
               borderWidth=2, opacity=100, rotateAngle=0, dashes=False,
               align='center', visible=True)
        drawRect(app.p1BX, app.BY, app.menuWidth, app.menuHeight*5, fill = None, 
                 border = app.textColor, borderWidth = 2)
        for i in range(len(app.options)):
            drawRect(app.p1BX, app.BY+i*app.menuHeight, app.menuWidth, app.menuHeight, 
                     fill = None, border = app.textColor, borderWidth = 1)
            if i>0:
                drawLabel(f"{app.optionList[i]}", labelX, labelY+i*app.menuHeight, 
                          size = 20, align = 'left', fill = app.textColor, 
                          font = 'cursive', bold = True)
    else:
        drawRegularPolygon(660, labelY, 10, 3, fill=app.textColor, border=None,
               borderWidth=2, opacity=100, rotateAngle=180, dashes=False,
               align='center', visible=True)
        drawRect(app.p1BX, app.BY, app.menuWidth, app.menuHeight, fill = None, 
                 border = app.textColor, borderWidth = 2)

    
def drawP2Menu(app):
    labelX = 990 
    labelY = 295

    drawLabel(f"{app.selectedTheme}", labelX, labelY, size = 20, align = 'left', 
              fill = app.textColor, font = 'cursive', bold = True)
    if app.p2MenuSelected == True:
        drawRegularPolygon(1100, labelY, 10, 3, fill=app.textColor, border=None,
               borderWidth=2, opacity=100, rotateAngle=0, dashes=False,
               align='center', visible=True)
        drawRect(app.p2BX, app.BY, app.menuWidth, app.menuHeight*5, fill = None, 
                 border = app.textColor, borderWidth = 2)
        for i in range(len(app.options)):
            drawRect(app.p2BX, app.BY+i*app.menuHeight, app.menuWidth, app.menuHeight, 
                     fill = None, border = app.textColor, borderWidth = 1)
            if i>0:
                drawLabel(f"{app.optionList[i]}", labelX, labelY+i*app.menuHeight, 
                          size = 20, align = 'left', fill = app.textColor, 
                          font = 'cursive', bold = True)
    else:
        drawRegularPolygon(1100, labelY, 10, 3, fill=app.textColor, border=None,
               borderWidth=2, opacity=100, rotateAngle=180, dashes=False,
               align='center', visible=True)
        drawRect(app.p2BX, app.BY, app.menuWidth, app.menuHeight, fill = None, 
                 border = app.textColor, borderWidth = 2)