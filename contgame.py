from cmu_graphics import *
from newgame import *

#load continued game
def contgame_onAppStart(app):
    print("continue game")
    app.start = False
    getPrevGame(app)

    app.allCoords = parsing(app.directions)

def getPrevGame(app):
    filename = 'commands.txt'
    # credits to Professor Pat Virtue for this code:
    with open(filename, encoding='utf-8') as f:
        fileString = f.read()   
    # print(fileString)

    app.directions = str(fileString)
    print(type(app.directions))

def parsing(dir):
    dictCoords = dict()
    dictCoords["red"] = []
    dictCoords["blue"] = []
    # print("coords", dir.splitlines())
    curTeam = ""
    for coord in dir.splitlines():
        print("coord", coord)
    
        if coord.isalpha():
            if coord == "red":
                print("red is here")
                curTeam = "red"
            elif coord == "blue":
                print("blue is here")
                curTeam = "blue"
        else:
            tempX = ""
            tempY = ""
            xTurn = True
            yTurn = False
            for char in coord:
                if char.isdigit():
                    if xTurn:
                        tempX += char
                    elif yTurn:
                        tempY += char
                if char == ",":
                    xTurn = False
                    yTurn = True
            
            tempX = int(tempX)
            tempY = int(tempY)
            print("tempX", tempX)
            print("tempY", tempY)
            newCoord = (tempX, tempY)
            
            
            dictCoords[curTeam].append(newCoord)
    return dictCoords

def contgame_onMousePress(app, mouseX, mouseY):
    if app.width//4 <= mouseX <= app.width//4 + app.width//2:
        if app.height-50 <= mouseY <= app.height-10:
            setActiveScreen('newgame')

def drawGhostMarbles(app):
    for team in app.allCoords:
        for coords in app.allCoords[team]:
            (x, y) = coords
            drawCircle(x, y, 15, fill = team)

def drawAgreeButton(app):
    drawRect(app.width//4, app.height-50, app.width//2, 40, fill = "lightgreen")

def contgame_redrawAll(app):
    drawLabel("Start this Game Again?", app.width//2, 25, size = 20, 
              font = 'cinzel')
    drawSnakeGame(app)
    drawBoard(app)
    drawGhostMarbles(app)
    drawAgreeButton(app)



