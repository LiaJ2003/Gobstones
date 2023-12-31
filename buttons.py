class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def isClicked(self, curX, curY):
        if (self.x <= curX <= self.x + self.width and 
            self.y <= curY <= self.y + self.height):
            return True
        return False
    
    