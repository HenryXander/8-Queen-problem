from Algoritmes.simulated_annealing import simulated_annealing as sa
from Algoritmes.hill_climbing import hill_climbing as hc
from Algoritmes.min_conflicts import min_conflicts as min_con
from Node import Node

class agent():
    def __init__(self, problem, heuristic, csp=None):
        self.problem = problem
        self.heuristic = heuristic
        self.csp = csp

    def simulated_annealing(self, schedule):
        return sa(self.problem, self.heuristic, schedule)

    def hill_climbing(self):
        return hc(self.problem, self.heuristic)

    def min_conflicts(self, max_steps=5000):
        csp_solution = min_con(self.csp, max_steps)
        if csp_solution != "Failure":
            solution_node = Node(self.problem, csp_solution, None, None, 0, 0)
            solution_node.set_h_value(self.heuristic(solution_node))
            return solution_node
        return "Failure"
