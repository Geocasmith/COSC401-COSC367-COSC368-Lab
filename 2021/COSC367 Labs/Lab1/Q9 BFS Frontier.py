from search import *
import collections


class BFSFrontier(Frontier):

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = collections.deque([])

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """We don't need a separate iterator object. Just return self. You
        don't need to change this method."""
        return self

    def __next__(self):

        if len(self.container) > 0:
            return self.container.popleft()
        else:
            raise StopIteration  # don't change this one

graph = ExplicitGraph(nodes=set('SAG'),
                      edge_list = [('S','A'), ('S', 'G'), ('A', 'G')],
                      starting_nodes = ['S'],
                      goal_nodes = {'G'})

solutions = generic_search(graph, BFSFrontier())
solution = next(solutions, None)
print_actions(solution)

graph = ExplicitGraph(nodes=set('SAG'),
                      edge_list = [('S','G'), ('S', 'A'), ('A', 'G')],
                      starting_nodes = ['S'],
                      goal_nodes = {'G'})

solutions = generic_search(graph, BFSFrontier())
solution = next(solutions, None)
print_actions(solution)

flights = ExplicitGraph(nodes=['Christchurch', 'Auckland',
                               'Wellington', 'Gold Coast'],
                        edge_list = [('Christchurch', 'Gold Coast'),
                                 ('Christchurch','Auckland'),
                                 ('Christchurch','Wellington'),
                                 ('Wellington', 'Gold Coast'),
                                 ('Wellington', 'Auckland'),
                                 ('Auckland', 'Gold Coast')],
                        starting_nodes = ['Christchurch'],
                        goal_nodes = {'Gold Coast'})

my_itinerary = next(generic_search(flights, BFSFrontier()), None)
print_actions(my_itinerary)

graph = ExplicitGraph(nodes=set('SABG'),
                      edge_list = [('S','A'), ('S', 'B'),
                               ('B','S'), ('A', 'G')],
                      starting_nodes = ['S'],
                      goal_nodes = {'G'})

solutions = generic_search(graph, BFSFrontier())
solution = next(solutions, None)
print_actions(solution)