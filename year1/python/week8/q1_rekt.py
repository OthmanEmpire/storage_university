            ### A representation of a rectangle as a class ###

##### BONUS: ADD YIELD/GENERATOR FUNCTIONALITY TO THE DRAW FUNCTION
##### SO THAT RECTANGLES DRAWN ARE NOT OVERLAPPED

from tkinter import * ### WHY? ###

# A class that represents a euclidean rectangle
class Rectangle:
    """ representation of a geometric rectangle """

    def __init__(self, width=0, height=0):
        """ creates a new rectangle object with height and width defaulting
         defaulting to zero """

        if(width >= 0 or height >= 0):            
            self.width = width
            self.height = height
        else:
            raise ValueError("Non-negative dimensions are rejected")

            
    def __str__(self):
        """ returns a string that denotes height and width of rectangle """
        template = "Height {} || Width: {}"
        return template.format(self.height, self.width)


    def __repr__(self):
        """ returns a representation of the object for debugging purposes """
        template = "Rectangle(width={}, height={}"
        return template.format(self.width, self.height)


    def getArea(self):
        """ returns the area of the rectangle """
        return self.width*self.height
        

    def getPerimeter(self):
        """ returns the perimeter of the rectangle """
        return 2*(self.width + self.height)


    def draw(self):
        """ graphically draws the rectangle via tkinter library """

        scale = 10
        coord = [0, 0,
                 scale*self.width, 0,
                 scale*self.width, scale*self.height,
                 0, scale*self.height]

        root = Tk()

        canvas = Canvas(root, bg="white", height=500, width=500)    
        canvas.create_polygon(coord,fill ="#476042")
        canvas.pack()
        canvas.mainloop()



def main():
    """ Runs a test on the rectangle class then draws the results on tkinter """

    rekt1 = Rectangle(4, 40)
    rekt2 = Rectangle(3.5, 35.7)
    rekt3 = Rectangle(100, 100)

    area1 = rekt1.getArea()
    area2 = rekt2.getArea()

    perimeter1 = rekt1.getPerimeter()
    perimeter2 = rekt2.getPerimeter()

    print("Area: {:.1f} || Perimieter: {:.1f}".format(area1, perimeter1))
    print("Area: {:.1f} || Perimieter: {:.1f}".format(area2, perimeter2))
    
    rekt1.draw()
    rekt2.draw()

main()
