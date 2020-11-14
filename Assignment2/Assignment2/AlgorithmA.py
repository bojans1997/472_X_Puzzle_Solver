from queue import PriorityQueue
import time

timeout = time.time() + 60
puzzles = []
with open('../../Downloads/472_Assignment2-Sunny 2/Assignment2/Assignment2/Resources/testpuzzle.txt') as f:
    for line in f:
        puzzles.append([int(i) for i in line.split()])

target_state = [[1,2,3,4,5,6,7,0], [1,3,5,7,2,4,6,0]]


# get all possible state in 1 move starting from the passed state
def getNeighborStates(list):
    initial_list = list[0].copy()
    new_state = list[0].copy()
    neighbor_states = []

    zero_index = initial_list.index(0)

    if zero_index != 0 and zero_index != 3 and zero_index != 4 and zero_index != 7:
        new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
        neighbor_states.append([new_state, initial_list, 1, new_state[zero_index]])
        new_state = initial_list.copy()

        new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
        neighbor_states.append([new_state, initial_list, 1, new_state[zero_index]])
        new_state = initial_list.copy()

        if zero_index > 3:
            new_state[zero_index], new_state[zero_index - 4] = new_state[zero_index - 4], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1, new_state[zero_index]])
            new_state = initial_list.copy()
        else:
            new_state[zero_index], new_state[zero_index + 4] = new_state[zero_index + 4], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1, new_state[zero_index]])
            new_state = initial_list.copy()
    else:
        if zero_index == 0:
            new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1, new_state[zero_index]])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index + 4] = new_state[zero_index + 4], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1, new_state[zero_index]])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 2, new_state[zero_index]])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index + 5] = new_state[zero_index + 5], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 3, new_state[zero_index]])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index + 7] = new_state[zero_index + 7], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 3, new_state[zero_index]])
            new_state = initial_list.copy()
        elif zero_index == 3:
            new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1, new_state[zero_index]])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index + 4] = new_state[zero_index + 4], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1, new_state[zero_index]])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 2, new_state[zero_index]])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 3, new_state[zero_index]])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 3, new_state[zero_index]])
            new_state = initial_list.copy()
        elif zero_index == 4:
            new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1, new_state[zero_index]])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index - 4] = new_state[zero_index - 4], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1, new_state[zero_index]])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 2, new_state[zero_index]])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 3, new_state[zero_index]])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 3, new_state[zero_index]])
            new_state = initial_list.copy()
        else:
            new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1, new_state[zero_index]])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index - 4] = new_state[zero_index - 4], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1, new_state[zero_index]])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 2, new_state[zero_index]])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index - 5] = new_state[zero_index - 5], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 3, new_state[zero_index]])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index - 7] = new_state[zero_index - 7], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 3, new_state[zero_index]])
            new_state = initial_list.copy()
    return neighbor_states


# if empty tile is at bottom right corner, hn = 0, else hn = 1
def getDemoHeuristic(state):
    zero_index = state.index(0)
    if (zero_index == 7):
        return 0
    else:
        return 1


# count how many tiles are in the wrong position relative to solution 1
def getFirstHeuristic(state):
    misplacedTiles = 0
    index = 0
    for num in state:
        if state[index] != target_state[0][index]:
            misplacedTiles += 1
        index += 1
    return misplacedTiles


# count how many tiles are in the wrong position relative to solution 2
def getSecondHeuristic(state):
    misplacedTiles = 0
    index = 0
    for num in state:
        if state[index] != target_state[1][index]:
            misplacedTiles += 1
        index += 1
    return misplacedTiles


def algorithmA(heuristic=1):
    puzzle_num = -1
    for puzzle in puzzles:
        start_time = time.time()
        solution_found = False
        current_state = puzzle
        previous_state = []
        num_moves = 0

        open_list = PriorityQueue()
        open_list.put((0, [current_state, previous_state, 0, 0]))
        dupe_check = [current_state]
        closed_list = []
        test = 0

        while not open_list.empty():
            if time.time() - start_time > timeout:
                break
            test += 1
            current_state = open_list.get()
            closed_list.append(current_state)
            if current_state[1][0] == target_state[0] or current_state[1][0] == target_state[1]:
                solution_found = True
                break
            neighbor_states = getNeighborStates(current_state[1])

            for state in neighbor_states:
                found = False
                for closed_state in closed_list:
                    if closed_state[1][0] == state[0]:
                        found = True
                        break
                        # check if it was a visited state
                    if state[0] in dupe_check:
                        found = True
                        break
                        tempList = []
                        temp_openList = open_list
                        while not temp_openList.empty():
                           itemToSave = temp_openList.get()
                           tempList.append(itemToSave)
                           isRemovingItem = False
                           for item in tempList:
                                if state[0] == item[1][0]:
                                     if state[2] + current_state[0] < item[0]:
                                        itemToRemove = item
                                        isRemovingItem = True
                                        found = True
                                        priority1 = state[2] + current_state[0]
                                        if (heuristic == 0):
                                            priority2 = getDemoHeuristic(state[0])
                                        elif (heuristic == 1):
                                            priority2 = getFirstHeuristic(state[0])
                                        else:
                                            priority2 = getSecondHeuristic(state[0])
                                        priority = priority1 + priority2
                                        open_list.put((priority, state))
                                        dupe_check.append(state[0])
                           if isRemovingItem:
                                tempList.remove(itemToRemove)
                                open_list = temp_openList
                    if not found:
                        priority1 = state[2] + current_state[0]
                        if (heuristic == 0):
                            priority2 = getDemoHeuristic(state[0])
                        elif (heuristic == 1):
                            priority2 = getFirstHeuristic(state[0])
                        else:
                            priority2 = getSecondHeuristic(state[0])
                        priority = priority1 + priority2
                        open_list.put((priority, state))
                        dupe_check.append(state[0])

        # write solution steps to file
        puzzle_num += 1
        if solution_found:
            total_cost = 0
            solution_path = []
            parent = closed_list[-1][1][0]
            while parent:
                full_state = []
                for closed_state in closed_list:
                    if parent == closed_state[1][0]:
                        parent = closed_state[1][1]
                        full_state = closed_state
                        total_cost += closed_state[1][2]

                solution_path.append(full_state)
            f = open(str(puzzle_num) + "_algoA-h" + str(heuristic) + "_solution.txt", "w")
            for solution_state in reversed(solution_path):
                st = ""
                for i in solution_state[1][0]:
                    st += str(i) + " "
                f.write(str(solution_state[1][3]) + " " + str(solution_state[1][2]) + " " + st)
                f.write("\n")
            f.write("Total cost: " + str(total_cost) + " Execution time: " + str(time.time() - start_time))
            f.close()
            # write search path to file
            f = open(str(puzzle_num) + "_algoA-h" + str(heuristic) + "_search.txt", "w")
            for state in closed_list:
                fn = str(0) + " "
                gn = str(0) + " "
                hn = str(state[0]) + " "
                st = ""
                for i in state[1][0]:
                    st += str(i) + " "
                f.write(fn + gn + hn + st)
                f.write("\n")
            f.close()
        else:
            f = open(str(puzzle_num) + "_algoA-h" + str(heuristic) + "_solution.txt", "w")
            f.write("No solution")
            f.close()
            f = open(str(puzzle_num) + "_algoA-h" + str(heuristic) + "_search.txt", "w")
            f.write("No solution")
            f.close()

algorithmA(1)




