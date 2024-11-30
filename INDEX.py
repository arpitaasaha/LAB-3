import util
import time


class SearchProblem:
   

    def getStartState(self):
        util.raiseNotDefined()

    def isGoalState(self, state):
        util.raiseNotDefined()

    def getSuccessors(self, state):
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Implements DFS for Pacman.
    """
    stack = util.Stack()  # Frontier as a stack
    stack.push((problem.getStartState(), []))
    visited = set()

    while not stack.isEmpty():
        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)

        if problem.isGoalState(state):
            return path

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                stack.push((successor, path + [action]))

    return []


def breadthFirstSearch(problem):
    """
    Implements BFS for Pacman.
    """
    queue = util.Queue()  # Frontier as a queue
    queue.push((problem.getStartState(), []))
    visited = set()

    while not queue.isEmpty():
        state, path = queue.pop()

        if state in visited:
            continue

        visited.add(state)

        if problem.isGoalState(state):
            return path

        for successor, action, stepCost in problem.getSuccessors(state):
            if successor not in visited:
                queue.push((successor, path + [action]))

    return []


def uniformCostSearch(problem):
    """
    Implements UCS for Pacman.
    """
    priority_queue = util.PriorityQueue()
    priority_queue.push((problem.getStartState(), []), 0)
    visited = {}

    while not priority_queue.isEmpty():
        state, path = priority_queue.pop()
        cost = problem.getCostOfActions(path)

        if state in visited and visited[state] <= cost:
            continue

        visited[state] = cost

        if problem.isGoalState(state):
            return path

        for successor, action, stepCost in problem.getSuccessors(state):
            new_cost = cost + stepCost
            priority_queue.push((successor, path + [action]), new_cost)

    return []