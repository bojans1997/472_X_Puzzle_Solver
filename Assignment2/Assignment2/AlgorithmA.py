from queue import PriorityQueue
import time

timeout = 60

total_solution_path = 0
total_search_path = 0
total_no_solution = 0
total_final_cost = 0
total_execution_time = time.time()

puzzles = []
with open('Resources/50puzzles.txt') as f:
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


# count how many tiles are in the wrong position relative to both solutions, and return the lowest value
def getFirstHeuristic(state):
    misplacedTiles = 0
    index = 0
    firstCost = 0
    for num in state:
        if state[index] != target_state[0][index]:
            misplacedTiles += 1
        index += 1
    firstCost = misplacedTiles

    misplacedTiles = 0
    index = 0
    for num in state:
        if state[index] != target_state[1][index]:
            misplacedTiles += 1
        index += 1
    if misplacedTiles < firstCost:
        return misplacedTiles
    else:
        return firstCost

# count number of tiles in wrong row relative to both solutions, and return the lowest value
def getSecondHeuristic(state):
    wrongRow = 0
    index = 0
    firstCost = 0
    for num in state:
        if num > 0 and num <= 4 and index > 3:
            wrongRow += 1
        elif (num == 0 or num > 4) and index <= 3:
            wrongRow += 1
        index += 1
    firstCost = wrongRow

    wrongRow = 0
    index = 0
    for num in state:
        if (num == 1 or num == 3 or num == 5 or num == 7) and index > 3:
            wrongRow += 1
        elif (num == 2 or num == 4 or num == 6 or num == 0) and index <= 3:
            wrongRow += 1
        index += 1
    if wrongRow < firstCost:
        return wrongRow
    else:
        return firstCost


def algorithmA(heuristic=1):
    global timeout
    global total_solution_path
    global total_search_path
    global total_no_solution
    global total_final_cost
    global total_execution_time

    puzzle_num = -1
    for puzzle in puzzles:
        start_time = time.time()
        solution_found = False
        current_state = puzzle
        previous_state = []
        num_moves = 0

        open_list = PriorityQueue()
        open_list.put((0, [current_state, previous_state, 0, 0], 0, 0))
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
                        if state[0] in dupe_check:
                            dupe_check.remove(state[0])
                        break
                        # check if it was a visited state
                if state[0] in dupe_check:
                    found = True
                    tempList = []
                    foundBetterPath = False
                    while not open_list.empty():
                        itemToSave = open_list.get()
                        if state[0] == itemToSave[1][0] and itemToSave[0] > state[2] + current_state[0]:
                            foundBetterPath = True
                            break
                        else:
                            tempList.append(itemToSave)
                    if foundBetterPath:
                        g = state[2] + current_state[0]
                        if (heuristic == 0):
                            h = getDemoHeuristic(state[0])
                        elif (heuristic == 1):
                            h = getFirstHeuristic(state[0])
                        else:
                            h = getSecondHeuristic(state[0])
                        priority = g + h
                        open_list.put((priority, state, g, h))

                    for item in tempList:
                        open_list.put((item[0], item[1], item[2], item[3]))

                if not found:
                    g = state[2] + current_state[0]
                    if (heuristic == 0):
                        h = getDemoHeuristic(state[0])
                    elif (heuristic == 1):
                        h = getFirstHeuristic(state[0])
                    else:
                        h = getSecondHeuristic(state[0])
                    priority = g + h
                    open_list.put((priority, state, g, h))
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
            f = open("Astar-results/" + str(puzzle_num) + "_astar-h" + str(heuristic) + "_solution.txt", "w")
            for solution_state in reversed(solution_path):
                st = ""
                for i in solution_state[1][0]:
                    st += str(i) + " "
                f.write(str(solution_state[1][3]) + " " + str(solution_state[1][2]) + " " + st)
                f.write("\n")
            f.write("Total cost: " + str(total_cost) + " Execution time: " + str(time.time() - start_time))
            f.close()
            total_final_cost += total_cost
            total_solution_path += len(solution_path)
            total_search_path += len(closed_list)
            # write search path to file
            f = open("Astar-results/" + str(puzzle_num) + "_astar-h" + str(heuristic) + "_search.txt", "w")
            for state in closed_list:
                fn = str(state[0]) + " "
                gn = str(state[2]) + " "
                hn = str(state[3]) + " "
                st = ""
                for i in state[1][0]:
                    st += str(i) + " "
                f.write(fn + gn + hn + st)
                f.write("\n")
            f.close()
        else:
            f = open("Astar-results/" + str(puzzle_num) + "_astar-h" + str(heuristic) + "_solution.txt", "w")
            f.write("No solution")
            f.close()
            f = open("Astar-results/" + str(puzzle_num) + "_astar-h" + str(heuristic) + "_search.txt", "w")
            f.write("No solution")
            f.close()
            total_no_solution += 1

algorithmA(1)

total_execution_time = time.time() - total_execution_time

print("avg solution length: " + str(total_solution_path / 50))
print("total solution length: " + str(total_solution_path))
print("avg search length: " + str(total_search_path / 50))
print("total search length: " + str(total_search_path))
print("total no solution: " + str(total_no_solution))
print("avg cost: " + str(total_final_cost / 50))
print("total cost: " + str(total_final_cost))
print("avg execution time: " + str(total_execution_time / 50))
print("total execution time: " + str(total_execution_time))