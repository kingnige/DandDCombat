import numpy as np

def showMap():
    print(np.matrix(map))
    print('\n\n')

#create an array to hold the information
grid = 15
map = ['-'] * grid
for i in range(grid):
    map[i] = ['-'] * grid

#create values to store the current location of the array
arrayX = 7
arrayY = 7

#create values to store the different compass directions
north = -1
south = 1
west = -1
east = 1

#create values to record the possible movements
arrayXpos = arrayX
arrayYpos = arrayY

#add the character to the centre of the map
map[arrayX][arrayY] = 'C'

#define movement speed
movement = 6
loopMovement = movement
loopControl = True
diagonalCounter = 0

#find possible movement places North
for i in range(1,movement+1):
    arrayXpos = arrayXpos + north
    map[arrayXpos][arrayYpos] = 'p'
arrayXpos = arrayX
arrayYpos = arrayY

#find possible movement places East
for i in range(1,movement+1):
    arrayYpos = arrayYpos + east
    map[arrayXpos][arrayYpos] = 'p'
arrayXpos = arrayX
arrayYpos = arrayY

#find possible movement places South
for i in range(1,movement+1):
    arrayXpos = arrayXpos + south
    map[arrayXpos][arrayYpos] = 'p'
arrayXpos = arrayX
arrayYpos = arrayY

#find possible movement places West
for i in range(1,movement+1):
    arrayYpos = arrayYpos + west
    map[arrayXpos][arrayYpos] = 'p'
arrayXpos = arrayX
arrayYpos = arrayY

#find possible movement places North East
while loopMovement > 0:
    if loopMovement >= 1:
        if loopControl == True:
            arrayXpos = arrayXpos + north
            arrayYpos = arrayYpos + east
            map[arrayXpos][arrayYpos] = 'd'
            loopControl = False
            loopMovement = loopMovement - 1
            diagonalCounter = diagonalCounter + 1
    if loopMovement >= 2:
        if loopControl == False:
            arrayXpos = arrayXpos + north
            arrayYpos = arrayYpos + east
            map[arrayXpos][arrayYpos] = 'd'
            loopControl = True
            loopMovement = loopMovement - 2
            diagonalCounter = diagonalCounter + 1
arrayXpos = arrayX
arrayYpos = arrayY
loopMovement = movement
loopControl = True

#find possible movement places North West
while loopMovement > 0:
    if loopMovement >= 1:
        if loopControl == True:
            arrayXpos = arrayXpos + north
            arrayYpos = arrayYpos + west
            map[arrayXpos][arrayYpos] = 'd'
            loopControl = False
            loopMovement = loopMovement - 1
    if loopMovement >= 2:
        if loopControl == False:
            arrayXpos = arrayXpos + north
            arrayYpos = arrayYpos + west
            map[arrayXpos][arrayYpos] = 'd'
            loopControl = True
            loopMovement = loopMovement - 2
arrayXpos = arrayX
arrayYpos = arrayY
loopMovement = movement
loopControl = True

#find possible movement places South East
while loopMovement > 0:
    if loopMovement >= 1:
        if loopControl == True:
            arrayXpos = arrayXpos +south
            arrayYpos = arrayYpos + east
            map[arrayXpos][arrayYpos] = 'd'
            loopControl = False
            loopMovement = loopMovement - 1
    if loopMovement >= 2:
        if loopControl == False:
            arrayXpos = arrayXpos + south
            arrayYpos = arrayYpos + east
            map[arrayXpos][arrayYpos] = 'd'
            loopControl = True
            loopMovement = loopMovement - 2
arrayXpos = arrayX
arrayYpos = arrayY
loopMovement = movement
loopControl = True

#find possible movement places South West
while loopMovement > 0:
    if loopMovement >= 1:
        if loopControl == True:
            arrayXpos = arrayXpos + south
            arrayYpos = arrayYpos + west
            map[arrayXpos][arrayYpos] = 'd'
            loopControl = False
            loopMovement = loopMovement - 1
    if loopMovement >= 2:
        if loopControl == False:
            arrayXpos = arrayXpos + south
            arrayYpos = arrayYpos + west
            map[arrayXpos][arrayYpos] = 'd'
            loopControl = True
            loopMovement = loopMovement - 2
arrayXpos = arrayX
arrayYpos = arrayY
loopMovement = movement
loopControl = True

#find all possible movement places North West and North
for diagonalCount in range(1,diagonalCounter+1):
    while loopMovement > 0:
        while diagonalCount > 0:
            if loopMovement >= 1 and diagonalCount > 0:
                if (loopControl):
                    arrayXpos = arrayXpos + north
                    arrayYpos = arrayYpos + west
                    map[arrayXpos][arrayYpos] = 'd'
                    loopControl = False
                    loopMovement = loopMovement - 1
                    diagonalCount = diagonalCount - 1
            if loopMovement >= 2 and diagonalCount > 0:
                if loopControl == False:
                    arrayXpos = arrayXpos + north
                    arrayYpos = arrayYpos + west
                    map[arrayXpos][arrayYpos] = 'd'
                    loopControl = True
                    loopMovement = loopMovement - 2
                    diagonalCount = diagonalCount - 1
        if loopMovement >= 1:
            for i in range(0,loopMovement):
                arrayXpos = arrayXpos + north
                map[arrayXpos][arrayYpos] = 'd'
        loopMovement = 0
    arrayXpos = arrayX
    arrayYpos = arrayY
    loopMovement = movement
    loopControl = True

#show the current map
showMap()