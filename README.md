# Cleaning Robot AI

This project is to refresh myself on basic artificial intelligence ideas by having an unintelligent cleaning robot clean an environment that does not present an impossibility such as a blocked corner.

### The Environment
The space that the robot will have to clean can be occupied by a couple  different things: "Dirt", "Empty", "Object", or the "Robot" itself.

### Movement
The robot is only possible of 4 different movements either 'Up', 'Right', 'Down', or 'Left'. There might be the addition of the diagonal directions being added in the future but as of the intial development it will remain those 4.

### Random Robot
This robot given an environment that is possible to solve will attempt to solve it by randomly choosing between the four directions "Up", "Right", "Down", or "Left" until there are no spaces that are not "Clean" or "Object". Each robot has access to its environment and movement stats. The movement stats are how many times it has moved in each of the four directions and how many times it has moved in total. The testing on this robot in different scenarios can be found in the results folder in 'randomResults.txt'. The tests consist of varying environment sizes 5x5, 10x10, 25x25, 50x50. Along with varying amounts and locations of clean and blocked spaces either at (1, 1), (1, 1) and (2, 2), or (1, 1), (2, 2), and (3, 3).

### Under Construction
The next idea for this project is to include other types of cleaning methods aside from random. Then taking those other cleaning methods develop ways in which they can mutate and hold a tournament style evolution where a population is generated, N elements are chosen from the population and the best of that selection is then cloned and the whole process repeats.
