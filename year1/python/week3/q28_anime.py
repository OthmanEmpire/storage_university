from tkinter import *

width  = 1000
height = 1000
x_velocity = 5
y_velocity = 5

# function that changes the position of the ball
def animate(canvas):
    canvas.after(50) # 50 ms delay
    canvas.move('ball', x_velocity, y_velocity)
    canvas.update()


main = Tk()
canvas = Canvas(main, width = width, height = height)
canvas.create_oval(0,0,100,100, fill = "red", tag = 'ball')
canvas.pack()



while True:
   animate(canvas)
