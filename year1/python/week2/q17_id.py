### This program prints a 5 element list nested in a 5 element list ###


array = []

for i in range(5):
    array.append([])
    
    for j in range(5):
        element = 5*j + i           # As specified in workbook   
        array[i].append(element)


for i in range(5):          # Prints out one nested list at a time
    print(array[i])
