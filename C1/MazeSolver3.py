'''
New maze solver using a method by which neighboring
spaces are counted and filled in an outward
propogating direction (faucet method). Currently
returns shortest path, could be tweaked to return
all possible unique paths.
'''


import matplotlib.pyplot as plt
import numpy as np
from MazeGen import gen_maze, gen_maze2


def solve(maze,enter,exit):
    SIZE,_ = maze.shape

    def get_neighbors(pt):
        '''Function to return the indexes of the
        4 orthogonal neighbors of a point. Takes
        into account and does not error at edges.'''
        r,c = pt
        up = (max(0,r-1),c)
        down = (min(SIZE-1,r+1),c)
        left = (r, max(0, c-1))
        right = (r, min(SIZE-1, c+1))
        return [up, down, left, right]


    paths = np.zeros(maze.shape)
    paths[enter] = 1
    paths[enter[0]+1,enter[1]] = 2

    #-------------------
    # Main Filling Loop
    #-------------------
    n = 2
    noexit = True
    while noexit:
        r,c = np.where(paths==n)
        cidxs = [(i,j) for i,j in zip(r,c)]
        for pt in cidxs:
            if pt == exit:
                noexit = False
                break
            for d in [(-1,0), (1,0), (0,-1), (0,1)]:
                npt = tuple(i+j for i,j in zip(pt,d))
                if paths[npt] == 0 and maze[npt] == 0:
                    paths[npt] = n+1
        n += 1

    #----------------
    # Shortest path
    #----------------

    # Set zeros in path to nan so as to not interfere with min calcs
    paths = np.where(paths==0,np.nan,paths)

    spath = [exit]
    while spath[-1] != enter:
        cpt = spath[-1]
        best_nb_val = SIZE**2
        best_nb_idx = (0,0)
        for nb in get_neighbors(cpt):
            if paths[nb] < best_nb_val:#This will guarantee shortest path
            # if paths[nb] < paths[cpt]: #Technically just needs this atm
                best_nb_val = paths[nb]
                best_nb_idx = nb
        spath.append(best_nb_idx)

    return spath, paths

if __name__ == '__main__':
    SIZE = 100
    maze, enter, exit = gen_maze2(SIZE)
    spath, paths = solve(maze, enter, exit)

    plt.imshow(paths, cmap='cool')
    plt.imshow(maze, cmap='gray_r', alpha=0.4)
    plt.plot([i[1] for i in spath],[i[0] for i in spath], color='black',lw=2)
    plt.axis('off')
    plt.show()
