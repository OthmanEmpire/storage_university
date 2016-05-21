### This program reads lists from two different files and then prints ###
### the intersection of both lists ###


def readListFromFile(data_file):

    school_class = []
    
    while True:
        try:
            with open(data_file, "r") as file:

                for line in file:
                    school_class.append(line.rstrip())

                return school_class

        except IOError() as err:
            print("{}\n".format(err))
            data_file = input("Please input your file name again: ")



def commonElements(listA, listB):

    listC = []
    
    for a in range(len(listA)):

        end_of_list = False
        b = 0

        while not end_of_list:
            
            if(listA[a] == listB[b]):
                
                listC.append(listB[b])
                del listB[b]
                
            b += 1

            if(b == len(listB)):
                end_of_list = True

            

    return listC
            
            


print("Welcome to Sodium Hydrogen Carbonate, ", end = "")
print("i.e. Sodium Bicarbonate, version 1.0!\n")

classA = readListFromFile("ClassA.txt")
classB = readListFromFile("ClassB.txt")
print(classA)
print()
print(classB)

common_students = commonElements(classA, classB)
print("\n")
print(common_students)
