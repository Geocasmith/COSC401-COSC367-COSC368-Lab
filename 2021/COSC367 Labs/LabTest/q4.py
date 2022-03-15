import heapq

from search import *
from statistics import pvariance

class PriorityFrontier(Frontier):

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        variance = []
        cost = 0
        for arc in path:
            cost += arc[3]
            variance.append(arc[3])
        pvar = pvariance(variance)



        heapq.heappush(self.container, ((cost,-pvar), path))

    def __iter__(self):
        """We don't need a separate iterator object. Just return self. You
        don't need to change this method."""
        return self

    def __next__(self):

        if len(self.container) > 0:
            return heapq.heappop(self.container)[1]
        else:
            raise StopIteration

graph = ExplicitGraph(
    nodes = {'S', 'A', 'B', 'C', 'G'},
    edge_list=[('S','A', 1), ('S','C',2), ('S', 'B', 2),
               ('A', 'G', 3), ('C', 'G', 2), ('B', 'G', 2)],
    starting_nodes = ['S'],
    goal_nodes = {'G'})

solution = next(generic_search(graph, PriorityFrontier()))
print_actions(solution)