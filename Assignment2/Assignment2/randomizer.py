import random

nums = [0, 1, 2, 3, 4, 5, 6, 7]
target_state = [[1,2,3,4,5,6,7,0], [1,3,5,7,2,4,6,0]]

f = open("Resources/50puzzles.txt", "w")
for i in range(50):
    random.shuffle(nums)
    while nums == target_state[0] or nums == target_state[1]:
        random.shuffle(nums)
    for num in nums:
        f.write(str(num) + " ")
    if i != 49:
        f.write("\n")
f.close()

