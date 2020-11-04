import numpy as np

puzzle_file = open("Resources/testpuzzle.txt")
with open('Resources/testpuzzle.txt', 'r') as f:
    data = f.read()

puzzles = [int(i) for i in data.split(" ")]

target_state = [[1,2,3,4,5,6,7,0], [1,3,5,7,2,4,6,0]]

def getMinPriority(list):
    minIndex = -1
    minNumber = 10
    for state in list:
        if state[2] < minNumber:
            minNumber = state[2]
        minIndex += 1
    return minIndex


def getNeighborStates(list):
    initial_list = list[0].copy()
    new_state = list[0].copy()
    neighbor_states = []

    zero_index = 0
    for num in initial_list:
        if num == 0:
            break
        zero_index += 1

    if zero_index != 0 and zero_index != 3 and zero_index != 4 and zero_index != 7:
        new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
        neighbor_states.append([new_state, initial_list, 1])
        new_state = initial_list.copy()

        new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
        neighbor_states.append([new_state, initial_list, 1])
        new_state = initial_list.copy()

        if zero_index > 3:
            new_state[zero_index], new_state[zero_index - 4] = new_state[zero_index - 4], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()
        else:
            new_state[zero_index], new_state[zero_index + 4] = new_state[zero_index + 4], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()
    else:
        if zero_index == 0:
            new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index + 4] = new_state[zero_index + 4], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index + 5] = new_state[zero_index + 5], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index + 7] = new_state[zero_index + 7], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()
        elif zero_index == 3:
            new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index + 4] = new_state[zero_index + 4], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()
        elif zero_index == 4:
            new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index - 4] = new_state[zero_index - 4], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()
        else:
            new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index - 4] = new_state[zero_index - 4], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index - 5] = new_state[zero_index - 5], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()

            new_state[zero_index], new_state[zero_index - 7] = new_state[zero_index - 7], new_state[zero_index]
            neighbor_states.append([new_state, initial_list, 1])
            new_state = initial_list.copy()
    return neighbor_states

def gbfs():
    current_state = puzzles
    previous_state = []
    num_moves = 0

    open_list = [[current_state, previous_state, 1]]
    closed_list = []
    while len(open_list) > 0:
        current_state = open_list.pop(getMinPriority(open_list))
        closed_list.append(current_state)
        if current_state[0] == target_state[0] or current_state[0] == target_state[1]:
            print("solution found")
            break
        neighbor_states = getNeighborStates(current_state)
        for state in neighbor_states:
            found1 = False
            found2 = False
            for closed_state in closed_list:
                if closed_state[0] == state[0]:
                    found1 = True
                    break
            for open_state in open_list:
                if open_state[0] == state[0]:
                    found2 = True
                    break

            if not found1 and not found2:                
                open_list.append(state)
    for state in closed_list:
        print(state)
gbfs()