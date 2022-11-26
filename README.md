# Dillinger

## Intro

In graph theory, coloring is the process of labeling each vertex with a color.
We define "collision" as a case where 2 neighbor vetrices are labeled with the same color.
Coloring problem is useful in the area of computer science, as it can be a reduction to real-world problems taken from many worlds: networks, constuction/civil engineering, design and more.
The project's objective is to find a coloring for a given graph, with minimum collisions, using evolutionary algorithm.
The amount of colors can be determined by the user.

## Implementation
### Representation and coloring definitions:
- Graph - Represented as adjecency matrix (symmetric, with zeros on the diagonals)
- We included a package which draws the "best" solution the algorithm finds. I.E: 

Evolutionary definitions:
- Phenotype - array with a cell for each vertex. the value each cell holds is the color of the cell.
there is no need for validation on the Phenotype, as there is no "illegal colorings"
- Fitness - amount of collision in the coloring, according to a certain Phenotype.
If nodes v,u are neighbors and have the same color, we count this as 1 collision.
- Initial population - random arrays with their length set to amount of vertices, with random colors (Up to the amount of colors set by the user)

- Used operators
-- Crossover - Taking two individuals from the population, we cut their color arrays, and mix between the two.
-- Mutation - For the new generation created by crossover, we'll mutate each entity with probability of 0.05. mutation is implemeted by a random index, and assigning it a random color.
- Selection - Tournament based, using size of 4

## Installation and usage

- Clone git repository
- Verify using python 3
- Install dependencies: numpy, matplotlib, networkX, ECKity
- Swap the graph_matrix parameter to a value of your choosing.
- Under `consts.py`, change pramater MAX_COLORS to desired value.
Note: inserted matrix should be:
-- 2D, [n,n] array.
-- Containing only zeros and ones.
-- symmetric, with 0 on the diagonal
-- Entry [i,j] == 1 IFF there is an edge from vertex i to vertex j.
- Feel free to change the max_generation and population_size variables to any positive integer.
- Run the script. The result and a figure with the colored graph will be presented.

## Examples
