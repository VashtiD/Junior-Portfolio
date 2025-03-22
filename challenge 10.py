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
        t.forward(length)  # Use the dynamic length
        t.left(90)         # Turn left by 90 degrees

# Function to draw an n-sided regular polygon
def polygon(t, length, n):
    exterior_angle = 360 / n  # Calculate the exterior angle
    for _ in range(n):
        t.forward(length)      # Move forward by length
        t.left(exterior_angle) # Turn by the exterior angle

# Function to approximate a circle using polygons
def circle(t, r):
    n = 100  # Number of sides for approximation
    circumference = 2 * math.pi * r
    length = circumference / n  # Length of each side
    polygon(t, length, n)  # Draw the approximated circle

# Create a turtle for drawing circles
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
bob.goto(-150, -150)  # Move the turtle to a new position
bob.pendown()
bob.setheading(0)     # Set the heading to face right

# Test the square function with different lengths
square(bob, 100)  # First test with length 100
bob.penup()
bob.goto(-50, -150)  # Move to a new position for the next test
bob.pendown()
square(bob, 150)  # Second test with length 150
bob.penup()
bob.goto(100, -150)  # Move to a new position for the next test
bob.pendown()
square(bob, 200)  # Third test with length 200

# Reset bob's position and heading to draw polygons
bob.penup()
bob.goto(-150, 100)  # Move to a new position for polygons
bob.pendown()

# Test the polygon function with different values of n
polygon(bob, 50, 3)  # Draw a triangle
bob.penup()
bob.goto(0, 100)  # Move to a new position for the next polygon
bob.pendown()
polygon(bob, 50, 5)  # Draw a pentagon
bob.penup()
bob.goto(150, 100)  # Move to a new position for the next polygon
bob.pendown()
polygon(bob, 50, 6)  # Draw a hexagon

# Test the circle function with various radii
bob.penup()
bob.goto(-200, -50)  # Move to a new position for the circles
bob.pendown()
circle(bob, 50)  # Test with radius 50
bob.penup()
bob.goto(0, -50)  # Move to a new position for the next circle
bob.pendown()
circle(bob, 100)  # Test with radius 100
bob.penup()
bob.goto(200, -50)  # Move to a new position for the next circle
bob.pendown()
circle(bob, 150)  # Test with radius 150

# Complete the drawing
turtle.done()
