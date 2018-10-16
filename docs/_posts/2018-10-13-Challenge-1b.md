---
title: Challenge 1b
author: Jed
layout: post
cover-photo: assets/images/C1b_cover.png
cover-photo-alt: Image of a solved maze
icon: fa-certificate
---

The second challenge builds on the first. 
Here the goal is to plot a __direct__ path through the maze from beginning to end. 
Not plotting any of the deadends. 
Your solver may well go _down_ these deadends in the course of solving the maze, but in the end you want to only plot the direct path.

<figure>
<center>
<img src="{{site.baseurl}}/assets/images/C1b_cover.png" alt='Example Challenge 2 maze' style="width:50%">
<figcaption>Example of plotting only the most direct route from entrance to exit</figcaption>
</center>
</figure>


Due to the algorithm used to create these mazes, this should also be akin to the shortest path from beginning to end.
You'll use the same maze generator script you used in Challenge 1a, so if you skipped that one go back to grab the generator there.

Once you have a script that can find and plot the direct path, test it on several different sizes of maze and then send it my way!
