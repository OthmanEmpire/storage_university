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


def parcel_category(parcel):        # First checks weight, then checks dimensions where the dimensions are independent of order

    n = 0
    optimal = None
    
    label = labels()

    for i in range(1,5):    # Start at 1 to ignore row r0 which is just a header

        category = data_table(label[i])      

        weightfit = float(parcel[0]) <= float(category[1])

        if(weightfit):
            optimal = category[0]
            position = i
            break
        elif(i == 4):

##            print(category)
            return 'Large_parcel'


    while(position < 5):

        category = data_table(label[position])
        test = dimension_algorithm(parcel, category)

        if(test == False):
            
            # 11.5 400 100 600
            position += 1
            
        else:

##            print(category[1:])
            return list(category)[0]

##    print(category)
    return 'Large_parcel'
    

# Dimension Algorithm classifies a parcel regardless of how the user
# inputs length, height and width of the parcel
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




#########################################################

import time

while True:

    start = time.perf_counter()


    for a in range(1,30):
        for b in range(1,611):
            for c in range(1,611):

                end  = time.perf_counter()
                progress = end - start

                time_left = (1 - c/611) * progress

                
                
                for d in range(1,611):
                    parcel = [a,b,c,d]

##                    print(parcel)


                    pcat = parcel_category(parcel)

                    


                    print(a,b,c,d, "Time left: {:.3f}".format(time_left))
                    
##                    print("The smallest available parcel type is: {}\n\n".format(pcat))

                    

   

    gen_cost_table()
    price = cost(pcat, parcel)





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
