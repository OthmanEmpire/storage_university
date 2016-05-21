### This program inputs the dimensions and weight of a parcel then outputs ###
### the smallest parcel type available from a data table ###

import time

def data_table(rowname):
    r0 = 'Type Max_weight/kg Max_length/mm Max_width/mm Max_height/mm'
    r1 = 'Letter 0.1 240 165 5'
    r2 = 'Large_letter 0.75 353 250 25'
    r3 = 'Small_parcel 2 450 350 80'
    r4 = 'Small_parcel 2 350 250 160'
    r5 = 'Medium_parcel 20 610 460 460'

    row = tuple(eval(rowname).split())          # Tuple prevents change of data
    
    return row

def data_cost(rowname):
    r0 = 'Type Flat_price/£ Basic_weight/kg Price_per_0.1kg/£'
    r1 = 'Letter 1.72 0.1 0'
    r2 = 'Large_letter 2.03 0.1 0.10'
    r3 = 'Small_parcel 4.30 1 0.40'
    r4 = 'Medium_parcel 6.75 10 0.90'
    r5 = 'Large_parcel 15 10 1.56'

    row = tuple(eval(rowname).split())

    return row
        
def labels():
    labels = []
    for n in range(6):
        labels.insert(n, 'r' + str(n))         # Generates the labels of the rows in function data as strings
    return labels



def gen_data_table():
    print("For reference purposes, here is the CityParcel's data table:\n")

    label = labels()
    
    for i in range(6):
        print()
        row = data_table(label[i])

        for c in range(5):
            print("{:<15}".format(row[c]), end = "")



def gen_cost_table():
    print("For further reference purposes, here is the CityParcel's cost table:\n")

    label = labels()
    
    for i in range(6):
        print()
        row = data_cost(label[i])

        for c in range(4):
            print("{:<20}".format(row[c]), end = "")




def parcel_category(parcel):        # First checks weight, then checks dimensions where the dimensions are independent of order

    n = 0
    optimal = None
    
    label = labels()

    for i in range(1, 6):    # Starts at 1 to ignore row r0 which is just a header

        category = data_table(label[i]) 

        weightfit = float(parcel[0]) <= float(category[1])

        if(weightfit):
            optimal = category[0]
            position = i
            break
        elif(i == 5):
            return 'Large_parcel'


    while(position < 6):

        test = dimension_algorithm(parcel, category)

        if(test == False):
            position += 1
            # 11.5 400 100 600
            category = data_table(label[position])
        else:
            return list(category)[0]


    return 'Large_parcel'
    

# Algorithm sorts out two lists in ascending order and then maps an element
# of one list to an element of the other list that is on it's RIGHT
# hence being able to fit a set of numbers optimally within another set of numbers
def dimension_algorithm(parcel, category):

    dimension_fits = 0
    
    dimension_parcel = [int(x) for x in parcel[1:4]]
    dimension_category = [int(y) for y in category[2:5]]

    dimension_parcel.sort()
    dimension_category.sort()

    for dimension in range(3):

        if(dimension_parcel[dimension] <= dimension_category[dimension]):
            dimension_fits += 1

            if(dimension_fits == 3):
                return True

    return False


def dimension_algorithm(parcel, category):

    dimension_fits = 0
    
    dimension_parcel = [int(x) for x in parcel[1:4]]
    dimension_category = [int(y) for y in category[2:5]]

    dimension_parcel.sort()
    dimension_category.sort()

    for dimension in range(3):

        if(dimension_parcel[dimension] <= dimension_category[dimension]):
            dimension_fits += 1

            if(dimension_fits == 3):
                return True

    return False



def cost(pcat, parcel):

    cost = 0

    weight = parcel[0]
    
    label = labels()

    for i in range(5):
    
        data = data_cost(label[i + 1])       # Ignores r0 which is just a header
        
        if(pcat == data[0]):

            if(float(weight) < float(data[2])):
                cost = float(data[1])
                return cost
            else:
                overweight = float(weight) - float(data[2])
            
                cost = float(data[1]) + overweight*10*float(data[3])       # 10* is since price is per 0.1kg and not per kg

    if(cost == 0):
        print("\nError detected! cost = 0 which is unplausible since nothing apparently is for free.")

    return cost



def user_parcel():
    print("\n\nPlease input your parcel's weight and dimensions without units:")
    print("e.g. 1, 100, 200, 300")

    valid = 0
    
    while(valid == 0):
    
        parcel = input().split(',')

        if(len(parcel) != 4):
            print("Please input non-noob number of dimensions: ")
            continue
        
        for i in range(4):
            if(parcel[i] == '0'):
                print("I sense an imminent blackhole", end = "")
                for n in range(3):
                    print(".", end = "")
                    time.sleep(1)
                exit()

        valid = 1
        
    return parcel



#########################################################



print("Welcome to CityParcel, where there exists at least two people in London ", end = "")
print("that have the same number of hairs on their heads due to the Pigeonhole principle!\n")

grace = 0
totalcost = 0
valid = 0

while(grace == 0):
    gen_data_table()
    parcel = user_parcel()

    pcat = parcel_category(parcel)
    print("The smallest available parcel type is: {}\n\n".format(pcat))

    gen_cost_table()
    price = cost(pcat, parcel)
    totalcost += price
    print("\n\nThe cost of sending your junk is: £{:.2f}".format(price))
    print("So far, the total cost of ALL your junk is £{:.2f}".format(totalcost))

    while(valid == 0):
        choice = input("Would you like to classify more junk (Y/N)?: ")
        
        if(choice == 'Y'):
            valid = 1
        elif(choice == 'N'):
            exit()
        else:
            print("Nice try.")

    print()
    valid = 0   # Resets condition for while loop










### ALTERNATIVE INEFFICIENT ALGORITHM ###
### Algorithm sorts out two lists in ascending order and then maps an element
### of one list to an element of the other list that is on it's RIGHT
### hence being able to fit a set of numbers optimally within another set of numbers
##def dimension_algorithm(parcel, category):
##
##    matrix_A = [ [], [] ]
##    matrix_B = [ [], [] ]
##    matrix_C = [ [], [] ]
##
##    dimension_parcel = [int(x) for x in parcel[1:4]]
##    dimension_category = [int(y) for y in category[2:5]]
##
##    
##    a = dimension_parcel[0]
##    b = dimension_parcel[1]
##    c = dimension_parcel[2]
##
##
##    for dimension in range(3):      # Setting up the initial expressions
##
##        matrix_A[0].append(dimension_category[dimension] - a)
##        matrix_B[0].append(dimension_category[dimension] - b)
##        matrix_C[0].append(dimension_category[dimension] - c)
##
##    
##    for expression_index in range(3):
##
##        if(matrix_A[0][expression_index] >= 0):
##            matrix_A[1].append(True)
##        else:
##            matrix_A[1].append(False)
##
##        if(matrix_B[0][expression_index] >= 0):
##            matrix_B[1].append(True)
##        else:
##            matrix_B[1].append(False)
##
##        if(matrix_C[0][expression_index] >= 0):
##            matrix_C[1].append(True)
##        else:
##            matrix_C[1].append(False)
##
##    
####    print(matrix_A)
####    print(matrix_B)
####    print(matrix_C)
##
##
##    for a in range(3):
##        for b in range(3):
##            for c in range(3):
##                
##
##                if(matrix_A[1][a] == True):
##                    solution_A = True
##                else:
##                    solution_A = False
##
##                if(matrix_B[1][b] == True):
##
##                    solution_B = True
##                else:
##                    solution_B = False
##
##                if(matrix_C[1][c] == True):
##
##                    solution_C = True
##                else:
##                    solution_C = False
##
##                if(solution_A and solution_B and solution_C):
##                    return True
##
##                
##
##    return False







