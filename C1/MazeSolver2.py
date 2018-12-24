"""
Solution for Challenge 1b
 - Jed Rembold

Uses the same framework as the solution to
Challenge 1b but checks and removes duplicate
entries to remove dead-end paths.
"""


import matplotlib.pyplot as plt
import numpy as np
import MazeGen


def solve(maze, enter, exit):
    # Initialize the path at the start
    path = [np.array(enter)]

    # Setup the rotation matrix and initial heading
    rot = np.array([[0,1],[-1,0]])
    heading = np.array((1,0))

    # Keeping going until we are at the exit
    while any(path[-1] != exit):
        # Current position is latest path coordinate
        curr = path[-1]
        # Determine "right" heading
        rhead = rot.dot(heading)
        # Determine the coordinate of the right block
        rcoord = curr + rhead

        # Make our choices
        if not (maze[tuple(rcoord)]):
            # Right path open
            # Turn right and go forward
            path.append(rcoord)
            heading = rhead
        elif not (maze[tuple(curr+heading)]):
            # Forward block open
            # Go forward
            path.append(curr+heading)
        else:
            # Both right and forward paths blocked
            # Turn left
            heading=heading.dot(rot)

    # ----- Removing deadends -----
        # Find all the previous points which match
        # our current position
        repeats = np.where([all(x==path[-1]) for x in path])[0]
        # If there are repeats beyond the obvious last position
        # cut off all the path points beyond that repeat
        # (which would be the dead-end path)
        if len(repeats) > 1:
            path = path[:repeats[-2]+1]

    return path

if __name__ == '__main__':
    SIZE = 100
    # Create the maze
    maze, enter, exit = MazeGen.gen_maze(SIZE)
    # Find the path through the maze
    path = solve(maze, enter, exit)

    # Plot the maze
    plt.imshow(maze, cmap='gray_r')
    plt.axis('off')
    plt.plot([x[1] for x in path], [x[0] for x in path], lw=200/SIZE, color='red')
    plt.show()
