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
    
    for i in range(5):
        print()
        row = data_table(label[i])

        for c in range(5):
            print("{:<15}".format(row[c]), end = "")



def gen_cost_table():
    print("For further reference purposes, here is the CityParcel's cost table:\n")

    label = labels()
    
    for i in range(5):
        print()
        row = data_cost(label[i])

        for c in range(4):
            print("{:<20}".format(row[c]), end = "")




def parcel_category(parcel):
    
    label = labels()

    for i in range(5):

        category = data_table(label[i+1])       # Ignores row r0 which is just a header

        for n in range(4):
            # float below is NECESSARY or else DANGEROUS behaviour when comparing '100' > '2' which returns false since it compares one element at a time
            if(float(parcel[n]) > float(category[n+1])):        # n + 1 to ignore the literal string of parcel type 
                break
            
            elif(n == 3):           # Success if user's parcel's 4 dimensions are smaller than the given category
                return category[0]
    
    return 'Large_parcel'       # This holds true if no category match found in the for loop above
    


def cost(pcat, weight):
    
    label = labels()

    for i in range(5):
    
        data = data_cost(label[i + 1])       # Ignores r0 which is just a header
        
        if(pcat == data[0]):


            overweight = float(weight) - float(data[2])

            
            cost = float(data[1]) + overweight*10*float(data[3])       # 10* is since price is per 0.1kg and not per kg

    if(cost == 0):
        print("Error detected! cost = 0 which is unplausible since nothing apparently is for free.")

    return cost



def user_parcel():
    print("\n\nPlease input your parcel's weight and dimensions without units (just like the table above):")

    valid = 0
    
    while(valid == 0):
    
        parcel = input().split()

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
    print(pcat, parcel[0], type(pcat), type(parcel[0]))
    price = cost(pcat, parcel[0])
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
