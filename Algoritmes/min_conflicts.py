import random
import math

def min_conflicts(csp, max_steps=10000):
    current_assignment = {var: random.choice(csp.D[var]) for var in csp.X} #has to be complete
    for i in range(0, max_steps):
        if csp.valid(current_assignment):
            return current_assignment
        var = get_random_conflicted_var(current_assignment, csp)
        value = get_min_conflict_value(var, current_assignment, csp)
        current_assignment[var] = value
    return current_assignment

def count_conflicts(var, value, assignment, csp):
    count = 0
    for neighbor in csp.get_neighbors(var):
        constraint = csp.get_binary_constraint(var, neighbor)
        if constraint is not None:
            if not constraint(var, neighbor, value, assignment[neighbor]):
                count += 1
    return count

def get_random_conflicted_var(assignment, csp):
    conflicted_vars = []
    for var, value in assignment.items():
        for neighbor in csp.get_neighbors(var):
            constraint = csp.get_binary_constraint(var, neighbor)
            if constraint is not None:
                if not constraint(var, neighbor, value, assignment[neighbor]):
                    conflicted_vars.append(var)
                    break
    return random.choice(conflicted_vars)

def get_min_conflict_value(var, assignment, csp):
    min_values = []
    min_count = math.inf
    for value in csp.D[var]:
        count = count_conflicts(var, value, assignment, csp)
        if count < min_count:
            min_count = count
            min_values = [value]
        elif count == min_count:
            min_values.append(value)
    return random.choice(min_values)