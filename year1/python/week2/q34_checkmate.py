### This program creates a chessboared ###

from tkinter import *

sides = 8

root = Tk()

canv = Canvas(root, bg = "#400000", width = 800, height = 800)

for i in range(sides):
    for n in range(sides):

        xshift = (2*i)*100
        yshift = (n)*100

        if(n%2 == 0):   # Shifts the print out of squares on x-axis for every other row
            xshift = (2*i - 1)*100

        canv.create_polygon(xshift,yshift,xshift+100,yshift,xshift+100,yshift+100,xshift,yshift+100, fill="#803520")


canv.pack()

canv.mainloop()



