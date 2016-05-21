# This program inputs seconds and then converts it to the form HH:MM:SS #

print("Welcome to Chronokeeper version 1.0, time is money friend!")
print("We will now request your data in order to pass it through a wormhole.")

print("Please input the number of seoconds you wish to compress into a blackhole: ", end = " ")
seconds = int( input() )

SS = seconds % 60
MM = (seconds // 60) % 60       # The modulus 60 prevents MM exceeding 60 minutes (which should be rightfully carried over to HH)
HH = seconds // 3600

print("We have successfully (al7umdulilah) sent your information through the wormhole")
print("The output was: ", HH, ":", MM, ":", SS, "(HH:MM:SS)")
