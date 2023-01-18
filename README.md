# 

## Intro

In graph theory, coloring is the process of labeling each vertex with a color.
We define "collision" as a case where 2 neighbor vertices are labeled with the same color.
Coloring problem is useful in the area of computer science, as it can be a reduction to real-world problems taken from many worlds: networks, constuction/civil engineering, design and more.
The project's objective is to find a coloring for a given graph, with minimum collisions, using evolutionary algorithm.
The amount of colors can be determined by the user.

## Implementation
### Representation and coloring definitions:
- Graph - Represented as adjecency matrix (symmetric, with zeros on the diagonals)
- Coloring option - for a graph with n vertices, we'll assign each of the vertices with an index from 0 to n-1. An array in size of n will represent the coloring of the graph, where each index-value pair in the array will match to a vertex and it's color.
When running the algorithm we use numbers to represent the colors, and when projecting to the final solution we use a python dictionary to match each of the numbers with a valid color.

![Screenshot 2023-01-14 at 11 12 09](https://user-images.githubusercontent.com/63665467/212464893-d8722884-d6a6-4fa1-894f-5d8ebfc3810e.png)


Evolutionary definitions:
- Phenotype - array with a cell for each vertex. the value each cell holds is the color of the cell.
there is no need for validation on the Phenotype, as there is no "illegal colorings"
- Fitness - amount of collision in the coloring, according to a certain Phenotype.
If nodes v,u are neighbors and have the same color, we count this as 1 collision.
- Initial population - random arrays with their length set to amount of vertices, with random colors (Up to the amount of colors set by the user)

Used operators:

- Crossover - Taking two individuals from the population, we cut their color arrays, and mix between the two.
![Screenshot 2023-01-14 at 11 14 31](https://user-images.githubusercontent.com/63665467/212464927-af77571b-86de-494c-abc2-ca6e96abc839.png)

- Mutation - For the new generation created by crossover, we'll mutate each entity with probability of 0.05. mutation is implemeted by a random index, and assigning it a random color.
![Screenshot 2023-01-14 at 11 15 07](https://user-images.githubusercontent.com/63665467/212464944-8337daff-b6cb-43aa-a01f-cc3e1bb26e84.png)
- Selection - Tournament based, using size of 4

## Installation and usage

- Clone git repository
- Verify using python 3
- Install dependencies: numpy, matplotlib, networkX, ECKity
- Swap the graph_matrix parameter to a value of your choosing.
- Under `consts.py`, change pramater MAX_COLORS to desired value.
Note: inserted matrix should be:
- 2D, [n,n] array.
- Containing only zeros and ones.
- symmetric, with 0 on the diagonal
- Entry [i,j] == 1 IFF there is an edge from vertex i to vertex j.
- Feel free to change the max_generation and population_size variables to any positive integer.
- Run the script. The result and a figure with the colored graph will be presented.

## Run Example

- Let's initiate a graph with size of 10.
```
    graph_matrix = \
        [[0, 0, 1, 1, 1, 0, 1, 0, 1, 1],
         [0, 0, 1, 1, 0, 1, 1, 0, 0, 1],
         [1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
         [0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
         [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
         [1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
         [1, 1, 0, 0, 1, 0, 1, 0, 1, 0]]
```
-  set in consts.py the max num of colors. in this case, we'll use 5.
- Running main() will generate the following result:
```
Best solution found: 
Solution: [1, 0, 4, 4, 0, 3, 4, 2, 3, 2]
number of collisions: 0
Amount of colors in the solution is 5
```
- We'll also get a view of the colored graph:

![Screenshot 2023-01-14 at 11 33 07](https://user-images.githubusercontent.com/63665467/212465545-e51e44c9-a908-4111-99c6-ce198ffeeed8.png)
