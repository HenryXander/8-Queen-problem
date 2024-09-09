import Node

class local_search_problem():
    def __init__(self, initial_state, transition_model):
        self.transition_model = transition_model
        self.initial_state = initial_state
        self.initial_node = Node.Node(self, initial_state, None, None, 0, 0)

    def get_successors(self, node):
        successors = []
        actions = self.transition_model.get_actions(node)
        for action in actions:
            successor = node.get_child_node_from_action(action)
            successors.append(successor)
        return successors

    def result(self, state, action): # of node ipv state
        return self.transition_model.result(state, action)

    def step_cost(self, state, action):
        return self.transition_model.step_cost(state, action)