### A 2D graphical representation program that is based on Classes ###

import tkinter
import math


class Shape():
    """ King Arthur """

    def __init__(self, x, y, colour):
        """ King Arthur """
        self.x = x
        self.y = y
        self.colour = colour


    def draw(self, canvas):
        """ King Arthur """
        try:
            raise NotImplementedError
        except NotImplementedError:
            print("The feature has not been implemented.")



class Rectangle(Shape):
    """ King Arthur """

    def __init__(self, x, y, colour="blue", width=100, height=200):
        """ King Arthur """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.id = None


    def draw(self, canvas):
        """ Le art """
        coord = (self.x, self.y, self.x + self.width, self.y + self.height)
        self.id = canvas.create_rectangle(coord, fill=self.colour)


    def __str__(self):
        """ King Arthur """
        return str(self.id)


    def requestInput(self):
        """ King Arthur """

        arguments = ["x", "y", "colour", "width", "height"]
        kwargs = {}

        print("Please enter the parameters of the rectangle. \n"""
              "Note: you can enter 'default' option for colour, width & "
              "height.\n")

        for arg in arguments:

            value = input("Please enter {}: ".format(arg))

            if(value != "default"):
                kwargs[arg] = value

                if(arg != "colour"):
                    kwargs[arg] = int(value)

        return kwargs



class Graphics2D():
    """ King Arthur """

    def __init__(self, colour="white", width=300, height=300):
        """ King Arthur """
        self.window = tkinter.Tk()
        self.window.geometry("300x300")
        self.window.title("You got a point there.")

        self.canvas = tkinter.Canvas(self.window, width=300, height=300)
        self.canvas.pack()

        self.shapes = []


    def addShape(self, shape):
        """ King Arthur """
        self.shapes.append(shape)


    def removeShape(self, shape):
        """ King Arthur """
        try:
            self.shapes.remove(shape)
        except ValueError as e:
            print("The shape '{}' is not in the list of shapes stored.".format(
                shape))


    def draw(self):
        """ King Arthur """
        for shape in self.shapes:
            shape.draw(self.canvas)
      
        self.window.mainloop()



class Square(Rectangle):
    """ King Arthur """

    def __init__(self, x, y, colour="orange", width=100, height=100):
        super().__init__(x, y, colour, width, height)
        self.width = self.height


    def requestInput(self):
        """ King Arthur """

        arguments = ["x", "y", "colour", "width"]
        kwargs = {}

        print("Please enter the parameters of the square. \n"""
              "Note: you can enter 'default' option for colour, width.\n")

        for arg in arguments:

            value = input("Please enter {}: ".format(arg))

            if(value != "default"):
                kwargs[arg] = value

                if(arg != "colour"):
                    kwargs[arg] = int(value)

                if(arg == "width"):
                    kwargs["height"] = kwargs["width"]

        return kwargs



class Oval():
    """ King Arthur """

    def __init__(self, x0, y0, x1, y1, colour="pink"):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.colour = colour
        self.id = None


    def draw(self, canvas):
        """ Le art """
        coord = (self.x0, self.y0, self.x1, self.y1)
        self.id = canvas.create_oval(coord, fill=self.colour)


    def requestInput(self):
        """ King Arthur """

        arguments = ["x0", "y0", "x1", "y1", "colour"]
        kwargs = {}

        print("Please enter the parameters of the oval. \n"""
              "Note: you can enter 'default' option for colour.\n")

        for arg in arguments:

            value = input("Please enter {}: ".format(arg))

            if(value != "default"):
                kwargs[arg] = value

                if(arg != "colour"):
                    kwargs[arg] = int(value)

        return kwargs


    def __str__(self):
        """ King Arthur """
        return str(self.id)



class Circle(Oval):
    """ King Arthur """

    def __init__(self, x0, x1, colour="purple"):
        """ King Arthur """
        self.x0 = x0
        self.y0 = x0
        self.x1 = x1
        self.y1 = x1
        self.colour = colour
        self.id = None


    def requestInput(self):
        """ King Arthur """

        arguments = ["x0", "x1", "colour"]
        kwargs = {}

        print("Please enter the parameters of the circle. \n"""
              "Note: you can enter 'default' option for colour.\n")

        for arg in arguments:

            value = input("Please enter {}: ".format(arg))

            if(value != "default"):
                kwargs[arg] = value

                if(arg != "colour"):
                    kwargs[arg] = int(value)

        return kwargs



class RegularPolygon():
    """ a representation of a regular euclidean polygon """

    def __init__(self, n=3, side=1, x=0, y=0, colour="brown"):
        """ a polygon with 'n' sides of length 'sides', centered at (x,y) """
        self.n = n
        self.side = side
        self.x = x
        self.y = y
        self.colour = colour
        self.id = None

    # Setter and Getter methods below (or accessors and mutators)

    def getN(self):
        """ gets the number of sides of the regular polygon """
        return self.n

    def setN(self, new_n):
        """ sets the number of sides of the regular polygon """
        self.n = new_n

    def getSide(self):
        """ gets the length of the sides of the regular polygon """
        return self.side

    def setSide(self, new_side):
        """ sets the length of sides of the regular polygon """
        self.side = new_side

    def getX(self):
        """ gets the x-coord of the center of the regular polygon """
        return self.x

    def setX(self, new_x):
        """ sets the x-coord of the center of the regular polygon """
        self.x = new_x

    def getY(self):
        """ gets the y-coord of the center of the regular polygon """
        return self.y

    def setY(self, new_y):
        """ sets the x-coord of the center of the regular polygon """
        self.y = new_y


    def __str__(self):
        """ returns number of sides and length of sides of regular polygon """
        template = "Number of sides: {} || Length of sides: {}"
        return template.format(self.n, self.side)


    def __repr__(self):
        """ returns the string of class along with its corresponding inputs """
        template = "RegularPolygon({}, {}, {}, {})"
        return template.format(self.n, self.side, self.x, self.y)


    def getArea(self):
        """ returns the area of the regular polygon """
        import math
        return (self.side**2 * self.n) / (4 * math.tan(math.pi/self.n))


    def getPerimeter(self):
        """ returns the perimeter of the regular polygon """
        return self.n * self.side


    # calculates points via trigonometry (resolving lengths and then
    # consecutively adding them up to find the next coordinate)
    def getPoints(self):
        """ returns all the coordinates of the vertices on the polygon """
        scale = 1

        poly_x = 0
        poly_y = 0
        coord = []

        poly_angle = 2*math.pi / self.n

        for i in range(self.n):

            angle = poly_angle*i

            x_coord = self.side * math.cos(angle)
            y_coord = self.side * math.sin(angle)

            poly_x += x_coord
            poly_y += y_coord

            coord.append(scale*poly_x + self.x)   # +self.x for centering
            coord.append(scale*poly_y + self.y)   # +self.y for centering

        return coord


    def draw(self, canvas):
        """ King Arthur """
        coord = self.getPoints()
        self.id = canvas.create_polygon(coord, fill=self.colour)


    def requestInput(self):
        """ King Arthur """

        arguments = ["n", "side", "x", "y", "colour"]
        kwargs = {}

        print("Please enter the parameters of the regular polygon. \n"""
              "Note: you can enter 'default' option for colour, width.\n")

        for arg in arguments:

            value = input("Please enter {}: ".format(arg))

            if(value != "default"):
                kwargs[arg] = value

                if(arg != "colour"):
                    kwargs[arg] = int(value)

        return kwargs




def main():
    """ King Arthur """

    euclidian = Graphics2D()

    while True:

        print("Welcome to Euclidian's incomplete world!\n")
        print("Kindly choose a choice below to make your point.\n"
              "1. Draw a Rectangle\n"
              "2. Draw a Square\n"
              "3. Draw a Circle\n"
              "4. Draw an Oval\n"
              "5. Draw a regular Polygon\n"
              "6. Delete a shape\n"
              "7. Print all IDs\n"
              "8. Print all shapes\n")

        choice = input("Point: ")



        if(choice == '1'):

            rekt = Rectangle(0,0)
            kwargs = rekt.requestInput()
            rekt = Rectangle(**kwargs)

            euclidian.addShape(rekt)


        elif(choice == '2'):

            squa = Square(0,0)
            kwargs = squa.requestInput()
            squa = Square(**kwargs)

            euclidian.addShape(squa)


        elif(choice == '3'):

            circ = Circle(0,0)
            kwargs = circ.requestInput()
            circ = Circle(**kwargs)

            euclidian.addShape(circ)


        elif(choice == '4'):

            oval = Oval(0,0,0,0)
            kwargs = oval.requestInput()
            oval = Oval(**kwargs)

            euclidian.addShape(oval)


        elif(choice == '5'):

            regu = RegularPolygon()
            kwargs = regu.requestInput()
            regu = RegularPolygon(**kwargs)

            euclidian.addShape(regu)


        elif(choice == '6'):

            id = input("ID of shape to delete: ")

            try:
                euclidian.removeShape(id)
            except ValueError as e:
                print(e)


        elif(choice == '7'):
            for shape in euclidian.shapes:
                print(type(shape), shape.id)


        elif(choice == '8'):
            euclidian.draw()

        else:
            print("GG")





if __name__ == '__main__':
    main()
