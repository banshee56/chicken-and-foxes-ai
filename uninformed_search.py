
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

# input: goal SearchNode, once reached
# output: list/SearchSolution object path, representing the path taken from start to goal state
def backchain(node):
    path = []                           # the path resulting from backchaining
    curr_node = node                    # goal node

    while curr_node:
        curr_state = curr_node.state
        path.append(curr_state)         # add the state to the path
        curr_node = curr_node.parent    # move on to parent node

    # reverse the path we backchained
    solution = []                       # solution path from start to goal state
    i = len(path) - 1
    while i >= 0:
        solution.append(path[i])
        i -= 1
    
    return solution


# input: the problem containing relevant information, a FoxProblem object
# output: 
#        * on success: list, representing the path taken from start to goal state
#        * on failure: empty list
def bfs_search(search_problem):
    frontier = deque()
    start_node = SearchNode(search_problem.start_state)
    frontier.append(start_node)

    # setting up the SearchSolution obj
    solution = SearchSolution(search_problem, "bfs")

    # set to store visited states in
    visited = set()

    while frontier:
        curr_node = frontier.popleft()  # getting the first added state, FIFO
        curr_state = curr_node.state

        # using the problem's goal test function to check if we reached the goal
        if search_problem.goal_test(curr_state):
            solution.path = backchain(curr_node)            # success
            solution.nodes_visited = len(visited)
            return solution
        
        # get the successors to visit
        children = search_problem.get_successors(curr_state)

        for child in children:
            if child not in visited:
                visited.add(child)
                child_node = SearchNode(child, curr_node)   # create a successor node to add to the frontier
                frontier.append(child_node)

    solution.nodes_visited = len(visited)
    return solution                                         # failure


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
