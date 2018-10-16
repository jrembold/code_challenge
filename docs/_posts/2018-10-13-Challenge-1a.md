---
title: Challenge 1a
author: Jed
layout: post
cover-photo: assets/images/C1a_cover.png
cover-photo-alt: Image of a solved maze
---

The first challenges are all about finding your way through randomly generated mazes of different sizes.
In particular, this first challenge will just require you to be able to be able to plot a path from the beginning of the maze to the end of the maze without crossing any walls (and not traveling outside the maze). 
Any number of dead-end paths can be included, you just must have a legal continuous path from the start of the maze to the end.

I have taken care of coding up a maze generator script, which you can download using the button on the bottom of this post.
For convenience, you can import it as a library to use it to generate a maze for you to solve directly in your program.
The `gen_maze` function takes a single argument, the desired size of the maze. 
It will return three values: the maze itself as a numpy array, the coordinates for the starting point of the maze (row,column), and the coordinates for the ending point of the maze (row, column).
You can thus generate the maze in your python script using something like below:

```python
import numpy as np
import MazeGen

size = 50
maze, enter, exit = MazeGen.gen_maze(size)
```

Once you have that, you can start the process of finding your way through the maze!
The numpy array is setup such that 1's represent walls and 0's represent corridors. 
You are only allowed to move up, down, left or right.
No diagonal movement is allowed.

_A note on visualizing: You may want to use `cmap=gray_r` when plotting the maze itself with `plt.imshow` to ensure you get white paths and black corridors._

For this first challenge, a potential solution might look something like
<center>
<figure>
<img src="{{site.baseurl}}/assets/images/C1a_cover.png" alt="Image of solved maze" style="width:30%">
<figcaption>An example of a solved maze</figcaption>
</figure>
</center>


If you think you have a working solution, verify that it works on mazes of size 20, 50, and 100 and then email me with your script attached!

<footer>
<center>
<a href="{{site.baseurl}}/assets/scripts/MazeGen.py" class="button scrolly">Download MazeGen.py</a>
</center>
</footer>
