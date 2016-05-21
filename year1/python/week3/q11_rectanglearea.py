### This program calculates the area of a rectangle ###

def rectArea(width, height):

    area = width * height
    return area

width, height = input("Welcome... Please input width and height of rectangle: ").split()

width = int(width)
height = int(height)

area = rectArea(width, height)
print(area)
