### This program is an implementation of a vandalizing vending machine ###
### also known as vandalizing vendor (V^2). In essence, V^2 is a ###
### virtualized experience of reality--self explanatory. ###



# This function returns the dictionary of the available stock in V^2.
# The format of the dictionary is {item_number : (element, price)}
def getDefaultStockInMachineDict():
    """
    getDefaultStockInMachineDict() --> dictionary of stock in V^2
    in the form of {item_number: (element, price, quantity)}
    
    """

    stock_in_machine_dict = {   "01": ['Oxygen', 650, 3],
                                "02": ['Magnesium', 1, 3],
                                "03": ['Nitrogen', 32, 3],
                                "04": ['Phosphorus', 10, 3],
                                "05": ['Chlorine', 2, 3],
                                "06": ['Hydrogen', 95, 3],
                                "07": ['Calcium', 15, 3],
                                "08": ['Carbon', 185, 3],
                                "09": ['Potassium', 4, 3],
                                "10": ['Sodium', 2, 3],
                                "11": ['Sulfur', 3, 3],
                            }

    return stock_in_machine_dict




# This function returns a dictionary of the coins stored in V^2
# The format of the dictionary is {type_of_coin : quantity_stored_in_machine}
def getDefaultCoinsInMachineDict():
    """ getDefaultCoinsInMachineDict() --> dictionary of coins stored in V^2 """

    coins_in_machine_dict = {   "1p"    :   5,
                                "2p"    :   5,
                                "5p"    :   5,
                                "10p"   :   5,
                                "50p"   :   5,
                                "100p"  :   5,
                            }

    return coins_in_machine_dict



# This procedure prints out the menu of items that V^2 has in offer.
# The printed out text is in a neat table
def printStock():
    """ prints out the menu of V^2 (i.e. products in machine)"""

    max_items_per_line = 3
    stock_dict = getDefaultStockInMachineDict() 
                    
    for x in range(max_items_per_line):     # prints header per column
        print("{3} {0:<3} {1:<12} {2:<5} {3}"
              .format("NO.", "PRODUCT", "PRICE", '|'), end = '')

    print()

    for product_num, (product, price, _) in sorted(stock_dict.items()):
        
        print("{3} {0:<3} {1:<12} {2:<5} {3}"
              .format(str(product_num) + ".", product, price, '|'), end = '')

        if(int(product_num)%max_items_per_line == 0):    # Restricts printing on the 
            print()                                      # same line to
                                                         # max_items_per_line
    print("\n")                                          # times





        ### VARIOUS POTENTIAL ISSUES WITH THIS FUNCTION ###
# This function models inserting coins into V^2 and then returns
# the updated current coins in V^2 as a dictionary
def insertCoins(coins_in_machine_dict):
    """ insertCoins(coins_dict) --> total_coins_inserted, coins_dict """

    total_coins_inserted = 0

    print("Welcome to the endless insert a coin cycle.\n"
          "To illustrate how to input a coin, let us look at an example:\n"
          "To insert 100 pence please type 100p.\n"
          "This concludes the tutorial--Goodbye.\n\n"
          "NOTE: to end this brainless process, type: 'THE END'\n")
     
    while True:  
        inserted_coin = input("Insert: ")
        if(inserted_coin.upper() == "THE END"): ###1: NO ATTRIBUTEERROR()?
            break                               ### ABUSES THE FACT THAT INPUT       
                                                ### IS ALWAYS TYPE STR
        try:        
            coins_in_machine_dict = updateCoinsInMachine(inserted_coin,
                                                         coins_in_machine_dict)
        except (KeyError, TypeError, ValueError):
            continue
        ###2: NO TRY..EXCEPT() BECAUSE PREVIOUS ONE CATCHES THEM?
        total_coins_inserted += int(inserted_coin.strip('p'))
        total_funds_inserted = float(total_coins_inserted/100)        
        print("Total funds inserted: £{:.2f}\n".format(total_funds_inserted))


    return total_coins_inserted, coins_in_machine_dict





    ### SHOULD I SPECIFY EXCEPTIONS OR KEEP IT GENERAL IN THIS CASE? ###
            ### NOTE: OTHER POTENTIAL BAD PRACTICES BELOW ###
# This function updates the current coins dictionary in the machine when given
# a coin input; it is based heavily based on duck-typing
def updateCoinsInMachine(inserted_coin, coins_in_machine_dict):
    """ updateCoinsInMachine(coin, coin_in_machine_dict) ---> Boolean """

    try:
        inserted_coin = inserted_coin.lower()
        coins_in_machine_dict[inserted_coin] += 1

    except (KeyError, TypeError, ValueError):
        print("Error: a '{}' coin doesn't exist".format(inserted_coin))
        print("Please uphold moral values "
              "(i.e. your input was retarded).\n")
        raise ### NOTE RAISING TYPE OF ERROR WHEN GOING UP THE STACK
              ### E.G. WHEN USING PURCAHSE PRODUCT BELOW
        return coins_in_machine_dict ### DUPLICATE
    
    else:
        return coins_in_machine_dict ### DUPLICATE




                            ### BAD PRACTICE ### 
# This function allows the user to purchase a product from the stock available
# in V^2. It then updates the stock available and coins in machine as well as
# supply potential change back to the user. If various change sequences exist,
# it will allow the user to chose.
def purchaseProduct(total_coins_inserted,
                    stock_in_machine_dict, coins_in_machine_dict):
    """ purchaseProduct(stock_dict, coins_dict) --> item purchased"""

    funds = total_coins_inserted
    change_given = False
    
    printStock()
    print("Note: inputting 'THE END' will exit the purchase cycle\n")

    while True:

        item_num = input("What item would you like to buy? ")
        if(item_num == "THE END"):
            break

        try:
            ### GOOD ASSIGNMENT? ALSO, STOCK_IN_MACHINE THROWS SUPPRESSED
            ### EXCEPTIONS. E.G. INPUTTING ITEM_NUM = [1,2] WILL THROW AN
            ### EXCEPTION WITHOUT MUCH USEFUL INFORMATION FOR DEBUGGING/LOGGING
            product, price, quantity = stock_in_machine_dict[item_num]
            
              ### WHICH EXCEPTIONS SHOULD I SPECIFIY? ###
        except (KeyError, TypeError, ValueError) as e:
            print("A product number {} is a figment of your imagination.\n"
                  .format(e))
            continue


        if(price > funds):
            print("\nIn order to gain, one must sacrifice.\n"
                  "V\u00B2 follows the principle of equivalent exchange;\n"
                  "You require more funds for a valid exchange.\n"
                  "(You need {}p more coins.)\n".format(price - funds))

        if(quantity == 0):
            print("'{}' IS OUT OF STOCK.\n".format(product))
            continue
##            return    ### IF NO WHILE LOOP? SEEMS NOOB PRACTICE


        if(quantity != 0 and funds >= price):
            funds -= price
            stock_in_machine_dict[item_num] = (product, price, quantity - 1)
            print("You have purchased '{}'".format(product))

        print("Remaining funds: {}\n".format(funds))
 

    min_coins_dispensed_dict = marioAlgorithm(funds, coins_in_machine_dict)


    if(min_coins_dispensed_dict == None):
        print("Oh, what a suprise. No change can be given back. "
              "How unfortunate.")
    else:
        sorted_min_coins = sorted(min_coins_dispensed_dict.items(),
                                 key = lambda coin: int(coin[0].strip('p')),
                                 reverse = True)
        
        print()
        for (coin_type, quantity) in sorted_min_coins:
            coins_in_machine_dict[coin_type] -= quantity

            if(quantity != 0):
                print("Your change includes: {}x '{}' coins"
                      .format(quantity, coin_type))

        
        
        return coins_in_machine_dict, stock_in_machine_dict




    
    
                ### HOW TO MAKE THIS ALGORITHM CLEARER TO READ? ###
# This function calculates the minimum number of coins to dispense back to the
# user as change. The function uses a greedy algorithm hence an optimal solution
# is not guaranteed always. If no solution is found, NoneType is returned.
def marioAlgorithm(total_coins_inserted, coins_in_machine_dict):
    """ marioAlgorithm(total_coins, coins_dict) --> minimum coins for change """


    min_coins_dispensed = []
    partial_sum = 0
    full_sum = 0

    
    # Sorts the coins based on money value in descending order 
    sorted_coins_in_machine = sorted(coins_in_machine_dict.items(),
                                     key = lambda coin: int(coin[0].strip('p')),
                                     reverse = True)

    for coin_type, quantity in sorted_coins_in_machine:

        coin_type = int(coin_type.strip('p'))
        coins_fit = 0
        
        while True:
            coins_fit += 1
            partial_sum = coin_type*coins_fit

            if(partial_sum + full_sum > total_coins_inserted or
               coins_fit > quantity):
                
                coins_fit -= 1
                max_partial_sum = coin_type*coins_fit
                full_sum += max_partial_sum
                
                min_coins_dispensed.append((str(coin_type) + 'p', coins_fit))
                break
            

        if(full_sum == total_coins_inserted):
                return dict(min_coins_dispensed)

    if(full_sum < total_coins_inserted):
        print("\nNOT ENOUGH RAGE--NEED MORE RAGE.\n"
              "To be precise, V\u00B2 needs {}p more worth of coins internally."
              "\nTherefore, your transaction with V\u00B2 has been "
              "discontinued.\n".format(total_coins_inserted - full_sum))


        





# Initializes the coins and stock in V^2
coins_in_machine_dict = getDefaultCoinsInMachineDict()
stock_in_machine_dict = getDefaultStockInMachineDict()

coins_inserted = 0
running = True



print("{:^80}".format("Welcome to Vandalizing Vendor, "
                      "also known as V\u00B2, version VII!\n"))
while running:

    choice = input("\nLife consists of a finite quantity of decisions...\n\n"
                   "A. View available stock\n"
                   "B. Insert coins into V\u00B2\n"
                   "C. Purchase a product\n\n"
                   "Choice: ")
    if(choice == "THE END"):
        break


    if(choice.upper() == 'A'):
        print("\n")
        printStock()

    if(choice.upper() == 'B'):
        print("\n")
        coins_inserted, coins_in_machine_dict = insertCoins(
            coins_in_machine_dict) 

    if(choice.upper() == 'C'):
       coins_in_machine_dict, stock_in_machine_dict = purchaseProduct(
           coins_inserted, stock_in_machine_dict, coins_in_machine_dict)


















































