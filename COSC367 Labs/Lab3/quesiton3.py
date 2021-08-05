import re
from search import *


def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 31 Jul 2019

    """
    ATOM = r"[a-z][a-zA-z\d_]*"
    HEAD = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


class KBGraph(Graph):
    """
    The node are a list containing the body (eg if yes <- B^C) node = [b,c]
    You want to dfs through the graph replacing each part of the node with a different body from the clauses
    """

    def __init__(self, kb, query):
        self.clauses = list(clauses(kb))
        self.query = query

    def starting_nodes(self):
        """Returns a list of the start query nodes"""
        return [self.query]

    def is_goal(self, node):
        """
        The goal is when the node is yes <-
        That means the list node must be empty (no body)
        """
        if len(node)==0:
            return True
        return False

    def outgoing_arcs(self, tail_node):
        """
        Here you want to get the tail_node list (of heads) and go through the clauses to find bodies to replace the head with
        Cycle through the list in tail_node (the current query)
        For each node go through the clauses and find bodies to replace the head with and return as an arc
        :param tail_node:
        :return:
        """
        arcs = []
        for t in tail_node:
            for c in self.clauses:
                if c[0] == t:
                    arcs.append(Arc(t, c[1], str(tail_node) + '->' + str(c[1]), 1))
        return arcs

class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        # search will add and remove. This deals w how you add and remove
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop()
        else:
            raise StopIteration  # don't change this one

kb = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

query = {'a'}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")

kb = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

query = {'a', 'b', 'd'}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")

kb = """
all_tests_passed :- program_is_correct.
all_tests_passed.
"""

query = {'program_is_correct'}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")

kb = """
a :- b.
"""

query = {'c'}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")