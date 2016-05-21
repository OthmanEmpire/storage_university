### Count until 100 and replace: 3k = Fizz ; 5k = Buzz ;  3m and 5n = FizzBuzz ###

for n in range(1,101):      # Ignores 0 since 0%3 and 0%5 result in FizzBuzz

    mod3 = n%3
    mod5 = n%5

    if(mod3 == 0 and mod5 == 0):
        print("FizzBuzz")
        continue

    elif(n%3 == 0):
        print("{:<4}".format("Fizz"), end = " ")
        continue
              
    elif(n%5 == 0):
        print("{:<4}".format("Buzz"), end = " ")

    else:
        print("{:<4}".format(n), end = " ")
