### This program finds the combinatorics value of a given n & k ###


def combinatoric(n, k):

    if(k == 0 or k == n):
        return 1
    else:
        return combinatoric((n-1), (k-1)) + combinatoric((n-1),k)


n,k = input("Welcome to combine version 1.1! Please inject inputs: ").split()
n = int(n)
k = int(k)

print(combinatoric(n,k))

