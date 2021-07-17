class Node():
    def __init__(self, depth, previous, state, parent, start):
        self.cost = self.heuristic(state)
        self.state = state
        self.posblank = self.posbepaling()
        self.previous = previous
        self.depth = depth
        self.parent = parent
        self.start = start
        self.children = []

    def heuristic(self, state):  # manhattan distance as heuristic function
        sum = 0
        for i in range(0, len(state), 1):
            if state[i] != 0:
                if i < 3:
                    Y = 2
                elif 2 < i < 6:
                    Y = 1
                else:
                    Y = 0
                if i == 0 or i == 3 or i == 6:
                    X = 0
                elif i == 1 or i == 4 or i ==7:
                    X = 1
                else:
                    X = 2
                distance = self.manhattandistance(X, Y, state[i])
                sum += distance
        return sum
    def manhattandistance(self, X, Y, cijfer):
        Xgoal = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        Ygoal = [2, 2, 2, 1, 1, 1, 0, 0, 0]
        x = Xgoal[cijfer]
        y = Ygoal[cijfer]
        distance = abs(X - x) + abs(Y - y)
        return distance

    def posbepaling(self):
        for i in range(0, len(self.state), 1):
            if self.state[i] == 0:
                return i

    def expand(self):
        if self.canUp() == True:
            stateUp = self.state.copy()
            h = stateUp[self.posblank - 3]
            stateUp[self.posblank - 3] = 0
            stateUp[self.posblank] = h

            child = Node(self.depth + 1, 0, stateUp, self, False)
            self.children.append(child)
        if self.canRight() == True:
            stateRight = self.state.copy()
            h = stateRight[self.posblank + 1]
            stateRight[self.posblank + 1] = 0
            stateRight[self.posblank] = h

            child = Node(self.depth + 1, 1, stateRight, self, False)
            self.children.append(child)
        if self.canDown() == True:
            stateDown = self.state.copy()
            h = stateDown[self.posblank + 3]
            stateDown[self.posblank + 3] = 0
            stateDown[self.posblank] = h

            child = Node(self.depth + 1, 2, stateDown, self, False)
            self.children.append(child)
        if self.canLeft() == True:
            stateLeft = self.state.copy()
            h = stateLeft[self.posblank - 1]
            stateLeft[self.posblank - 1] = 0
            stateLeft[self.posblank] = h

            child = Node(self.depth+ 1, 3, stateLeft, self, False)
            self.children.append(child)

    def canUp(self):
        if self.previous == 2:
            return False
        if self.posblank < 3:
            return False
        return True
    def canRight(self):
        if self.previous == 3:
            return False
        if self.posblank == 2 or self.posblank == 5 or self.posblank == 8:
            return False
        return True
    def canDown(self):
        if self.previous == 0:
            return False
        if self.posblank > 5:
            return False
        return True
    def canLeft(self):
        if self.previous == 1:
            return False
        if self.posblank == 0 or self.posblank == 3 or self.posblank == 6:
            return False
        return True

    def getChildren(self):
        return self.children

    def getCost(self):
        if self.cost == 0:
            return self.cost
        return self.cost + self.depth

    def getParent(self):
        return self.parent

    def checkStart(self):
        if self.start == True:
            return True
        return False

    def getState(self):
        return self.state

    def print(self):
        print(self.state, end=' ')
        print(self.cost)

    def getPrevious(self):
        return self.previous

    def getDepth(self):
        return self.depth