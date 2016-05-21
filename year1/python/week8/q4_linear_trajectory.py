            ### Solves a 2x2 system of linear equations ###

##### LOOK AT THAT MASS INPUT PARADE AT BOTTOM; SO NOOB. #####

from tkinter import *

class LinearEquation():
    """ a representation of two linear equations of the form ax + by = c """

    def __init__(self, a, b, c, d, e, f):
        """ a,b,c,d,e,f are coefficients of two equations of form ax + by = c"""
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f


    def __str__(self):
        """ returns the two equations in the form ax + by = c """
        template = "{}x + {}y = {}, {}x + {}y = {}"
        return template.format(self.a, self.b, self.c, self.d, self.e, self.f)

    
    def __repr__(self):
        """ returns the literal input for instantiation """
        template = "LinearEquation({},{},{},{},{},{})"
        return template.format(self.a, self.b, self.c, self.d, self.e, self.f)


    def isSolvable(self):
        """ returns True if linear equations are solvable otherwise false """
        if(self.a*self.d - self.b*self.c == 0):
            return False
        else:
            return True


    def getX(self):
        """ returns the x solution for the system of equations """
        numerator = self.e*self.d - self.b*self.f
        denominator = self.a*self.d - self.b*self.c
        return (numerator / denominator)


    def getY(self):
        """ returns the y solution for the system of equations """
        numerator = self.a*self.f - self.e*self.c
        denominator = self.a*self.d - self.b*self.c
        return (numerator / denominator)


    def getFourPoints(self):
        """ returns two points per single linear equation hence four points """

        scale = 100
        shift = 150

        eq1_coord_list = []
        eq2_coord_list = []

        eq1 = lambda x: (self.e - self.a*x) / (self.b)    # equation first line
        eq2 = lambda x: (self.f - self.c*x) / (self.d)    # equation second line

        for x in range(2):

            eq1_coord_list.append(scale*x + shift)
            eq1_coord_list.append(scale*eq1(x) + shift)

            eq2_coord_list.append(scale*x + shift)
            eq2_coord_list.append(scale*eq2(x) + shift)


        return eq1_coord_list, eq2_coord_list

            
        


    def draw(self):
        """ draws the two equations graphically using tkinter """
        
        eq1_coord_list, eq2_coord_list = self.getFourPoints()

        print(eq1_coord_list)
        print(eq2_coord_list)

        root = Tk()

        canvas = Canvas(root, bg="white", width=500, height=500)
        canvas.create_line(eq1_coord_list)
        canvas.create_line(eq2_coord_list)
        canvas.pack()

        root.mainloop()

        




def main():
    """ runs a test on the class LinearEquations() """

    print("Welcome to Linear Trajectory, where SunStrikes are noob "
          "friendly, version 1.0!\n")

    ##### NOOB ALERT #####
    a = int(input('a: '))
    ##### NOOB ALERT #####
    b = int(input('b: '))
    ##### NOOB ALERT #####
    c = int(input('c: '))
    ##### NOOB ALERT #####
    d = int(input('d: '))
    ##### NOOB ALERT #####
    e = int(input('e: '))
    ##### NOOB ALERT #####
    f = int(input('f: '))
    ##### NOOB ALERT #####

    le = LinearEquation(a, b, c, d, e, f)

    if(le.isSolvable()):
        x, y = le.getX(), le.getY()
        print("\nx = {}".format(x))
        print("y = {}\n".format(y))
    else:
        print("The equation has no unique solution")

 

    le.draw()
    
main()
