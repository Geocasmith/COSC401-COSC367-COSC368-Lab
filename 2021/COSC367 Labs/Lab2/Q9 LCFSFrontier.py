import heapq

from search import *
from math import dist
import collections
class LocationGraph():
    def __init__(self, nodes, locations, edges, starting_nodes, goal_nodes, estimates=None):

        assert all(tail in nodes and head in nodes for tail, head, *_ in edges) \
            , "An edge must link two existing nodes!"
        assert all(node in nodes for node in starting_nodes), \
            "The starting_states must be in nodes."
        assert all(node in nodes for node in goal_nodes), \
            "The goal states must be in nodes."

        self.nodes = nodes
        self.locations = locations
        self.edge_list = edges
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
        self.estimates = estimates

    def starting_nodes(self):
        """Returns a sequence of starting nodes."""
        return self._starting_nodes

    def is_goal(self, node):
        """Returns true if the given node is a goal node."""
        return node in self.goal_nodes

    def outgoing_arcs(self, node):
        """Returns a sequence of Arc objects that go out from the given
        node. The action string is automatically generated.

        """
        arcs = []
        for edge in self.edge_list:
            if len(edge) == 2:  # if no cost is specified
                tail, head = edge
                cost = 1  # assume unit cost
            else:
                tail, head, cost = edge
            if tail == node:
                arcs.append(Arc(tail, head, str(tail) + '->' + str(head), dist(self.locations.get(head),self.locations.get(tail))))

            if head == node:
                arcs.append(Arc(head, tail, str(head) + '->' + str(tail), dist(self.locations.get(head),self.locations.get(tail))))
        arcs.sort()
        arcs = list(dict.fromkeys(arcs))
        return arcs


class LCFSFrontier(Frontier):

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        cost=0
        for arc in path:
            cost+=arc[3] #getting all the costs of previous path
        heapq.heappush(self.container, (cost,path))

    def __iter__(self):
        """We don't need a separate iterator object. Just return self. You
        don't need to change this method."""
        return self

    def __next__(self):

        if len(self.container) > 0:
            return heapq.heappop(self.container)[1]
        else:
            raise StopIteration  # don't change this one


graph = LocationGraph(nodes=set('ABC'),
                      locations={'A': (0, 0),
                                 'B': (3, 0),
                                 'C': (3, 4)},
                      edges={('A', 'B'), ('B','C'),
                             ('B', 'A'), ('C', 'A')},
                      starting_nodes=['A'],
                      goal_nodes={'C'})

solution = next(generic_search(graph, LCFSFrontier()))
print_actions(solution)

graph = LocationGraph(nodes=set('ABC'),
                      locations={'A': (0, 0),
                                 'B': (3, 0),
                                 'C': (3, 4)},
                      edges={('A', 'B'), ('B','C'),
                             ('B', 'A')},
                      starting_nodes=['A'],
                      goal_nodes={'C'})

solution = next(generic_search(graph, LCFSFrontier()))
print_actions(solution)

pythagorean_graph = LocationGraph(
    nodes=set("abc"),
    locations={'a': (5, 6),
               'b': (10,6),
               'c': (10,18)},
    edges={tuple(s) for s in {'ab', 'ac', 'bc'}},
    starting_nodes=['a'],
    goal_nodes={'c'})

solution = next(generic_search(pythagorean_graph, LCFSFrontier()))
print_actions(solution)