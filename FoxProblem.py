# Name: Bansharee Ireen
#
# Description: A definition for the search_problem class
# 
# 30 Sep 2022
# COSC76, Fall 2022

from collections import deque

class FoxProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)
        self.chickens = start_state[0]      # number of chickens on the shore we're focusing on
        self.foxes = start_state[1]         # number of foxes on the shore we're focusing on
        
    # get successor states for the given state
    def get_successors(self, state):
        successors = []

        chickens = state[0]
        foxes = state[1]
        # boat = 1 means its on the curr shore, 0 means its on the other shore
        boat = state[2]
        if boat == 1:
            move_b = 0
        else:
            move_b = 1

        # possible moves when choosing 2 animals to move across the river
        moves = [(2, 0), (1, 0), (1, 1), (0, 1), (0, 2)]

        for move in moves:
            move_c = move[0]
            move_f = move[1]

            # boat 1 means we're moving animals away from the shore
            if boat == 1:
                # resulting tuple will have less animals
                res = ((chickens-move_c), (foxes-move_f), move_b)
            else:
                res = ((chickens+move_c), (foxes+move_f), move_b)

            # if the addition/subtraction produces a valid tuple
            if 0 <= res[0] and res[0] <= self.chickens and 0 <= res[1] and res[1] <= self.foxes:
                # if none of the chickens are eaten
                if (res[0] >= res[1] or res[0] == 0) and (self.chickens-res[0] >= self.foxes-res[1] or self.chickens-res[0]==0):
                    successors.append(res)

        return successors
    
    # I also had a goal test method. You should write one.
    def goal_test(self, state):
        return state==self.goal_state

    def __str__(self):
        string =  "Chickens and foxes problem: " + str(self.start_state)
        return string


## A bit of test code

if __name__ == "__main__":
    test_cp = FoxProblem((5, 4, 1))
    print(test_cp.get_successors((5, 5, 1)))
    print(test_cp)
