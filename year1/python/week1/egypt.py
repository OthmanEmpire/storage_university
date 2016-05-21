### This program uses the tkinter library to draw egypt ###



from tkinter import *

# Creates a new window without a canvas
main = Tk()

# Creates a canvas to draw on
canvas = Canvas(main, bg="darkred", height=500, width=2000)

# Creates a sun rising from the west.
canvas.create_oval(10,10,150,150, fill ="darkorange")

# Creates a pyramid
canvas.create_polygon(0,500,250,250,500,500, fill="#fa7")

# Creates the beam of light reflected by the sun via the pyramid
canvas.create_polygon(1300,500,250,250,1200,500, fill="#FFF")




















# Updates data on screen & ensures everything fits in properly
canvas.pack()
