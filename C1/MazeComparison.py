'''
A quick script to compare different maze solving methods.
'''

import matplotlib.pyplot as plt
import numpy as np
from MazeGen import gen_maze, gen_maze2
import MazeSolver2 as ms2
import MazeSolver3 as ms3

SIZE = 100
maze, enter, exit = gen_maze2(SIZE)

path2 = ms2.solve(maze, enter, exit)
path3,cpath = ms3.solve(maze, enter, exit)

plt.imshow(maze, cmap='gray_r')
plt.plot([i[1] for i in path2], 
        [i[0] for i in path2], 
        lw=2, 
        color='red',
        alpha=0.5,
        label='Right Wall Hugger')
plt.plot([i[1] for i in path3], 
        [i[0] for i in path3],
        lw=2, 
        color='blue',
        alpha=0.5,
        label='Faucet Method')
plt.legend(loc='lower left', bbox_to_anchor=(0,1.01), ncol=2, frameon=False)
plt.axis('off')
plt.show()


