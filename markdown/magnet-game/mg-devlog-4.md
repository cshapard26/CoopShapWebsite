# Introduction
At this point, all the magnets have a net force controlling where they want to go. However, what happens if two magnets want to move to the same space? Which, if any, should get the space? Where should the other one move if it's first choice is taken? These are the questions I will answer in this devlog. *Note that all the below information is subject to change before the game's release. This algorithm works well for the current interactions, but new mechanics might warrant a full revamp of the algorithm.*

# Setting Desired Cells
The first goal is converting a magnet's net force into a list of cells the magnet wants to occupy, each with a weight. The way I implemented this was to break each force into its component x and y forces, weight each one directly with their magnitude, and also weight the diagonal with the average of these two weights multiplied by a constant. 

The cell associated with each of these weights are located at `(sign(net_force.x), 0)`, `(0, sign(net_force.y))`, and `(sign(net_force.x), sign(net_force.y))`, relative to the given magnet.

The reason that the diagonal weight is not simply the magnitude of the vector is to prevent magnets from always preferring to move diagonally. If there is any perpendicular force, no matter how small, it would make the magnet want to choose the diagonal. Instead, by averaging the x and y components and multiplying by a constant > 1, the magnets are able to move diagonally when the x and y forces are similar in magnitude, but prefer to move in cardinal directions otherwise.

The magnet also stores its current location as "friction" with a small constant. This ensures that even magnets with zero net force still have a place to move and also prevents negligible forces from influencing magnet movement.

Magnets now store an array filled with objects of (desired_cell, weight). A dictionary mapping each magnet to its array is created to consolidate this information.

# Resolving Cell Disputes
With each magnet now knowing what it wants and how much it wants it, we can start divvying up the cells. The algorithm is as follows:
1. Repeat the algorithm below until the dictionary is empty
2. Loop through each magnet in the dictionary.
3. If a magnet has no available spaces to move to, throw an error.
4. If a magnet only has one space it can move to, it moves there regardless of the weight and is removed from the dictionary. This location is now removed from all other magnets' desired cell arrays in the dictionary. 
5. Repeat the above process until all remaining magnets have >= 2 desired cells.
6. Find the highest weight among the remaining magnets' objects. Add all magnets with this weight to an array.
7. Check where each of these magnets want to move. If there is no conflict, then that magnet moves there and is removed from the dictionary. This location is now removed from all other magnets' desired cell arrays in the dictionary. 
8. If there is a conflict, the magnet with the smallest base (i.e. regular magnets are 1, large magnets are 2, etc.) moves and the objects are removed like in step 7.
9. If both magnets have the same base, then neither magnet moves. The shared location is removed form the dictionary, but the magnets are not.

# Examples
At this point, all magnets have moved to a cell determined the above algorithm. It allows for both complex and deterministic interactions, which is key in a puzzle game like Magnet Game. Here are some gifs of the interactions in action, with updated art too!
[Gif 1]
[Gif 2]
[Gif 3]

I hope you found the magnet movement system interesting and useful. If you have any questions, comments, or ideas, feel free to email me at coopershapard(at)duck.com!