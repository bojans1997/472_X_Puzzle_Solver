from queue import PriorityQueue
import time

timeout = time.time() + 60

puzzle_file = open("Resources/sampleBoards.txt")
puzzles = []
with open('Resources/sampleBoards.txt') as f:
    for line in f:
        puzzles.append([int(i) for i in line.split()])
print(puzzles)

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


    """
    Repeat following:
    Sort PQ <-- automatically done by python when adding to PQ
    If 2 nodes have same costs, just choose an arbitary one to put as first
     is it goal state? if no = continue, else end.
    Expand first one in queue.
   
        If you find a shorter path waiting in open list, replace with a new shorter path in PQ
        # old (heuristic_value, [[current_state], [parent_state], cost, tile_moved])
        # new (totalCost, [[current_state], [parent_state], cost, tile_moved])
   """
def ucs():
    puzzle_num = -1
    for puzzle in puzzles:
        start_time = time.time()
        solution_found = False
        current_state = puzzle
        previous_state = []
        num_moves = 0
        open_list = PriorityQueue()
        # old (heuristic_value, [[current_state], [parent_state], cost, tile_moved])
        # new (totalCost, [[current_state], [parent_state], cost, tile_moved])
        open_list.put((0, [current_state, previous_state, 0,0]))
        dupe_check = [current_state]
        closed_list = []
        test = 0

        while not open_list.empty():
            if time.time() - start_time > timeout:
                break
            test += 1
            current_state = open_list.get()
            #move current state to closed list
            closed_list.append(current_state)
            #check if it is target
            if current_state[1][0] == target_state[0] or current_state[1][0] == target_state[1]:
                solution_found = True
                print("solution found")
                break
            #get all possible moves from this state
            neighbor_states = getNeighborStates(current_state[1])

            for state in neighbor_states:
                found = False
                isDupeRemoved = False
                for closed_state in closed_list:
                    if closed_state[1][0] == state[0]:
                        found = True
                        if state[0] in dupe_check:
                            dupe_check.remove(state[0])
                            isDupeRemoved = True
                        break
                    #check if it was a visited state
                if state[0] in dupe_check and not isDupeRemoved:
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
                        priority = state[2] + current_state[0]
                        open_list.put((priority, state))

                    for item in tempList:
                        open_list.put((item[0], item[1]))

                if not found:
                    priority = state[2] + current_state[0]
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
            f = open(str(puzzle_num) + "_ucs-h" + "_solution.txt", "w")
            for solution_state in reversed(solution_path):
                st = ""
                for i in solution_state[1][0]:
                    st += str(i) + " "
                f.write(str(solution_state[1][3]) + " " + str(solution_state[1][2]) + " " + st)
                f.write("\n")
            f.write("Total cost: " + str(total_cost) + " Execution time: " + str(time.time() - start_time))
            f.close()
            # write search path to file
            f = open(str(puzzle_num) + "_ucs-h" + "_search.txt", "w")
            for state in closed_list:
                fn = str(0) + " "
                gn = str(state[0]) + " "
                hn = str(0) + " "
                st = ""
                for i in state[1][0]:
                    st += str(i) + " "
                f.write(fn + gn + hn + st)
                f.write("\n")
            f.close()
        else:
            f = open(str(puzzle_num) + "_ucs-h" + "_solution.txt", "w")
            f.write("No solution")
            f.close()
            f = open(str(puzzle_num) + "_ucs-h" + "_search.txt", "w")
            f.write("No solution")
            f.close()
ucs()