### This program creates a chessboared ###

from tkinter import *

import tkinter


def createNumberBoard():

    print_number = 0
    
    squares = 10
    square_size = 100

    
    wid = squares*square_size
    hei = squares*square_size

    root = Tk()

    canv = Canvas(root, bg = "#400000", width = wid, height = hei)

    for y in range(squares):
        for x in range(squares):

            xshift = (2*x)*square_size      # prints even squares across x-axis
            yshift = (y)*square_size
            
            xmid = (x*square_size) + (square_size/2)
            ymid = (y*square_size) + (square_size/2)

            if(y%2 == 0):       # Allows printing of odd squares across x-axis
                xshift = (2*x-1)*square_size

            print_number += 1

            coord = [xshift, yshift,\
                     xshift + square_size,yshift,\
                     xshift + square_size, yshift + square_size,\
                     xshift, yshift + square_size]
          
            canv.create_polygon(coord ,fill="#803520")
            z = canv.create_text(xmid, ymid, fill = "white", font = ('', 20),\
                             text = print_number)

            print(z)

            

    canv.delete(z)
   


          
            
    canv.pack()

    canv.mainloop()



createNumberBoard()
