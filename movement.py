import numpy as np

def showMap():
    print(np.matrix(map))
    print('\n\n')

#create an array to hold the information
grid = 11
map = ['-'] * grid
for i in range(grid):
    map[i] = ['-'] * grid

#create values to store the current location of the array
arrayX = 5
arrayY = 5

#create values to record the possible movements
arrayXpos = arrayX
arrayYpos = arrayY

#add the character to the centre of the map
map[arrayX][arrayY] = 'C'

#display the map with the character in the middle
showMap()

#define movement speed
movement = 4

#find possible movement places North
for i in range(1,movement+1):
    arrayXpos = arrayXpos - 1
    map[arrayXpos][arrayYpos] = 'p'
arrayXpos = arrayX
arrayYpos = arrayY
showMap()

#find possible movement places South
for i in range(1,movement+1):
    arrayXpos = arrayXpos + 1
    map[arrayXpos][arrayYpos] = 'p'
arrayXpos = arrayX
arrayYpos = arrayY
showMap()

#find possible movement places West
for i in range(1,movement+1):
    arrayYpos = arrayYpos - 1
    map[arrayXpos][arrayYpos] = 'p'
arrayXpos = arrayX
arrayYpos = arrayY
showMap()

#find possible movement places East
for i in range(1,movement+1):
    arrayYpos = arrayYpos + 1
    map[arrayXpos][arrayYpos] = 'p'
arrayXpos = arrayX
arrayYpos = arrayY
showMap()