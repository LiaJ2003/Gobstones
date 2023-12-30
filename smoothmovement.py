from cmu_graphics import *
from tempmarbles import Marbles

def onAppStart(app):
    app.marble1 = Marbles(50, 50, 25, "red")
    app.marble2 = Marbles(50, 200, 25, "red")
    app.marble3 = Marbles(app.width-50, 50, 25, "blue")
    app.marble4 = Marbles(app.width-50, 200, 25, "blue")

    app.marbles = {"chosen": [], "rest": [app.marble1, app.marble2, app.marble3, app.marble4],
                   "confirmed": []}
    app.begin = False


def drawBorder(app):
    drawRect(app.width//2-app.marble1.radius, 0, app.marble1.radius*2, app.height,
             fill = None, border = "black")
    
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

print(remFromList(["hi", "bye", "okay", "love"], "okay"))
    

def onMousePress(app, mouseX, mouseY):
    for marble in app.marbles["rest"]:
        if marble.isChosen(mouseX, mouseY) and marble not in app.marbles["confirmed"]:
            remFromList(app.marbles["rest"], marble)
            app.marbles["chosen"].append(marble)

def onKeyPress(app, key):
    #confirming
    print(app.marbles["chosen"])
    if key == "c" and len(app.marbles["chosen"])==1:
        curM = app.marbles["chosen"].pop()
        # print(app.marbles["chosen"])
        app.marbles["confirmed"].append(curM)


def redrawAll(app):
    drawMarble(app)
    drawBorder(app)



def onMouseDrag(app, mouseX, mouseY):
    if len(app.marbles["chosen"]) == 1:
        curM = app.marbles["chosen"][0]
        curM.x = mouseX
        curM.y = mouseY



    

runApp(width = 500, height = 500)


