# CSPs
----

[CS188](https://inst.eecs.berkeley.edu/~cs188/fa18/)

Constraint Satisfaction Problems, example: Map Coloring

Variables: WA, NT, Q, NSW, V, SA, T
Domains: D = {red, green, blue}
Constraints: adjacent regions must have different colors

![[Archive/面试资料/Programming/_resources/CSPs.resources/unknown_filename.png]]![[Archive/面试资料/Programming/_resources/CSPs.resources/unknown_filename.1.png]](constraint graphs)


Real-World CSPs

1.  Scheduling problems: e.g., when can we all meet?
2.  Timetabling problems: e.g., which class is offered when and where?
3.  Assignment problems: e.g., who teaches what class
4.  Hardware configuration
5.  Transportation scheduling
6.  Factory scheduling
7.  Circuit layout
8.  Fault diagnosis
9.  … lots more!


Backtracking Search

1.  Filtering: Can we detect inevitable failure early?
    1.  Forward checking: Cross off values that violate a constraint when added to the existing assignment, it propagates information from assigned to unassigned variables, but doesn't provide early detection for all failures
    2.  Arc Consistency: An arc X → Y is consistent iff for every x in the tail there is some y in the head which could be assigned without violating a constraint
        1.  one simple form of propagation makes sure all arcs are consistent => must rerun after each assignment.
2.  Ordering: Which variable should be assigned next? In what order should its values be tried?
    1.  MRV: Minimum Remaining Values, Choose the variable with the fewest legal left values in its domain => fail fast
    2.  LCV: Least Constraining Value, I.e., the one that rules out the fewest values in the remaining variables => don't need try all value, but need fit all variables, try the easy mode first
3.  Structure: Can we exploit the problem structure?
    1.  Tree-Structured CSPs
        1.  Runtime: O(n d^2)
    2.  Nearly Tree-Structured CSPs
        1.  Cutset conditioning: instantiate (in all ways) a set of variables such that the remaining constraint graph is a tree
        2.  Cutset size c gives runtime O( (d^c ) (n-c) d^2 ), very fast for small c


Iterative Algorithm

1.  Take an assignment with unsatisfied constraints
    1.  Variable selection: randomly select any conflicted variable
    2.  min-conflicts heuristic: Choose a value that violates the fewest constraints
2.  Operators reassign variable values
3.  No fringe! Live on the edge



Summary: CSPs

1.  CSPs are a special kind of search problem
    1.  States are partial assignments
    2.  Goal test defined by constraints
2.  Basic solution: backtracking search
3.  Speed-ups:
    1.  Ordering
    2.  Filtering
    3.  Structure
4.  Iterative min-conflicts is often effective in practice



Tree search keeps unexplored alternatives on the fringe (ensures completeness)
Local Search 

1.  improve a single option until you can’t make it better (no fringe!)
2.  Generally much faster and more memory efficient (but incomplete and suboptimal)
    1.  no guarantee to reach global maximum
3.  Simulated Annealing: e.g. hill climbing, escape local maxima by allowing downhill moves
4.  



----

- Date: 2019-09-15
- Tags: #Interview/Programing 



