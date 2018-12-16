import numpy as np

#create an array to hold the information
grid = 11
map = ['-'] * grid
for i in range(grid):
    map[i] = ['-'] * grid

#add the character to the centre of the map
map[5][5] = 'C'

#display the map with the character in the middle
print(np.matrix(map))