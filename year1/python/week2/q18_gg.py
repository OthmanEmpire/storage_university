### This program amalgamates the past; ask and you will be given a grid of numbers ###


array = []


print("Welcome to create to the 2D world.")

size = input("Please input your 2D dimensions (e.g. 3x4): ").split("x")

size[0], size[1] = int(size[0]), int(size[1])



for x in range(size[0]):
    array.append([])
    for y in range(size[1]):
        array[x].append(5*x + y)




for n in range(size[0]):
    print()
    for m in range(size[1]):
        print("{:<10d}".format(array[n][m]), end = " ")

