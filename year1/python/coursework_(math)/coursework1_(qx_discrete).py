# Attempts to verify the solutions of discrete mathematics CW1

import random

possibleRolls = [1, 2, 3, 4, 5, 6]
occuredRolls = set()
count = 0
allCount = 0

for i in range(100):
    while len(occuredRolls) < 6:

        count += 1
        random.shuffle(possibleRolls)

        roll = possibleRolls[1]

        occuredRolls.add(roll)

    print(count)
    allCount += count
    count = 0

print(allCount/100)