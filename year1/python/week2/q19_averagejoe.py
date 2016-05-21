### This program inputs numbers then prints out the sum and mean ###

s = 0
array = []

array = input("Please KINDLY input numbers (e.g. 3 1 4 1 5 9): ").split()


elements = len(array)

for n in range(elements):
    s = s + int(array[n])   # Sum
    m = s / elements     # Mean

print("Sum: {} | Avg: {}".format(s, m))
