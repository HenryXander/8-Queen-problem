import math

def get_best_successor(successors, heuristic):
    if successors:
        best_successor = None
        lowest_value = math.inf
        for successor in successors:
            value = heuristic(successor)
            successor.set_h_value(value)
            if value < lowest_value:
                best_successor = successor
                lowest_value = value
        return best_successor
    else:
        return None

def hill_climbing(problem, heuristic):
    current_node = problem.initial_node
    current_node.set_h_value(heuristic(current_node))

    while True:
        successors = problem.get_successors(current_node)
        next_node = get_best_successor(successors, heuristic)

        if next_node.h_value > current_node.h_value:
            return current_node
        else:
            current_node = next_node