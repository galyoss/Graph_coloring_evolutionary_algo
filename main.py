from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation

from utils import GraphColoringCreator, TSPEvaluator, ColoringMutation, ColoringCrossover, draw_graph_with_solution, generate_random_graph


def main():

    graph_matrix = generate_random_graph(20)

    print('running on graph {}'.format(graph_matrix))

    population_size = 50
    max_generation = 50
    # Initialize the evolutionary algorithm
    algo = SimpleEvolution(
        Subpopulation(creators=GraphColoringCreator(length=len(graph_matrix)),
                      population_size=population_size,
                      # user-defined fitness evaluation method
                      evaluator=TSPEvaluator(graph_matrix),
                      # maximization problem (fitness is sum of values), so higher fitness is better
                      higher_is_better=False,
                      elitism_rate=0.0,
                      # genetic operators sequence to be applied in each generation
                      operators_sequence=[
                          ColoringCrossover(),
                          ColoringMutation(change_color_probability=0.05)  # swap two random cities with prob ()
                      ],
                      selection_methods=[
                          # (selection method, selection probability) tuple
                          (TournamentSelection(tournament_size=4, higher_is_better=False), 1)
                      ]),
        breeder=SimpleBreeder(),
        max_workers=1,
        max_generation=max_generation,
        statistics=BestAverageWorstStatistics()
    )
    print("EA Process Presented Bellow:")

    # evolve the generated initial population
    algo.evolve()
    print("#####################################")

    print("The Ultimate solution found by our solver is (solution and fitness score)")
    algo.finish()
    solution = algo.best_of_run_.vector
    print(f"Amount of colors in the solution is {len(set(solution))}")
    #draw_graph_with_solution(solution, graph_matrix)



if __name__ == '__main__':
    main()
