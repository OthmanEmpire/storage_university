class VendingMachine():

    def __init__(self, products=[], coins=[]):
        self.products   = products
        self.coins      = coins
        self.isStopped  = True

    def computeMinimumChange(self, product, cashTendered):
        """Uses algorithm ScamCustomer to calculate minimum change"""
        pass

    def addProduct(self, product):
        pass

    def removeProduct(self, product):
        pass

    def purchaseProduct(self):
        #self.printProducts()

        selectedProductName = \
            input("\n\n Enter the name of the product you would like to buy: ")

        selectedProductQuantity = \
            input("\n\n Enter the quantity of the product you would like to buy: ")

        self.updateProduct( selectedProductName, selectedProductQuantity )


    def updateProduct(self, updatedProductName, updatedProductQuantity):
        for product in self.products:
            if( updatedProductName == product.name ):
                print(product.quantity)
                product.quantity -= int(updatedProductQuantity)
                print(product.quantity)
                print("Product updated successfully.\n")
                product.printName()
                product.printQuantity()


    def addCoin(self, denomination, quantity):
        if( insertedCoin.isValidDenomination() ):
            #Add 
            coins[insertedCoin] += quantity
            #Calculate the total value of the coins inserted
            totalAmount = insertedCoin.value * quantity            
            print("Total coins inserted: £{:.2f}\n".format(totalAmount)) 
        else:
            raise RunTimeError("Invalid coin denomination")
        

    def removeCoin(self):
        pass
    
    def printProducts(self):
        #Menu layout format
        layout = "{line} {uuid:<3} {name:<12} {price:<5} {line}"
        layoutWidth = 3

        #Print the header
        for column in range(layoutWidth):
            print(layout.format(uuid="NO.", name="PRODUCT",
                                    price="PRICE", line='|'), end='')
        #Print new line
        print()

        #Keeps track of what column we're printing in
        columnCounter = 1

        #Print product's uuid, name and price
        for product in self.products:
            productUUID     = product.uuid
            productName     = product.name
            productPrice    = product.price

            print(layout.format(uuid=productUUID, name=productName,
                                    price=productPrice, line='|'), end='')

            #Start a new line if printing after 3rd column
            if( columnCounter >= layoutWidth ):
                columnCounter = 1
                print()
            else:
                columnCounter += 1  
            
    
    def printCoins(self):
        print(self.coins)
    
    def isStopped(self):
        return self.isStopped

    def start(self):
        self.isStopped = False


class Product():

    def __init__(self, uuid=0, name="default", price=0, quantity=0):
        self.uuid       = uuid
        self.name       = name
        self.price      = price
        self.quantity   = quantity

    def printName(self):
        MenuFormatter.printHeader()
        print("Name: \n {}".format(self.name))

    def printPrice(self):
        print("Price: \n £{:.2f}".format(self.price))

    def printQuantity(self):
        print("Quantity: \n {} Units".format(self.quantity))
    
    

class Coin():
    coinDenominations = [1,2,5,10,50,100]

    def __init__(self, value=0):
        self.value = value

    def isValidDenomination(self, value):
        """Checks if the coin is a valid nomination"""

        if value not in coinDenominations:
            return False
        else:
            return True

    def printValue(self):
        #Divide the coin value by 100 to get clearer format
        print("£{:.2f}".format(self.value/100))

class MenuFormatter():
    layout = "{line} {uuid:<3} {name:<12} {price:<5} {line}"

    def printHeader():
        print(layout.format(uuid="NO.", name="PRODUCT",
                                price="PRICE", line='|'), end='')
    
    



if __name__ == "__main__":
    #dictionary of product's uuid,name,price,quantity
    products = {    "01": ['Oxygen', 650, 3],
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

    #dictionary of current coins
    coins = {  "1p"    :   5,
                "2p"    :   5,
                "5p"    :   5,
                "10p"   :   5,
                "50p"   :   5,
                "100p"  :   5,
            }
    
    #Extract list of products from OzDictionary
    listOfProducts = []

    for uuid in sorted(products):
        productName     = products[uuid][0]
        productPrice    = products[uuid][1]
        productQuantity = products[uuid][2]

        listOfProducts.append( Product(uuid,productName,
                                           productPrice,productQuantity) )


    #Initialize vendor
    vandalizingVendor = VendingMachine(listOfProducts,[])
    vandalizingVendor.printProducts()

    vandalizingVendor.start()
    vandalizingVendor.purchaseProduct()

        

        

    

    
            
    
