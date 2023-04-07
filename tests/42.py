
import turtle
from PIL import Image

# set up the turtle canvas
turtle.speed(0)
# move the turtle to the top-left corner of the canvas
turtle.penup()
turtle.setpos(-150, 150)
turtle.pendown()

# draw the chessboard
for i in range(10):
    for j in range(3):
        if (i + j) % 2 == 0:
            turtle.begin_fill()
        for k in range(4):
            turtle.forward(100)
            turtle.right(90)
        turtle.end_fill()
        turtle.forward(100)
    turtle.backward(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)

# save the chessboard as an image
turtle.getcanvas().postscript(file="chessboard.eps")
Image.open("chessboard.eps").convert("RGB").crop((1, 1, 210, 310)).save("chessboard.png")

# keep the turtle window open until manually closed
turtle.done()
