
from collections import deque
import queue
from SearchSolution import SearchSolution

# you might find a SearchNode class useful to wrap state objects,
#  keep track of current depth for the dfs, and point to parent nodes
class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, parent=None):
        # you write this part
        self.state = state
        self.parent = parent

# you might write other helper functions, too. For example,
#  I like to separate out backchaining, and the dfs path checking functions
def backchain(node):
    path = []
    curr_node = node

    while curr_node:
        curr_state = curr_node.state
        path.append(curr_state)
        curr_node = curr_node.parent

    solution = []
    i = len(path) - 1
    while i >= 0:
        solution.append(path[i])
        i -= 1
    
    return solution



def bfs_search(search_problem):
    frontier = deque()
    start_node = SearchNode(search_problem.start_state)
    frontier.append(start_node)

    # dictionary to store visited states in
    visited = {}

    while frontier:
        curr_node = frontier.popleft()  # getting the first added state
        curr_state = curr_node.state

        if search_problem.goal_test(curr_state):
            return backchain(curr_node)
        
        visited[curr_state] = ''
        children = search_problem.get_successors(curr_state)
        for child in children:
            if child not in visited:
                child_node = SearchNode(child, curr_node)
                frontier.append(child_node)
    
    return None 


# Don't forget that your dfs function should be recursive and do path checking,
#  rather than memoizing (no visited set!) to be memory efficient

# We pass the solution along to each new recursive call to dfs_search
#  so that statistics like number of nodes visited or recursion depth
#  might be recorded
def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    # if no node object given, create a new search from starting state
    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS")

    # you write this part



# def ids_search(search_problem, depth_limit=100):
    # you write this part
