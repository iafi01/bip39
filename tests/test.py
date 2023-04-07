import turtle
from PIL import Image

scr = turtle.Screen()
ttl = turtle.Turtle()

def draw_square(color):
    ttl.fillcolor(color)
    ttl.begin_fill()
    for i in range(4):
        ttl.forward(35)
        ttl.left(90)
    ttl.end_fill()

# Main driving Code
if __name__ == "__main__":
    scr.setup(750, 500)
    ttl.speed(0)  # increase speed for faster drawing
    ttl.penup()
    ttl.goto(-175, 175) # move to top left corner
    ttl.pendown()
    
    for i in range(2): # draw 11 squares on each row
        
        for j in range(1): # draw 12 squares on each column
            if (i+j)%2==0:
                draw_square("white")
            else:
                draw_square("black")

            ttl.penup()
            ttl.forward(35)
            ttl.pendown()

        # move to the next row
        ttl.penup()
        ttl.goto(-175, 175 - 35*(i+1))
        ttl.pendown()

    ttl.hideturtle()
    
    # Save image as PNG
    img = scr.getcanvas().postscript(colormode='color')
    Image.frombuffer('RGBA', (int(scr.window_width()), int(scr.window_height())), img, 'raw', 'RGBA', 0, 1).save("chessboard.png")

    turtle.done()
