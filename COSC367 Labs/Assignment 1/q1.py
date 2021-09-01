import heapq
import time
import math
from search import *

class RoutingGraph(Graph):
    """A graph where nodes are numbers. A number n leads to n-1 and
    n+2. Nodes that are divisible by 10 are goal nodes."""

    def __init__(self, map):
        self.map = map
        self.startNodes = []
        self.goal = []
        self.obstacles = []
        self.fuel = []

        # Split string into individual chars, returns list of lists
        split = map.split('\n')
        for i in range(len(split)):
            split[i] = list(split[i])

        for row in range(len(split)):
            for col in range(len(split[row])):
                node = split[row][col]
                if node == 'X' or node == '|' or node == '+' or node == '-':
                    self.obstacles.append((row, col))
                elif node == 'F':
                    self.fuel.append((row, col))
                elif node == 'G':
                    self.goal.append((row, col))
                elif node == 'S':
                    self.startNodes.append((row, col, math.inf))
                elif node.isdigit():
                    self.startNodes.append((row, col, int(node)))
        #print(self.starting_nodes)
        # print(self.goal_nodes)
        # print(self.obstacles)
        #print(self.fuel)

    def outgoing_arcs(self, tail_node):
        """Takes a node (which is an integer in this problem) and returns
        outgoing arcs (always two arcs in this problem)"""
        outgoing = []
        available = [('N', -1, 0),
                     ('E', 0, 1),
                     ('S', 1, 0),
                     ('W', 0, -1), ]


        for move in available:
            action = move[0]

            newRow = tail_node[0] + move[1]
            newCol = tail_node[1] + move[2]
            target_node = (newRow, newCol)
            fuel=tail_node[2]

            if not (target_node in self.obstacles):


                if fuel!=0:
                    outgoing.append(Arc(tail_node, (newRow, newCol, (fuel - 1)), action, 5))
        tailx, taily, fuel = tail_node
        if (tailx,taily) in self.fuel and fuel < 9:
            outgoing.append(Arc(tail_node, (tailx, taily, 9), "Fuel up", 15))

        return outgoing

    def starting_nodes(self):
        """Returns a sequence (list) of starting nodes. In this problem
        the seqence always has one element."""
        return self.startNodes

    def is_goal(self, node):
        """Determine whether a given node (integer) is a goal."""
        return (node[0], node[1]) in self.goal
    def estimated_cost_to_goal(self, node):
        costs = []
        for goal in self.goal:
            goalx , goaly , fueld = goal
            nodex, nodey = node

            distancex = abs(goalx-nodex)
            distancey = abs(goaly-nodey)
            distance = (distancex,distancey)
            print("DISTANCE")
            print(distance)
            #costs.append((di))

class AStarFrontier(Frontier):

    def __init__(self,graph):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []
        self.graph=graph
        self.visited=[]
        self.startTime =time.time()
    def add(self, path):
        cost = 0
        for arc in path:
            cost += arc[3]  # getting all the costs of previous path
        heapq.heappush(self.container, (cost, path))


    def __iter__(self):
        """We don't need a separate iterator object. Just return self. You
        don't need to change this method."""
        return self

    def __next__(self):
        endtime = time.time()
        elapsed = endtime-self.startTime
        if(elapsed>0.5):
            raise StopIteration

        if len(self.container) > 0:
            return heapq.heappop(self.container)[1]
        else:
            raise StopIteration  # don't change this one


map_str = """\
+----------+
|    X     |
| S  X  G  |
|    X     |
+----------+
"""

map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print(solution)
print_actions(solution)