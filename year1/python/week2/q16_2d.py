### This program prints the values of a two dimensional list ###


array = []


print("Please input your values for a two dimensional list: ")
print("e.g. to input 4 and 8 type: 4 8\n")
    
for x in range(3):
    a, b = input("                            ").split()
    array.append([a,b])

    
    

for i in range(len(array)):
    print(array[i])

