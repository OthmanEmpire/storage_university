###




class Rectangle():
    """ a representation of a euclidean rectangle """


    def __init__(self, width=0, height=0):
        if(width >= 0 and height >=0):    
            self.width = width
            self.height = height
        else:
            raise ValueError("Rejected negative dimenisions.")


    def __str__():
        template = "Width: {} | Height: {}"
        print(template.format(width, height))

    def getArea():
        """ returns the area of the rectangle """
        return self.width * self.height


    def getPerimeter():
        """ returns the perimeter of the rectangle """
        return 2*(self.width + self.height)




rekt1 = Rectangle()

rekt1.__str__
