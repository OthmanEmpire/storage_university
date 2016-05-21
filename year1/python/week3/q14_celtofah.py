### This function converts Celsius to Fahrenheit ###

def fahtoCel(temp):

    cel = (5/9)*(temp - 32)

    return cel


temp = float(input("Welcome to fahtoCel! Please input your temperature in Fahrenheit: "))

cel = fahtoCel(temp)
print("{:.1f}".format(cel))
