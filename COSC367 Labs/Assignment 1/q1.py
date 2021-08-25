import math

from search import *
import collections
from itertools import dropwhile


class RoutingGraph(Graph):
    """A graph where nodes are numbers. A number n leads to n-1 and
    n+2. Nodes that are divisible by 10 are goal nodes."""

    def __init__(self, map):
        self.map = map
        self.start = []
        self.goal = []
        self.obstacles = []
        self.fuel = []

        # Split string into individual chars, returns list of lists
        split = map_str.split('\n')
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
                    self.start.append((row, col, math.inf))
                elif node.isdigit():
                    self.start.append((row, col, int(node)))
        # print(self.starting_nodes)
        # print(self.goal_nodes)
        # print(self.obstacles)
        # print(self.fuel)

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
            print(tail_node)
            newRow = tail_node[0][0] + move[1]
            newCol = tail_node[0][1] + move[2]
            target_node = (newRow, newCol)

            if not (target_node in self.obstacles):
                if target_node in self.fuel and tail_node[2] < 9:
                    outgoing.append(Arc(tail_node, tail_node, "Fuel up", 15))

                else:
                    outgoing.append(Arc[tail_node, (newRow, newCol, tail_node[2] - 5), action, 5])

        return outgoing

    def starting_nodes(self):
        """Returns a sequence (list) of starting nodes. In this problem
        the seqence always has one element."""
        return [self.start]

    def is_goal(self, node):
        """Determine whether a given node (integer) is a goal."""
        return node in self.goal


map_str = """\
+-------+
|  9  XG|
|X XXX  |
| S  0FG|
+-------+
"""

graph = RoutingGraph(map_str)

print("Starting nodes:", sorted(graph.starting_nodes()))
print("Outgoing arcs (available actions) at starting states:")
for s in sorted(graph.starting_nodes()):
    print(s)
    for arc in graph.outgoing_arcs(s):
        print ("  " + str(arc))

node = (1,1,5)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))

node = (1,7,2)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))

node = (3, 7, 0)
print("\nIs {} goal?".format(node), graph.is_goal(node))

node = (3, 7, math.inf)
print("\nIs {} goal?".format(node), graph.is_goal(node))

node = (3,6,5)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))

node = (3,6,9)
print("\nIs {} goal?".format(node), graph.is_goal(node))
print("Outgoing arcs (available actions) at {}:".format(node))
for arc in graph.outgoing_arcs(node):
    print ("  " + str(arc))