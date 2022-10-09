# Name: Bansharee Ireen
#
# Description: A collection of search techniques with a definition for the SearchNode class
# 
# 30 Sep 2022
# COSC76, Fall 2022

from collections import deque
from SearchSolution import SearchSolution

class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
    
    # getter method for state
    def get_state(self):
        return self.state

    # getter method for 
    def get_parent(self):
        return self.parent

# used by bfs_search once a path to goal is found
# input: goal SearchNode, once reached
# output: list/SearchSolution object path, representing the path taken from start to goal state
def backchain(node):
    path = []                               # the path resulting from backchaining
    curr_node = node                        # goal node

    # traverse through the parents to place nodes in preliminary path
    while curr_node:
        curr_state = curr_node.get_state()
        path.append(curr_state)             # add the state to the path
        curr_node = curr_node.get_parent()  # move on to parent node

    # reverse the path we backchained
    solution = []                           # solution path from start to goal state
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
    start_node = SearchNode(search_problem.start_state)

    # deque used as FIFO queue to hold the nodes in order
    frontier = deque()
    frontier.append(start_node)

    # set to store visited states in
    visited = set()
    visited.add(search_problem.start_state)

    # setting up the SearchSolution obj
    solution = SearchSolution(search_problem, "BFS")

    while frontier:
        curr_node = frontier.popleft()  # getting the first added state, FIFO
        curr_state = curr_node.get_state()

        # using the problem's goal test function to check if we reached the goal
        if search_problem.goal_test(curr_state):
            solution.path = backchain(curr_node)            # success
            solution.nodes_visited = len(visited)
            return solution
        
        # get the successors to visit
        children = search_problem.get_successors(curr_state)

        # go through the children
        for child in children:
            if child not in visited:
                visited.add(child)
                child_node = SearchNode(child, curr_node)   # create a successor node to add to the frontier
                frontier.append(child_node)

    solution.nodes_visited = len(visited)
    return solution                                         # failure


# path checking function to help dfs_search keep track of nodes on current path
# input:
#       * check_node: node under inspection, to check if we've visited it before
#       * curr_node: the node we are comparing check_node to
# output:
#       * True -> have seen check_node on current path before
#       * False -> first time seeing check_node on current path
def path_checking(check_node, curr_node):
    # check if the nodes are the same
    if check_node.get_state() == curr_node.get_state():
        return False

    # if we reached the end of the path, i.e. got to the start
    # then there are no other duplicate nodes
    elif curr_node.get_parent() is None:
        return True
    
    # recurse until we either reach the start_state or until we find duplicate check_node
    return path_checking(check_node, curr_node.get_parent())


# input:
#       * depth_limit: keeps the dfs from going on when given an infinite graph
# output: returns the solution, a SearchSolution object
def dfs_search(search_problem, node=None, solution=None, depth_limit=100):
    # if no node object given, create a new search from starting state
    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS")
    
    # getting the state and adding to putting it on our path
    curr_state = node.get_state()
    solution.path.append(curr_state)
    solution.nodes_visited += 1

    # Base Case 1: hit the depth_limit
    if len(solution.path) > depth_limit:    # stops dfs from going on forever, and ids uses it for its iterative limit
        solution.path.pop()                 # we don't need the last added state because it exceeds the depth limit
        return solution

    # Base Case 2: if current node is the goal, return it
    if search_problem.goal_test(curr_state):
        return solution
    
    # get the successors of the node just added to the path
    children = search_problem.get_successors(curr_state)

    for child in children:
        child_node = SearchNode(child, node)

        if path_checking(child_node, node):
            # visit child node
            solution = dfs_search(search_problem, child_node, solution, depth_limit)

            # the child led us to the goal, so return the path so far
            if search_problem.goal_test(solution.path[-1]):
                return solution

    # went through the kids and didn't return solution, so just pop the state and return up
    solution.path.pop()
    return solution

# inputs:
#       * depth_limit: the max limit we will incremement each iteration's depth to
# output: returns the solution, a SearchSolution object
def ids_search(search_problem, depth_limit=100):
    curr_limit = 0                                          # the limit to compare the depth_limit to

    # setting up the start node and solution
    # as this node gets passed to dfs_search, it does not trigger the dfs initialization of the solution
    node = SearchNode(search_problem.start_state, None)
    solution = SearchSolution(search_problem, "IDS")

    while curr_limit < depth_limit:
        solution = dfs_search(search_problem, node, solution, curr_limit)

        # if we received a valid solution, return it
        if len(solution.path) > 0 and search_problem.goal_test(solution.path[-1]):
            return solution
        curr_limit += 1

    # if no valid solution was found after depth_limit exceeded, return findings
    return solution
