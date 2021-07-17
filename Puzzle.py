from Node import Node

class Puzzle():

    def __init__(self, startState):
        self.Nodes = []
        self.start = Node(0, 4, startState, startState, True)
        self.selectedNode = self.start

    def selectNext(self):
        self.expand()
        self.selectedNode = self.Nodes[0]
        self.Nodes = self.Nodes[1:]
        if self.checkGoal() == True:
            return True
        else:
            return False


    def expand(self):
        self.selectedNode.expand()
        children = self.selectedNode.getChildren()
        for i in range(0, len(children), 1):
            if self.isDuplicate(children[i]) == False:
                self.Nodes.append(children[i])
        self.order()

    def isDuplicate(self, node):
        for i in range(0, len(self.Nodes), 1):
            if self.Nodes[i].getState() == node.getState():
                return True
        return False


    def order(self):
        i = 0
        while i < len(self.Nodes) - 1:
            costfirst = self.Nodes[i].getCost()
            costnext = self.Nodes[i + 1].getCost()
            if costfirst > costnext:
                h = self.Nodes[i]
                self.Nodes[i] = self.Nodes[i + 1]
                self.Nodes[i + 1] = h
                i = 0
            else:
                i += 1

    def checkGoal(self):
        if self.selectedNode.getCost() == 0:
            return True
        return False

    def getSelected(self):
        return self.selectedNode

    def getPath(self):
        start = False
        sequence = []
        self.selectedNodeBack = self.selectedNode
        while (start == False):
            parent = self.selectedNodeBack.getParent()
            sequence.append(parent.getState())
            self.selectedNodeBack = parent
            start = self.selectedNodeBack.checkStart()
        return sequence

    def printNodes(self):
        for i in range(0, len(self.Nodes), 1):
            self.Nodes[i].print()
