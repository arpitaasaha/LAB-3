def depthFirstSearch(problem):
    """
    Implements Depth-First Search (DFS) for the Pacman game.
    """
    from util import Stack
    stack = Stack()
    stack.push((problem.getStartState(), []))  # (current_state, path_to_state)
    visited = set()
    
    while not stack.isEmpty():
        state, actions = stack.pop()
        if state in visited:
            continue
        visited.add(state)
        
        if problem.isGoalState(state):
            return actions
        
        for successor, action, _ in problem.getSuccessors(state):
            if successor not in visited:
                stack.push((successor, actions + [action]))
    return []


def breadthFirstSearch(problem):
    """
    Implements Breadth-First Search (BFS) for the Pacman game.
    """
    from util import Queue
    queue = Queue()
    queue.push((problem.getStartState(), []))  # (current_state, path_to_state)
    visited = set()
    
    while not queue.isEmpty():
        state, actions = queue.pop()
        if state in visited:
            continue
        visited.add(state)
        
        if problem.isGoalState(state):
            return actions
        
        for successor, action, _ in problem.getSuccessors(state):
            if successor not in visited:
                queue.push((successor, actions + [action]))
    return []


def uniformCostSearch(problem):
    """
    Implements Uniform-Cost Search (UCS) for the Pacman game.
    """
    from util import PriorityQueue
    pq = PriorityQueue()
    pq.push((problem.getStartState(), [], 0), 0)  # (state, path_to_state, current_cost), priority
    visited = {}
    
    while not pq.isEmpty():
        state, actions, cost = pq.pop()
        if state in visited and visited[state] <= cost:
            continue
        visited[state] = cost
        
        if problem.isGoalState(state):
            return actions
        
        for successor, action, step_cost in problem.getSuccessors(state):
            new_cost = cost + step_cost
            pq.push((successor, actions + [action], new_cost), new_cost)
    return []
