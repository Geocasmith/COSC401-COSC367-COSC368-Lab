import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM   = r"[a-z][a-zA-Z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")

def forward_deduce(kb):
    clausesList = []
    startingLength = len(clausesList)
    endingLength = len(clausesList)+1
    while(startingLength!=endingLength):
        #Gets length at start
        startingLength = len(clausesList)
        for c in list(clauses(kb)):
            if not (c[0] in clausesList):
                if len(c[1])==0: #if no body then add
                    clausesList.append(c[0])
                elif all(b in clausesList for b in c[1]): #if all body members are in clause list C
                    clausesList.append(c[0])

        #if no clauses added then stops loop
        endingLength = len(clausesList)

    return clausesList
kb = """
a :- b.
b.
"""

print(", ".join(sorted(forward_deduce(kb))))

kb = """
good_programmer :- correct_code.
correct_code :- good_programmer.
"""

print(", ".join(sorted(forward_deduce(kb))))

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


print(", ".join(sorted(forward_deduce(kb))))