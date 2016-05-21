    ### A program that represents a regular polygon in Euclidean space ###

from tkinter import *
import math


class RegularPolygon():
    """ a representation of a regular euclidean polygon """

    def __init__(self, n=3, side=1, x=0, y=0):
        """ a polygon with 'n' sides of length 'sides', centered at (x,y) """
        self.n = n
        self.side = side
        self.x = x
        self.y = y

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
        scale = 20
        
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

            coord.append(poly_x)   # +self.x for centering 
            coord.append(poly_y)   # +self.y for centering

        return coord


class Gui():
    selectedRegularPolygon = 0
    regularPolygons = []

    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.geometry("768x768+300+300")
        self.mainWindow.configure(background="white")
        self.mainWindow.title("RegularPolygon")
        self.mainFrame = Frame(self.mainWindow)
        self.mainFrame.pack(fill="both", expand=True)

        self.bottomFrame = Frame(self.mainWindow)
        self.bottomFrame.pack(side="bottom",fill="both")
        self.bottomFrame.pack_propagate(0)
        self.bottomFrame.configure(width="768",height="50")

        self.createMainCanvas()
        self.createLabelArea()
        self.createLabelPerimeter()
        self.createButton("<<")
        self.createButton(">>")

    def createMainCanvas(self):
        self.mainCanvas = Canvas(self.mainFrame, bg="gray")
        self.mainCanvas.addtag_all("all")
        self.mainCanvas.pack(fill="both", expand=True)

    def createLabelArea(self):
        self.lblArea = Label(self.bottomFrame)
        self.lblArea.configure(width="20", height="50")
        self.lblArea.configure(bg="pink",fg="white")
        self.lblArea.pack(side="left")

    def createLabelPerimeter(self):
        self.lblPerimeter = Label(self.bottomFrame)
        self.lblPerimeter.configure(width="20", height="50")
        self.lblPerimeter.configure(bg="lightBlue",fg="white")
        self.lblPerimeter.pack(side="left")
    
    def setLabelAreaText(self, text):
        template = "Area: {:.2f}".format(text)
        self.lblArea.configure(text=template)

    def setLabelPerimeterText(self, perimeter):
        template = "Perimeter: {}".format(perimeter)
        self.lblPerimeter.configure(text=template)

    def createButton(self, text):
        Label(self.bottomFrame, width="5").pack(side="left")
        btnNext = Button(self.bottomFrame, text=text)
        btnNext.configure(width="20", height="50")
        btnNext.configure(command=lambda: self.selectRegularPolygon(text))
        btnNext.pack(side="left")

    def selectRegularPolygon(self, buttonPressed):
        if( self.selectedRegularPolygon > 2 ):
            self.selectedRegularPolygon = 0
            
        if( self.selectedRegularPolygon < 0 ):
            self.selectedRegularPolygon = 2

        print(self.regularPolygons)
        
        self.drawRegularPolygon(
            self.regularPolygons[self.selectedRegularPolygon] )

        if( buttonPressed == "<<" ):
            self.selectedRegularPolygon -= 1
        if( buttonPressed == ">>" ):
            self.selectedRegularPolygon += 1

    def drawRegularPolygon(self, selectedRegularPolygon):
        area = selectedRegularPolygon.getArea()
        perimeter = selectedRegularPolygon.getPerimeter()
        points = selectedRegularPolygon.getPoints()

        self.setLabelAreaText(area)
        self.setLabelPerimeterText(perimeter)

        self.mainCanvas.create_polygon(points, fill="red")
        self.mainCanvas.scale("all",-5,-5,40,40)
        self.mainCanvas.pack(fill="both", expand=True)     

    def loadRegularPolygons(self, regularPolygons):
        self.regularPolygons = regularPolygons     

    
if __name__ == "__main__":
    r1 = RegularPolygon()
    r2 = RegularPolygon(6, 4)
    r3 = RegularPolygon(10, 4, 5.6, 7.8)

    regularPolygons = [r1, r2, r3]
    
    app = Gui()
    app.loadRegularPolygons(regularPolygons)
    app.mainWindow.mainloop()
    


