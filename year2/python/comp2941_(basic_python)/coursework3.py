###########################################
### Name: Othman Alikhan                ###
### Module: COMP2941: Algorithms II     ###
### Coursework Number: 3                ###
###########################################

import math

############################# SOLUTIONS: Q2 & Q3 ###############################
def calculateSquareRoot(n):
    """
    Given an input n, returns the closest integer above square root of n.
    """

    root = 1    # Only considering positive roots
    while(root*root <= n):
            root += 1

    return root

############################# SOLUTIONS: Q4  ###################################
def generateEvilMatrix(n):
    """
    Generates a sinister matrix for show by appending data into a list of lists.
    """

    matrixA = []

    for i in range(1, n+1):     # row indexing start from 1
        matrixA.append([])
        for j in range(1, n+1):     # column indexing start from 1
            matrixA[i-1].append((1 / ((i + 1) + (j + 1))))

    return matrixA

def printEvilMatrix(matrixA):
    """
    Prints a sinister matrix for show in a relatively neat format (evil must
    also be presented neatly).
    """
    for row in matrixA:
        for element in row:
           print("{:.3f} ".format(element), end="")
        print()     # prints a space between each row

############################# SOLUTIONS: Q5 (part a)  ##########################
def estimatePiSquared(n):
    """
    Estimates that value of Pi^2 through a formula involving partial sums.
    n is the number of terms to be summed; the larger the more accurate the
    estimation of Pi^2 tends to be (but not always).
    """

    partialSum = 0    # Initializing

    # Implementation of the mathematical formula involving summing
    for k in range(1, n+1):
        partialSum += 1 / (k ** 2)
    estimate = 6*partialSum

    return estimate

def printEstimatePiSquared():
    """
    Prints the amount of summands, estimated value of Pi^2 (using
    estimatePiSquared), actual value of Pi^2, and the absolute error in
    the approximation in a neat 'table'.
    This is done for specific amount of summands: 10**6, ..., 10**9
    """

    summands = [10**6, 10**7, 10**8, 10**9]

    for quantity in summands:

        estimate = estimatePiSquared(quantity)
        actual = math.pi**2
        error = actual - estimate
        print("Terms: {:.1e} || Estimate: {} || Actual: {} || Abs Error: {}"
              .format(quantity, estimate, actual, error))

############################# SOLUTIONS: Q5 (part b)  ##########################
def estimateModifiedPiSquared(n):
    """
    Estimates that value of Pi^2 through a formula involving partial sums.
    n is the number of terms to be summed; the larger the more accurate the
    estimation of Pi^2 tends to be (but not always).
    The modification relative to estimatePiSquared() is that the n terms are
    added in reverse order (i.e. the smallest values are added first).
    """

    partialSum = 0    # Initializing

    # Implementation of the mathematical formula involving summing
    for k in range(n, 0, -1):     # Order reversed
        partialSum += 1 / (k ** 2)
    estimate = 6*partialSum

    return estimate

def printEstimateModifiedPiSquared():
    """
    Prints the amount of summands, estimated value of Pi^2 (using
    estimateModifiedPiSquared), actual value of Pi^2, and the absolute error in
    the approximation in a neat 'table'.
    This is done for specific amount of summands: 10**6, ..., 10**9
    """

    summands = [10**6, 10**7, 10**8, 10**9]

    for quantity in summands:

        estimate = estimateModifiedPiSquared(quantity)
        actual = math.pi**2
        error = actual - estimate
        print("Terms: {:.1e} || Estimate: {} || Actual: {} || Abs Error: {}"
              .format(quantity, estimate, actual, error))

############################# 'TESTING' SOLUTIONS  #############################
def runTestQ2AndQ3():
    """
    Exhibits the powers of Q2 & Q3.
    """
    print("Q2 + Q3: The closest integer above square root of '466352' is: {}\n"
          .format(calculateSquareRoot(466352)))

def runTestQ4():
    """
    Exhibits the powers of Q4.
    """
    matrixA = generateEvilMatrix(5)

    print("Q4: Now entering the matrix:")
    printEvilMatrix(matrixA)
    print()

def runTestQ5PartA():
    """
    Exhibits the powers of Q5 (part a).
    """
    print("Q5: Everyone likes some Pi...")
    printEstimatePiSquared()
    print()

def runTestQ5PartB():
    """
    Exhibits the powers of Q5 (part a).
    """
    print("Q5: Everyone likes some genetically modified Pi...")
    printEstimateModifiedPiSquared()
    print()

def runTests():
    """
    'Verifies' the solutions of the coursework
    """
    runTestQ2AndQ3()
    runTestQ4()
    runTestQ5PartA()
    runTestQ5PartB()


if __name__ == "__main__":
    runTests()