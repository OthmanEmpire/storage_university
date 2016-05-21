### This program prints out the Celsius to Fahrenheit conversion table ###

def fahren(n):
    fah = (9/5)*n + 32
    return fah



print("Celsius   Fahrenheit")

for cel in range(0,101):
    fah = fahren(cel)
    fah = format(fah, '6.1f')
    print('{:^7} | {:^8}'.format(cel, fah))



          
##    x = format( 3.14 , '2.2' 'f')     This actually works

##    print("%4d  |  %.1f" % (cel, fahren(cel)))    Old formatting method
