import turtle
import math

# Function to draw filled circles
def draw_circle(t, color, size, x, y):
    t.penup()
    t.color(color)
    t.fillcolor(color)
    t.goto(x, y)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    t.pendown()

# Recursive pattern function
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.forward(length * n)
    t.left(angle)
    draw(t, length, n - 1)
    t.right(2 * angle)
    draw(t, length, n - 1)
    t.left(angle)
    t.backward(length * n)

# Function to draw a square with dynamic side length
def square(t, length):
    for _ in range(4):
        t.forward(length)
        t.left(90)

# Function to draw an n-sided regular polygon
def polygon(t, length, n):
    exterior_angle = 360 / n
    for _ in range(n):
        t.forward(length)
        t.left(exterior_angle)

# Function to approximate a circle using polygons
def circle(t, r):
    n = 100  # Number of sides for approximation
    circumference = 2 * math.pi * r
    length = circumference / n
    polygon(t, length, n)

# New function to draw an arc
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * (angle / 360)
    n = int(arc_length / 3) + 1  # Number of segments to approximate the arc
    step_length = arc_length / n
    step_angle = angle / n

    for _ in range(n):
        t.forward(step_length)
        t.left(step_angle)

# Create a turtle for drawing
tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(500)

# Draw filled circles
draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)

# Move to a new location and create another turtle for the pattern
bob = turtle.Turtle()
bob.shape("turtle")
bob.speed(500)

# Draw the recursive pattern
draw(bob, 10, 5)

# Reset bob's position and heading to draw a square
bob.penup()
bob.goto(-150, -150)  
bob.pendown()
bob.setheading(0)

# Test the square function
square(bob, 100)
bob.penup()
bob.goto(-50, -150)
bob.pendown()
square(bob, 150)
bob.penup()
bob.goto(100, -150)
bob.pendown()
square(bob, 200)

# Move to a new position and test polygons
bob.penup()
bob.goto(-150, 100)  
bob.pendown()
polygon(bob, 50, 3)  
bob.penup()
bob.goto(0, 100)  
bob.pendown()
polygon(bob, 50, 5)  
bob.penup()
bob.goto(150, 100)  
bob.pendown()
polygon(bob, 50, 6)  

# Test the arc function with various angles
bob.penup()
bob.goto(-200, -50)  
bob.pendown()
arc(bob, 50, 180)  # Half-circle arc
bob.penup()
bob.goto(0, -50)  
bob.pendown()
arc(bob, 100, 270)  # Three-quarter circle arc
bob.penup()
bob.goto(200, -50)  
bob.pendown()
arc(bob, 150, 360)  # Full circle arc

# Complete the drawing
turtle.done()
