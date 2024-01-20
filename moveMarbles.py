from marbles import Marble

def hasFallen(marble, width, height, radius):
    curX = marble.x
    curY = marble.y
    centerX, centerY = width//2, height//2
    if (centerX - radius <= curX <= centerX + radius):
        if (centerY - radius <= curY <= centerY + radius):
            return True


def moveMarbles(marbles, width, height, radius):
    for marble in marbles:
        # check if it fell
        if hasFallen(marble, width, height, radius):
            # check legality
            for angle in range(0, 360, 45):
                if checkAngles(marble, marble.x, marble.y, width, height):
                    marble.angle = angle
            death = True
            # app.death, when on then moves it; toggle on and get the angle
            # set random speed and move it off the board 
            # adjust the disappearing:))
        

# backtracking
def checkAngles(marble, x, y, width, height):
    if x >= width and y > 0.75*height:
        return True
    #possible moves
    else:
        # make move
        for angle in range(0, 360, 45):
            marble.angle = angle
            x += 1
            y += 1
            # check
            if not marble.collide:
                return checkAngles(marble, x, y, width, height)
            x -= 1
            y -= 1
    return False