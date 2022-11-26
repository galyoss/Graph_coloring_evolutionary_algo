import random

import numpy as np

from eckity.genetic_encodings.ga.vector_individual import Vector
from eckity.genetic_operators.genetic_operator import GeneticOperator

from eckity.creators.ga_creators.simple_vector_creator import GAVectorCreator
from eckity.genetic_encodings.ga.int_vector import IntVector
from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator

import networkx as nx
import matplotlib.pyplot as plt

from consts import MAX_COLORS, COLOR_MAP

''''
TODO:
fitness - num of collisions

'''


class GraphColoringCreator(GAVectorCreator):
    def __init__(self,
                 length=1,
                 events=None):
        super().__init__(length, None, (0, MAX_COLORS - 1), IntVector, events)

    def create_vector(self, individual):
        """
        :param individual:
        :return: void
        the function sets the individual coloring from a random generator, when range of options is the number of colors
        """
        coloring = list(np.random.randint(MAX_COLORS, size=individual.length))
        individual.set_vector(coloring)


# assuming even number of individuals
class ColoringCrossover(GeneticOperator):
    def __init__(self):
        self.applied_individuals = None
        super().__init__(arity=2)

    def apply(self, individuals):
        for i in range(0, len(individuals) - 1, 2):
            if i + 1 < len(individuals):
                individuals[i], individuals[i + 1] = self.cross(individuals[i], individuals[i + 1])
        self.applied_individuals = individuals
        return individuals

    def cross(self, individual1: Vector, individual2: Vector):
        cut_index = int(np.random.randint(individual1.length, size=1))
        # get vector parts to put in other individual
        part_from_first_vec = individual1.get_vector_part(0, cut_index)
        part_from_second_vec = individual2.get_vector_part(0, cut_index)
        # get full vectors of individuals
        individual1_full_vector = individual1.get_vector()
        individual2_full_vector = individual2.get_vector()
        # create new color vectors
        individual1_full_vector[0:cut_index] = part_from_second_vec
        individual2_full_vector[0:cut_index] = part_from_first_vec
        # set new color vectors
        individual1.set_vector(individual1_full_vector)
        individual2.set_vector(individual2_full_vector)
        return individual1, individual2


class ColoringMutation(GeneticOperator):
    def __init__(self, change_color_probability):
        super().__init__(arity=1, probability=change_color_probability)
        self.applied_individuals = None

    def apply(self, individuals):
        for ind in individuals:
            random_color = int(np.random.randint(MAX_COLORS, size=1))
            random_index = int(np.random.randint(ind.length, size=1))
            ind.set_cell_value(random_index, random_color)
        self.applied_individuals = individuals

        return individuals


class TSPEvaluator(SimpleIndividualEvaluator):
    def __init__(self, graph_matrix):
        super().__init__()
        self.graph_matrix = graph_matrix

    def _evaluate_individual(self, individual):
        """
        Compute the fitness value of a given individual.
        Parameters
        ----------
        individual: Vector
            The individual to compute the fitness value for.
        Returns
        -------
        float
            The evaluated fitness value of the given individual.
        """
        collision_counter = 0
        individual_list = individual.get_vector()
        for i in range(len(self.graph_matrix)):
            for j in range(len(self.graph_matrix)):
                if self.graph_matrix[i][j] == 1:  # vertices are neighbors
                    if individual_list[i] == individual_list[j]:  # coloring is the same for neighbor vertices
                        collision_counter += 1

        return int(collision_counter / 2)  # since we count every collision twice (i,j and j,i)


def draw_graph_with_solution(solution, graph_matrix):
    graph = nx.Graph()
    graph.add_nodes_from([i for i in range(len(graph_matrix))])
    coloring = [COLOR_MAP.get(i, "black") for i in solution]
    for i in range(len(graph_matrix)):
        for j in range(len(graph_matrix)):
            if graph_matrix[i][j] == 1:
                graph.add_edge(i, j)
    nx.draw(graph, node_color=coloring, with_labels=True)
    plt.show()

def generate_random_graph(size):
    g = []
    for _ in range(size):
        g.append([0 for _ in range(size)])

    for i in range(size):
        for j in range(i):
            rnd = random.randint(0, 1)
            g[i][j] = rnd
            g[j][i] = rnd

    return g


if __name__ == '__main__':
    g= generate_random_graph(30)
    x=5