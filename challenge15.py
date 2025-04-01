# Import the turtle module to use its graphics functionality
import turtle

# Function to draw a Koch curve of a given length
def koch_curve(t, length):
    # If the length is smaller than 3, just draw a straight line
    if length < 3:
        t.forward(length)
    else:
        # Otherwise, break it into smaller segments
        # Recursively draw the first third of the curve
        koch_curve(t, length / 3)
        # Turn the turtle left by 60 degrees
        t.left(60)
        # Recursively draw the second third of the curve
        koch_curve(t, length / 3)
        # Turn the turtle right by 120 degrees
        t.right(120)
        # Recursively draw the third third of the curve
        koch_curve(t, length / 3)
        # Turn the turtle left by 60 degrees
        t.left(60)
        # Recursively draw the final third of the curve
        koch_curve(t, length / 3)

# Function to draw a snowflake by drawing three Koch curves
def snowflake(t, length):
    for _ in range(3):
        koch_curve(t, length)  # Draw a single Koch curve with the specified length
        t.right(120)  # Turn the turtle right by 120 degrees to form the snowflake shape

# Create a turtle object named pepito to draw
pepito = turtle.Turtle()

# Create a screen object to control the turtle window
screen = turtle.Screen()

# Set the background color of the turtle graphics window to white
screen.bgcolor('white')

# Set the speed of the turtle to the fastest setting
pepito.speed('fastest')

# Move the turtle to an appropriate starting position without drawing
pepito.penup()
pepito.goto(-150, 90)  # Start in a better position for drawing
pepito.pendown()

# Draw the snowflake with a side length of 300 using the snowflake function
snowflake(pepito, 300)

# Add color
pepito.color('blue')
pepito.fillcolor('lightblue')

# Complete the drawing
pepito.hideturtle()
screen.mainloop()  # Keep the window open
