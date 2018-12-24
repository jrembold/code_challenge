"""
Solution for Challenge 1a
 - Jed Rembold

Algorithm uses the follow the right-hand wall
method to find its way through the maze. Any
dead-ends paths are left in the path to be
plotted.
"""

import matplotlib.pyplot as plt
import numpy as np
import MazeGen

# Set desired size
SIZE = 100

# Generate the maze
maze, enter, exit = MazeGen.gen_maze(SIZE)

# Path is my list of the followed points
# Here I initialize it to the starting point
path = [np.array(enter)]

# My rotation vector to apply a vector rotation to the right
rot = np.array([[0,1],[-1,0]])
# My initial heading (downwards)
heading = np.array((1,0))

# Keep going as long as our latest point isn't the exit
while any(path[-1] != exit):
    # Set our current location to the last point
    curr = path[-1]
    # Determine what direction is "right" of us
    rhead = rot.dot(heading)
    # Use that direction to determine the "right block" coordinates
    rcoord = curr + rhead

    # Making our choices
    if not (maze[tuple(rcoord)]):
        # There is an opening to the right
        # Turn right and go forward
        path.append(rcoord)
        heading = rhead
    elif not (maze[tuple(curr+heading)]):
        # There is an opening ahead of us
        # Go forward
        path.append(curr+heading)
    else:
        # Both ahead and to the right are blocked
        # Turn left
        heading=heading.dot(rot)


# Plot up the resulting path. Using 'gray_r' for black walls
plt.imshow(maze, cmap='gray_r')
plt.axis('off')
plt.plot([x[1] for x in path], [x[0] for x in path], lw=200/SIZE, alpha=0.5)
plt.show()
