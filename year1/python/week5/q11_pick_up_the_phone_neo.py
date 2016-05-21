#### This program simulates a Terminal Phonebook Directory ###






    ### MERGE CODE INTO ONE SECTION BUT NEED INDEPENDENT EXCEPTION CATCHING ###
# This function adds a new number to the phonebook directory then returns the
# phonebook directory
def addContact(phonebook_dict): 
    """ Adds a new number to the phonebook dict then returns dict """

    try:
        contact = input("Please input the name of your contact: ")
        
        if(not contact.isalpha()): 
            raise ValueError

    except ValueError:
        for _ in range(3):
            print(end = ".")
            freeze(1)
        print()
        for _ in range(3):
            print("{} is UNACCEPTABLE!".format(contact))
            freeze(1)
        return      ### BAD PRACTICE? ###
        

    try:
        tele_num = input("Please input a telephone number: ")

        numberLength = len(tele_num)

        if( not (6 < numberLength < 14)  ):
            pass

        if( not numberLength.isdigit() ):
            pass

        if( numberLength in range(6,14) ):




        if(len(tele_num) > 14 or len(tele_num) < 6 or not tele_num.isdigit()): 
            raise ValueError

    except ValueError:        
        for _ in range(3):
            print(end = ".")
            freeze(1)
        print()
        for _ in range(3):
            print("{} is UNACCEPTABLE!".format(tele_num))
            freeze(1)
        return      ### BAD PRACTICE? ###
        
    phonebook_dict[contact] = tele_num 

    return phonebook_dict




# 
def viewAllContacts(phonebook_dict):
    pass





def searchContact():
    pass

def deleteContact():
    pass


# Freeze.
def freeze(x):
    """ Bends the fabrics of time itself """
                      
    try:
        import time
        time.sleep(x)
                    
    except ImportError:
        print("Time in this region could not be frozen.")


        
phonebook_dict = {}

addContact(phonebook_dict)

    
    
