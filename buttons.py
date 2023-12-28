class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

#checking to see if a button should be of a lower opacity, particularly the 
#cont game button
    def isFaded(self, saveFiles):
        if len(saveFiles) > 0:
            return True
        return False

    def isClicked(self, curX, curY):
        if (self.x <= curX <= self.x + self.width and 
            self.y <= curY <= self.y + self.height):
            return True
        return False
    
    