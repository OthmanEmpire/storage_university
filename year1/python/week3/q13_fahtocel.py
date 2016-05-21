### This function converts Celsius to Fahrenheit ###

def celtoFah(temp):

    fahren = (9/5)*temp + 32

    return fahren


temp = int(input("Welcome to celtoFah! Please input your temperature in Celsius: "))

fah = celtoFah(temp)
print(fah)
