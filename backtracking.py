# backtracking

# OBJECTIVE: Make it so that marbles on the board can go back to orig 
# position without collisions

from marbles import Marble

def findDist(marble, center):
    x, y = center
    return ((marble.x - x)**2 + (marble.y-y)**2) ** 0.5

def lastMarbleInsert(center, remaining, total):
    lastM = remaining[0]
    dist1 = findDist(lastM, center)
    index = 0
    for marble in total:
        if findDist(marble, center) > dist1:
            return total.insert(index, lastM)
        index += 1
    return total.append(lastM)
<<<<<<< Updated upstream

=======
    
    
    
## keep this for later ##
>>>>>>> Stashed changes
def getOrdered(center, remaining, total):
    print(total)
    if len(remaining) == 1:
        return lastMarbleInsert(center, remaining, total)
    else:
        marbles = remaining[0:2]
        remaining = remaining[2:]
        m1, m2 = marbles[0], marbles[1]
        dist1 = findDist(m1, center)
        dist2 = findDist(m2, center)
        if dist1 <= dist2:
            print("hey")
            return getOrdered(center, remaining, total+[m1,m2])
        else:
            print("oh")
            curr = [m2]
            return curr.append(getOrdered(center, [m1] + remaining, total))
    

def getMarbsList(marbles, width, height):
    new = []
    center = (width//2, height//2)
    for marble in marbles:
        new.append(marble)
    return new

def moveBack(marbles, width, height):
    # get marbles in order of position to board
    center = (width//2, height//2)
    marbleList = getMarbsList(marbles, width, height)
    marblePositions = getOrdered(center, marbleList, [])
    print(marblePositions)

m1 = Marble(10, 20, 25, "red")
m2 = Marble(30, 20, 25, "red")
m3 = Marble(10, 60, 25, "red")
m4 = Marble(50, 60, 25, "red")
m5 = Marble(80, 100, 25, "red")
m6 = Marble(90, 130, 25, "red")
marbles1 = [m1, m2, m3, m4, m5, m6]
moveBack(marbles1, 400, 400)
