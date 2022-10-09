# Name: Bansharee Ireen
#
# Description: Some test runs for all three search techniques defined in uninformed_search.py
# 
# 30 Sep 2022
# COSC76, Fall 2022

from FoxProblem import FoxProblem
from uninformed_search import bfs_search, dfs_search, ids_search

# Create a few test problems:
problem111 = FoxProblem((1, 1, 1))
problem221 = FoxProblem((2, 2, 1))
problem321 = FoxProblem((3, 2, 1))
problem331 = FoxProblem((3, 3, 1))
problem541 = FoxProblem((5, 4, 1))
problem551 = FoxProblem((5, 5, 1))

# Run the searches.
#  Each of the search algorithms should return a SearchSolution object,
#  even if the goal was not found. If goal not found, len() of the path
#  in the solution object should be 0.

# my test cases
print(bfs_search(problem111))
print(dfs_search(problem111))
print(ids_search(problem111))
print('----------------------')

print(bfs_search(problem221))
print(dfs_search(problem221))
print(ids_search(problem221))
print('----------------------')

print(bfs_search(problem321))
print(dfs_search(problem321))
print(ids_search(problem321))
print('----------------------')

# given test cases
print(bfs_search(problem331))
print(dfs_search(problem331))
print(ids_search(problem331))
print('----------------------')

# 541 with too small a depth limit to find solution
print(bfs_search(problem541))
print(dfs_search(problem541))
print(ids_search(problem541, 9))
print('----------------------')

# 541 with large enough (default) depth limit
print(bfs_search(problem541))
print(dfs_search(problem541))
print(ids_search(problem541))
print('----------------------')

print(bfs_search(problem551))
print(dfs_search(problem551))
print(ids_search(problem551))
