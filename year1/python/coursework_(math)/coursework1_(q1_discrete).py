# Attempts to verify the solutions of discrete mathematics CW1

import random

def listUpTo(num):
    """
    Returns a lists of integers from 1 up to num
    """
    return list(range(1, num + 1))

def countMultiples(dividendList, divisor):
    """
    Returns the total number of multiples of the divisor in dividendList
    """
    multNum = 0

    for dividend in dividendList:
        if dividend % divisor == 0:
            multNum += 1

    return multNum

def solveQ1(myList, divisor, selectAmount, n):
    """
    Let X denote the number of successful trails in a given n trails.

    Selects a 'selectAmount' random elements from 'myList', checks whether it
    is a multiple of 'divisor', performs this for 'n' trails, then returns a
    probability point of X from it's binomial distribution.
    """

    X = 0

    for _ in range(n):
        random.shuffle(myList)

        for i, selected in enumerate(myList, start=1):

            if i == selectAmount:
                break
            else:
                if selected % divisor == 0:
                    X += 1


    p = X / (len(myList) * n * selectAmount)
    print(p)


if __name__ == "__main__":

    list40 = listUpTo(40)
    # print(list40)
    # print(countMultiples(list40, 4))
    # print()

    solveQ1(list40, 4, 2, 10000)

