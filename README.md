# 

## Intro

In graph theory, coloring is the process of labeling each vertex with a color.
We define "collision" as a case where 2 neighbor vetrices are labeled with the same color.
Coloring problem is useful in the area of computer science, as it can be a reduction to real-world problems taken from many areas: networks, constuction/civil engineering, design etc.
The project's objective is to find a coloring for a given graph, with minimum collisions, using evolutionary algorithm.
The amount of colors as well as the graph itself can be determined by the user.

## Implementation
### Representation and coloring definitions:
- Graph - Represented as adjecency matrix (symmetric, with zeros on the diagonals). if there is an edge between vertices i and j, then matrix[i][j] = matrix[j][i] = 1 . Else, the value is zero.
- We included a package which draws the "best" solution the algorithm finds. I.E: ![WhatsApp Image 2022-11-26 at 12 39 20 PM](https://user-images.githubusercontent.com/63665467/204087891-a34e5d22-43f6-4024-8e96-39b82739212d.jpeg)


Evolutionary definitions:
- Phenotype - array with a cell for each vertex. the value each cell holds is the color of the represented vertex.
there is no need for validation on the Phenotype, as there is no "illegal colorings"
- Fitness - amount of collision in the coloring, according to a certain Phenotype.
If nodes v,u are neighbors and have the same color, we count this as 1 collision. Fitness of a solution is the amount of collisions in the graph (each a collision between vertices i and j is counted as a single collision).
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
-- 2D (nXn)] array.
-- Containing only zeros and ones.
-- symmetric, with 0 on the diagonal
-- Entry [i,j] == 1 IFF there is an edge from vertex i to vertex j.
- Feel free to change the max_generation and population_size variables to any positive integer.
- Run the script. The result and a figure with the colored graph will be presented.

## Examples
