        ### A quadratic solver and plotter via using a Class ### 

##### CAN PERHAPS SLAUGHTER THE UNFACTORIZED INPUTTING PROCEDURE IN DEF MAIN
##### I.E. REPETITIVE INPUT STATEMENTS ON VARIOUS A, B, C

##### ALSO, NOTE GETALLCOORD, GETSCALEDCOORD AND DRAW WHICH ALL CALL EACH
##### OTHER CHRONOLOGICALLY HENCE DEPENDANT TO A CERTAIN EXTENT; BAD PRACTICE?
##### SHOULD THOSE CALLS BE DONE IN MAIN() AND PASSED THROUGH ARGUMENTS OF
##### THE FUNCTIONS?

from tkinter import *

class QuadraticEquation():
    """ a representation of a quadratic equation (ax^2 + bx + c) """


    def __init__(self, a=1, b=-1, c=-1):
        """ a, b, c refer to the coefficients of the quadratic equation """
        self.a = a
        self.b = b
        self.c = c


    def __str__(self):
        """ returns the polynomial in the form of ax^2 + bx + c """
        template = "Q-Equation: ({})x\u00B2 + ({})x + ({})"
        return template.format(self.a, self.b, self.c)


    def __repr__(self):
        """ returns the actual string used to instantiate the variable """
        template = "QuadraticEquation({}, {}, {})"
        return template.format(self.a, self.b, self.c)
    

    def getDiscriminant(self):
        """ returns the discriminant of the quadratic equation (b^2 - 4ac) """
        return self.b**2 - (4 * self.a * self.c)


    def getRoot1(self):
        """ finds the first root of the quadratic equation """
        disc = self.getDiscriminant()
        return (-self.b + disc**0.5)/(2*self.a)
    

    def getRoot2(self):
        """ finds the second root of the quadratic equation """
        disc = self.getDiscriminant()
        return (-self.b - disc**0.5)/(2*self.a)


    def getCoord(self):
        """ yields x & y coordinates on the curve """
        half_amount_coords = 100
        f = lambda x : self.a*x**2 + self.b*x + self.c
        
        for coord_x in range(-half_amount_coords, half_amount_coords):
            yield coord_x, f(coord_x)


    def getAllCoord(self):
        """ returns all x & y coords as a single list range(amount_coords)"""
        half_amount_coords = 100

        coord_gen = self.getCoord()
        coord_list = []
    
        for _ in range(2*half_amount_coords):
            
            coord = next(coord_gen)       
            coord_list.append(coord[0])
            coord_list.append(coord[1])

        return coord_list


    def getScaledAllCoord(self):
        """ shifts and rescales the coordinates for further visibility """
        scale = -10     # for tkinter
        shift = 200

        coord_list = self.getAllCoord()
        
        scaled_coord_list = [scale*coord + shift for coord in coord_list]
        return scaled_coord_list


    def draw(self):
        """ draws the quadratic equation graphically using tkinter """

        scaled_coord_list = self.getScaledAllCoord()

        root = Tk()

        canvas = Canvas(root, bg="white", width=500, height=500)
        canvas.create_line(scaled_coord_list)
        canvas.pack()
        
        root.mainloop()



def main():
    """ runs a test on the QuadraticEquation() class """


    while True:
        try:
            print("Wecome to <Q.E.D> , version 1.2.3, "
                  "the Quite Easily Done version!\n"
                  "Please input your coefficients")

            a = int(input("a: "))
            b = int(input("b: "))
            c = int(input("c: "))
            break
        
        except ValueError:
            print("RETARD ALERT.")
            

    eq1 = QuadraticEquation(a, b, c)


    if(eq1.getDiscriminant() > 0):
        print("Root1: {} || Root2: {}".format(eq1.getRoot1(), eq1.getRoot2()))

    elif(eq1.getDiscriminant() == 0):
        unique_root = eq1.getRoot1()
        print("Unique root: {}".format(unique_root))

    elif(eq1.getDiscriminant() < 0):
        print("There are no real roots at the very least.")

    eq1.draw()


main()
