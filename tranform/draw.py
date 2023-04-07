import turtle
import tkinter as tk
from PIL import Image, ImageTk
import io
import sys
import save

scr = turtle.Screen()
ttl = turtle.Turtle()
turtle.title("Bip39")

def draw_square():
    for i in range(4):
        ttl.forward(35)
        ttl.left(90)

def draw(arr):
    scr.setup(750, 500)
    ttl.speed(0)
    ttl.penup()
    ttl.goto(-175, 175) 
    ttl.pendown()
    
    for i in range(12): 
        
        for j in range(11): 
            
            if arr[i][j] == "0":
                ttl.fillcolor("white")
            else:
                ttl.fillcolor("black")

            ttl.begin_fill()
            draw_square()
            ttl.end_fill()
            
            ttl.penup()
            ttl.forward(35)
            ttl.pendown()

        
        ttl.penup()
        ttl.goto(-175, 175 - 35*(i+1))
        ttl.pendown()

    ttl.hideturtle()
    save.save(arr)
    turtle.done()
    return
    
