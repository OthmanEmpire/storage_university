"""
% heat.py
%
% Finds the distribution of temperature throughout a square for a given
% temperature distribution on the boundary.
"""

import numpy as np
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d,Axes3D
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data
from matplotlib import cm

def storeFirstRow(A, b, Temp, m, n):
    """
    Inserts all of the non-zero entries for the first row of matrix A and
    vector b.

    Temp contains the temperature initial distribution data.
    n is the number of unknown temperature points per direction
    """

    #Begin with the row of the grid immediately below the top boundary.
    i = 1
    j = 1
    k = 0 #k is used to store the row number of the matrix throughout.
    A[k,k] = 4.
    b[k] = b[k] + Temp[i-1,j]
    b[k] = b[k] + Temp[i,j-1]
    A[k,k+1] = -1.
    A[k,k+n] = -1.

    for j in xrange(2,m-2):
        k += 1
        A[k,k] = 4.
        b[k] = b[k] + Temp[i-1,j]
        A[k,k-1] = -1.
        A[k,k+1] = -1.
        A[k,k+n] = -1.

    k += 1
    A[k,k] = 4.
    b[k] = b[k] + Temp[i-1,j]
    A[k,k-1] = -1.
    b[k] = b[k] + Temp[i,j+1]
    A[k,k+n] = -1.

    return A, b, k

def storeMiddleRows(A, b, Temp, m, n, k):
    """
    Inserts all of the non-zero entries for all the rows except the first and
    last for matrix A and vector b.

    k is used to store the row number of the matrix throughout.
    Temp contains the initial temperature distribution data.
    n is the number of unknown temperature points per direction
    """

    #Now consider rows 2 to m-2
    for i in xrange(2,m-2):
        j = 1
        k += 1
        A[k,k] = 4.
        A[k,k-n] = -1.
        b[k] = b[k] + Temp[i,j-1]
        A[k,k+1] = -1.
        A[k,k+n] = -1.
        for j in xrange(2,m-2):
            k += 1
            A[k,k] = 4.
            A[k,k-n] = -1.
            A[k,k-1] = -1.
            A[k,k+1] = -1.
            A[k,k+n] = -1.

        k += 1
        A[k,k] = 4.
        A[k,k-n] = -1.
        A[k,k-1] = -1.
        b[k] = b[k] + Temp[i,j+1]
        A[k,k+n] = -1.

    return A, b, k

def storeLastRow(A, b, Temp, m, n, k):
    """
    Inserts all of the non-zero entries into the last row for matrix A and
    vector b.

    k is used to store the row number of the matrix throughout.
    Temp contains the initial temperature distribution data.
    n is the number of unknown temperature points per direction
    """
    #Finally consider the row of the grid immediately above the bottom
    #boundary
    i = m-2
    j = 1
    k += 1
    A[k,k] = 4.
    A[k,k-n] = -1.
    b[k] = b[k] + Temp[i,j-1]
    A[k,k+1] = -1.
    b[k] = b[k] + Temp[i+1,j]
    for j in xrange(2,m-2):
        k += 1
        A[k,k] = 4.
        A[k,k-n] = -1.
        A[k,k-1] = -1.
        A[k,k+1] = -1.
        b[k] = b[k] + Temp[i+1,j]

    k += 1
    A[k,k] = 4.
    A[k,k-n] = -1.
    A[k,k-1] = -1.
    b[k] = b[k] + Temp[i,j+1]
    b[k] = b[k] + Temp[i+1,j]

    return A, b, k

def generateSystemOfEquations(m):
    """
    For the given temperature distribution network problem, generates the
    matrix A and vector b such that Ax = b.
    """

    #Initialise an array for storing the temperature at each approximation
    #point in the m by m grid
    Temp = np.zeros([m,m])

    #Impose the desired temperature distribution on the boundary (any values
    #not set here are left as zero).
    Temp[0,:] = np.linspace(100,0,m)
    Temp[:,0] = np.linspace(100,0,m)

    #Let n be the number of points in each direction at which th temperature
    #is unknown and let n2 be the total number of unknown points (i.e. the
    #number of grid points not on the boundary).
    n = m-2
    n2 = n**2

    #Initialise to zero all entries of the n2 by n2 matrix and the right-hand
    A = np.zeros([n2,n2])
    b = np.zeros([n2,1])

    #Insert all of the non-zero entries into the matrix and right-hand side
    #vector
    A, b, k = storeFirstRow(A, b, Temp, m, n)
    A, b, k = storeMiddleRows(A, b, Temp, m, n, k)
    A, b, _ = storeLastRow(A, b, Temp, m, n, k)

    return A, b, Temp

def plotSystem(Temp, u, m):
    """
    Plots the 3D temperature distribution across the surface of interest.
    This done by first initializing the plot and then by executing it.
    """

    #INITALIZATION
    #The entries of u can now be mapped into their corresponding points in
    #the two-dimensional array Temp
    k = -1
    for i in xrange(1,m-1):
        for j in range(1,m-1):
            k += 1
            Temp[i,j] = u[k]

    #PLOTTING
    #Finally we can plot the results
    x = np.linspace(1,m,m)
    y = np.linspace(1,m,m)
    X,Y = np.meshgrid(x,y)

    fig = plt.figure()
    ax = Axes3D(fig)
    surf = ax.plot_surface(X,Y,Temp, rstride=1,cstride=1,
                           cmap=cm.gnuplot, linewidth=0,antialiased=False)
    #ax.plot_wireframe(X,Y,Temp)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('Temperature')
    ax.set_xlim3d([1,m])
    ax.set_ylim3d([1,m])
    ax.set_zlim3d([0.,100.])
    plt.title('Temperature distribution across a square')
    plt.show()

def solveSystemUsingLinalg():
    """
    Solves and plots the system of equations for the temperature distribution
    problem using a built-in numpy method, linalg.
    """

    #The list of the number of approximation points required in each direction
    #to be iterated through
    m_list = [17, 33, 65, 129]

    for m in m_list:
        A, b, Temp = generateSystemOfEquations(m)

        #Solving the system of linear equations and timing them
        t0 = time.clock()
        u = np.linalg.solve(A,b)
        time_taken = time.clock() - t0

        unknown_points = (m-2) * (m-2)
        centre_temp = u[len(u)//2][0]
        error = 25.0 - centre_temp


        print "m: {} || Unknown Points: {} || Centre Temp: {:.6f} || " \
              "Error: {:.3e} || Time Taken: {:.1e}"\
            .format(m, unknown_points, centre_temp, error, time_taken)

        plotSystem(Temp, u, m)

########################################################################
###ACKNOWLEDGEMENT: TAKEN FROM VLE (SPECIFICALLY FROM matrixSolve.py)###
########################################################################
def jacobi_new(A,u,b,tol):
    """
    Solve the system A u = b using a Jacobi iteration

    ARGUMENTS:  A   k x k matrix
                u   k-vector storing initial estimate
                b   k-vector storing right-hand side
                tol real number providing the required convergence tolerance

    RESULTS:    u   k-vector storing solution
    """
    #Get dimension
    k = len(A)

    #Make sure matrix A is float
    A = A.astype(float)

    #Set the maximum number of iterations
    maxit = 10000

    #Initialise the iteration counter
    it = 0

    #Initialise diffRMS to exceed tol for the first iteration
    diffRMS = 2*tol

    unew = np.zeros([k,1])
    while ((diffRMS > tol) and (it < maxit)):
        for j in xrange(k):
            unew[j] = u[j] + (b[j] - np.dot(A[j,:],u)) / A[j,j]

        diffRMS = 0
        for j in xrange(k):
            diffRMS = diffRMS + (unew[j] - u[j])**2

        it += 1
        diffRMS = np.sqrt(diffRMS)
        u = np.copy(unew)

    if (diffRMS) > tol:
        print 'Warning! Iteration has not converged'

    return u, it

########################################################################
###ACKNOWLEDGEMENT: TAKEN FROM VLE (SPECIFICALLY FROM matrixSolve.py)###
########################################################################
def gauss_seidel_new(A,u,b,tol):
    """
    Solve the system A u = b using a Gauss-Seidel iteration

    ARGUMENTS:  A   k x k matrix
                u   k-vector storing initial estimate
                b   k-vector storing right-hand side
                tol real number providing the required convergence tolerance

    RESULTS:    u   k-vector storing solution
    """

    #Get dimension
    k = len(A)

    #Make sure matrix A is float
    A = A.astype(float)

    #Set the maximum number of iterations
    maxit = 10000

    #Initialise the iteration counter
    it = 0

    #Initialise diffRMS to exceed tol for the first iteration
    diffRMS = 2*tol

    while ((diffRMS > tol) and (it < maxit)):
        uold = np.copy(u)

        for j in xrange(k):
            u[j] = u[j] + (b[j] - np.dot(A[j,:],u))/A[j,j]

        diffRMS = 0
        for j in xrange(k):
            diffRMS = diffRMS + (u[j] - uold[j])**2

        it += 1
        diffRMS = np.sqrt(diffRMS)

    if (diffRMS) > tol:
        print 'Warning! Iteration has not converged'

    return u, it

###########################################################################
###ACKNOWLEDGEMENT: MODIFIED FROM VLE (SPECIFICALLY FROM matrixSolve.py)###
###########################################################################
def sor_new(A,u,b,k,tol,w):
    """
    Solve the system A u = b using a Gauss-Seidel iteration

    ARGUMENTS:  A   k x k matrix
                u   k-vector storing initial estimate
                b   k-vector storing right-hand side
                k   integer dimension of system (NOT USED)
                tol real number providing the required convergence tolerance
                w   weight factor for the iterations

    RESULTS:    u   k-vector storing solution
    """

    #Get dimension
    k = len(A)

    #Make sure matrix A is float
    A = A.astype(float)

    #Set the maximum number of iterations
    maxit = 10000

    #Initialise the iteration counter
    it = 0

    #Initialise diffRMS to exceed tol for the first iteration
    diffRMS = 2*tol

    while ((diffRMS > tol) and (it < maxit)):
        uold = np.copy(u)
        for j in xrange(k):

            p = u[j] + (b[j] - np.dot(A[j,:],u))/A[j,j]
            u[j] = w*p + (1-w)*u[j] #Successive Over-Relaxation improvement

        diffRMS = 0
        for j in xrange(k):
            diffRMS = diffRMS + (u[j] - uold[j])**2

        it += 1
        diffRMS = np.sqrt(diffRMS)

    if (diffRMS) > tol:
        print 'Warning! Iteration has not converged'

    return u, it

def solveSystemUsingJacobi():
    """
    Solves and plots the system of equations for the temperature distribution
    problem using Jacobi iteration.
    """

    #The list of the number of approximation points required in each direction
    #to be iterated through
    m_list = [9, 17, 33]
    tolerance = 10 ** -5

    for m in m_list:
        A, b, Temp = generateSystemOfEquations(m)

        #Initial guess of the solution
        x = np.zeros([(m-2)**2, 1])

        #Solving the system of linear equations and timing them
        t0 = time.clock()
        u, it = jacobi_new(A,x,b,tolerance)
        time_taken = time.clock() - t0

        unknown_points = (m-2) * (m-2)
        centre_temp = u[len(u)//2][0]
        error = 25.0 - centre_temp


        print "m: {} || Unknown Points: {} || Centre Temp: {:.6f} || " \
              "Error: {:.3e} || Time Taken: {:.1e} || Iter: {}"\
            .format(m, unknown_points, centre_temp, error, time_taken, it)

        plotSystem(Temp, u, m)

def solveSystemUsingGaussSeidel():
    """
    Solves and plots the system of equations for the temperature distribution
    problem using Gauss-Siedel iteration.
    """

    #The list of the number of approximation points required in each direction
    #to be iterated through
    m_list = [9, 17, 33]
    tolerance = 10 ** -5

    for m in m_list:
        A, b, Temp = generateSystemOfEquations(m)

        #Initial guess of the solution
        x = np.zeros([(m-2)**2, 1])

        #Solving the system of linear equations and timing them
        t0 = time.clock()
        u, it = gauss_seidel_new(A,x,b,tolerance)
        time_taken = time.clock() - t0

        unknown_points = (m-2) * (m-2)
        centre_temp = u[len(u)//2][0]
        error = 25.0 - centre_temp


        print "m: {} || Unknown Points: {} || Centre Temp: {:.6f} || " \
              "Error: {:.3e} || Time Taken: {:.1e} || Iter: {}"\
            .format(m, unknown_points, centre_temp, error, time_taken, it)

        plotSystem(Temp, u, m)

def solveSystemUsingSOR():
    """
    Solves and plots the system of equations for the temperature distribution
    problem using Successive Over-Relaxation (SOR).
    """

    #The list of the number of approximation points required in each direction
    #to be iterated through
    m_list = [17, 33]
    tolerance = 10 ** -5
    w = 1.9

    for m in m_list:
        A, b, Temp = generateSystemOfEquations(m)

        #Initial guess of the solution
        x = np.zeros([(m-2)**2, 1])

        #Solving the system of linear equations and timing them
        t0 = time.clock()
        u, it = sor_new(A,x,b,0,tolerance,w)
        time_taken = time.clock() - t0

        unknown_points = (m-2) * (m-2)
        centre_temp = u[len(u)//2][0]
        error = 25.0 - centre_temp


        print "w: {} || m: {} || Unknown Points: {} || Centre Temp: {:.6f} || " \
              "Error: {:.3e} || Time Taken: {:.1e} || Iter: {}"\
            .format(w, m, unknown_points, centre_temp, error, time_taken, it)

        plotSystem(Temp, u, m)

def main():
    """
    Runs all the different algorithm types to solve the heat problem.
    """
    solveSystemUsingLinalg()
    solveSystemUsingJacobi()
    solveSystemUsingGaussSeidel()
    solveSystemUsingSOR()

if __name__ == "__main__":
    main()
