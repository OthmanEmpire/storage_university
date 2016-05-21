### This program prints out the first 5 Pythagorean triples ###

def triplet(m,n):    

    a = 0
    b = 0
    c = 0

    A = m%n         # Condition to test whether m and n are coprime
    if(n == 1):     # To catch special cases (e.g. 2%1 = 0 but 2 and 1 are indeed coprime 
        A = 1
        
    B = (m - n - 1)%2           # Condition to test whether m or n is odd
    C = (m > n)         # Condition to prevent negative 'a'

    if((A != 0) and (B == 0) and (C == 1)):        # Tests whether conditions hold true
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2

    if(a > 0 and b > 0):          # Prevents negative integers
        return [a,b,c]
    else:
        return 0


def order(array):           # Orders the list of lists based on the first element

    length = len(array)

    for n in range(length):
        if(array[n][0] > array[n][1]):
            array[n][0], array[n][1] = array[n][1], array[n][0]

    
    
tri = []

tablesize = input("Please input the size of the magical table (e.g. 42) ")
tablesize = int(tablesize)


for m in range(1, tablesize):
    for n in range(1, tablesize):

        if(triplet(m,n) != 0):
            tri.append(triplet(m,n))

order(tri)

length = len(tri)

print("The triplets are:\n")
for i in range(0, length - 2, 3):       # To prevent index out of reach error for below print function
    print("{:<20} {} {:^20} {} {:>20}".format(tri[i], '|', tri[i+1], '|', tri[i+2]))
