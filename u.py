import turtle
from tkinter import messagebox
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.title("Drawing Program")
pen = turtle.Turtle()
pen.speed(0) 
pen.hideturtle()
def draw_square(x, y, color, size):
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.pencolor(color) 
    pen.fillcolor(color) 
    for _ in range(4):
        pen.forward(size)
        pen.left(90)
    pen.end_fill() 

def draw_circle(x, y, color, size):
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.pencolor(color)
    pen.fillcolor(color)
    pen.circle(size / 2)
    pen.end_fill()

def draw_triangle(x, y, color, size):
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.pencolor(color)
    pen.fillcolor(color)
    for _ in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()

def handle_click(x, y):
    global current_shape, current_color, current_size
    if current_shape == "square":
        draw_square(x, y, current_color, current_size)
    elif current_shape == "circle":
        draw_circle(x, y, current_color, current_size)
    elif current_shape == "triangle":
        draw_triangle(x, y, current_color, current_size)

current_shape = "square"
current_color = "black"
current_size = 20

screen.onclick(handle_click) 
def select_square(x,y):
    global current_shape
    current_shape = "square"

def select_circle(x,y):
    global current_shape
    current_shape = "circle"

def select_triangle(x,y):
    global current_shape
    current_shape = "triangle"


square_button = turtle.Turtle()
square_button.penup()
square_button.goto(-200, -250)
square_button.pendown()
square_button.shape('square')
square_button.write("Square", font=("Arial", 14))
square_button.onclick(select_square)

circle_button = turtle.Turtle()
circle_button.penup()
circle_button.goto(0, -250)
circle_button.pendown()
circle_button.shape('circle')
circle_button.write("Circle", font=("Arial", 14))
circle_button.onclick(select_circle)

triangle_button = turtle.Turtle()
triangle_button.penup()
triangle_button.goto(200, -250)
triangle_button.pendown()
triangle_button.shape('triangle')
triangle_button.write("Triangle", font=("Arial", 14))
triangle_button.onclick(select_triangle)

def change_color(color):
    global current_color
    current_color = color

color_options = ["black", "red", "green", "blue"]
button_x = -200
for color in color_options:
    color_button = turtle.Turtle()
    color_button.penup()
    color_button.goto(button_x, -150)
    color_button.pendown()
    color_button.shapesize(2)
    color_button.dot(10, color)
    color_button.onclick(lambda x, y, c=color: change_color(c))
    button_x += 50

def change_size(size_change):
    global current_size
    current_size += size_change
    if current_size < 5:
        current_size = 5
messagebox.showinfo("Instructions","Click on the cursors for color and size changes, and click on the shapes to change shape")
size_up_button = turtle.Turtle()
size_up_button.penup()
size_up_button.goto(-200, -100)
size_up_button.pendown()
size_up_button.write("+", font=("Arial", 14))
size_up_button.onclick(lambda x, y: change_size(20))

size_down_button = turtle.Turtle()
size_down_button.penup()
size_down_button.goto(0, -100)
size_down_button.pendown()
size_down_button.write("-", font=("Arial", 14))
size_down_button.onclick(lambda x, y: change_size(-20))
turtle.done()
