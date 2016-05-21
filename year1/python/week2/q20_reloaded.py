### Lucky Number Guesser ###

print(" *** Lucky Number Guesser *** ")

nstring = input("Enter an integer: ")
n = int(nstring)

if(n == 42):
      print("You guessed my lucky number.")
      print("Give yourself a pat on the back.")

if not(n == 42):
      print("Unlucky :( --- Better luck next time.")
