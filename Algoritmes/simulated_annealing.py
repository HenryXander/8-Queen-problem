import math
import random

def simulated_annealing(problem, heuristic, schedule):
    current_node = problem.initial_node
    current_node.set_h_value(heuristic(current_node))

    t = 1
    while t > 0:
        temp = schedule(t)

        if temp == 0:
            #print(t)
            return current_node

        successors = problem.get_successors(current_node)
        next_node = random.choice(successors)
        next_node.set_h_value(heuristic(next_node))

        delta_E = next_node.h_value - current_node.h_value #local search dus g waarde boeit niet, enkel h waarde
        if delta_E < 0:
            current_node = next_node
        else:
            probability_treshold = math.exp(-delta_E/temp)
            probability = random.random()
            if probability <= probability_treshold:
                current_node = next_node
        t += 1