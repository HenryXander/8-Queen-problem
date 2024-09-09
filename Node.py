class ExceptionsNode(Exception):
    pass



class Node():
    def __init__(self, problem, state, parent, action_from_parent, path_cost, depth):
        self.problem = problem
        self.state = state
        self.action_from_parent = action_from_parent
        self.parent = parent
        self.depth = depth
        self.g_value = path_cost
        self.h_value = None
        self.f_value = path_cost
        self.children = []

    def get_value(self, relevant_cost):
        if relevant_cost == "g":
            return self.g_value
        elif relevant_cost == "h":
            return self.h_value
        elif relevant_cost == "gh":
            return self.f_value
        else:
            raise ExceptionsNode("Can't return value. Relevant_cost parameter is ill defined")

    def get_child_node_from_action(self, action):
        child_node = Node(self.problem, self.problem.result(self.state, action), self, action, self.g_value + self.problem.step_cost(self.state, action), self.depth + 1)
        self.children.append(child_node)
        return child_node

    def get_successors(self):
        successor_nodes = []
        for successor_state in self.problem.transition_model.get_successors(self):
            successor_node = Node(self.problem, successor_state, self, "", self.g_value + self.problem.transition_model.step_cost(self.state, successor_state), self.depth + 1)
            successor_nodes.append(successor_node)
        return successor_nodes

    def set_h_value(self, h_value):
        self.h_value = h_value
        self.f_value = self.g_value + self.h_value #update f value

    def set_f_value(self, f_value):
        self.f_value = f_value