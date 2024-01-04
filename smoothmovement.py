from cmu_graphics import *
from tempmarbles import Marbles

def onAppStart(app):
    app.marble1 = Marbles(50, 50, 25, "red")
    app.marble2 = Marbles(50, 200, 25, "red")
    app.marble3 = Marbles(app.width-50, 50, 25, "blue")
    app.marble4 = Marbles(app.width-50, 200, 25, "blue")

    #had to make chosen a set because otherwise there was the bug of marbles
    #being unable to move *tears* 

    ## NOTE: might need to make confirmed a set as well ##
    app.marbles = {"chosen": set(), "rest": [app.marble1, app.marble2, app.marble3, app.marble4],
                   "confirmed": []}

    app.begin = False


def drawBorder1(app):
    drawRect(app.marble1.radius*4, 0, app.marble1.radius*2, app.height,
             fill = None, border = "black")
    
def drawBorder2(app):
    drawRect(app.width - app.marble1.radius*6, 0, app.marble1.radius*2,
             app.height, fill = None, border ="black")
    
def drawMarble(app):
    drawCircle(app.marble1.x, app.marble1.y, app.marble1.radius, fill = app.marble1.team)
    drawCircle(app.marble2.x, app.marble2.y, app.marble2.radius, fill = app.marble2.team)
    drawCircle(app.marble3.x, app.marble3.y, app.marble3.radius, fill = app.marble3.team)
    drawCircle(app.marble4.x, app.marble4.y, app.marble4.radius, fill = app.marble4.team)

def findIndex(L, find):
    index = 0
    for item in L:
        if item == find:
            return index
        index+=1
    return None  


def remFromList(L, item):
    curI = findIndex(L, item)
    return L[:curI] + L[curI+1:]
    

def onMousePress(app, mouseX, mouseY):
    for marble in app.marbles["rest"]:
        if marble.isChosen(mouseX, mouseY) and marble not in app.marbles["confirmed"]:
            remFromList(app.marbles["rest"], marble)
            app.marbles["chosen"].add(marble)
    print("choosing", app.marbles["chosen"])

def onKeyPress(app, key):
    #confirming
    print("confirm", app.marbles["chosen"])
    if key == "c" and len(app.marbles["chosen"])==1:
        curM = app.marbles["chosen"].pop()
        # print(app.marbles["chosen"])
        app.marbles["confirmed"].append(curM)

    #undoing
    if key == "u" and len(app.marbles["confirmed"]) >= 1:
        undoM = app.marbles["confirmed"].pop()
        if len(app.marbles["chosen"]) > 0:
            prev = app.marbles["chosen"].pop()
            app.marbles["rest"].append(prev)
        app.marbles["chosen"].add(undoM)


def redrawAll(app):
    drawMarble(app)
    drawBorder1(app)
    drawBorder2(app)


def onMouseDrag(app, mouseX, mouseY):
    if len(app.marbles["chosen"]) == 1:
        for item in app.marbles["chosen"]:
            curM = item
        curM.x = mouseX
        curM.y = mouseY

def onMouseRelease(app, mouseX, mouseY):
    if len(app.marbles["chosen"]) == 1:
        for item in app.marbles["chosen"]:
            snapM = item
        snapM.x = findClosestDistance(app, mouseX)
        snapM.y = mouseY

def findClosestDistance(app, x):
    b1X = 125
    b2X = app.width-125
    if x < app.width//2:
        return b1X
    return b2X

    

runApp(width = 500, height = 500)


