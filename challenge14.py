# Import the turtle module to use its graphics functionality

import turtle

import math


# Define the draw_spiral function that draws an Archimedean spiral

def draw_spiral(t, n, length, a, b):

    """

    Arguments:

      t: turtle object

      n: how many line segments to draw

      length: how long each segment is

      a: how loose the initial spiral starts out (larger is looser)

      b: how loosely coiled the spiral is (larger is looser)

    """

    # Initialize the angle (theta) to 0.0

    theta = 0.0


    # Loop to draw 'n' line segments

    for _ in range(n):

        # Move the turtle forward by the specified length

        t.forward(length)


        # Calculate the change in angle (dtheta) based on the formula 1 / (a + b * theta)

        dtheta = 1 / (a + b * theta)


        # Turn the turtle left by the calculated angle (dtheta)

        t.left(math.degrees(dtheta))  # Convert radians to degrees


        # Update the angle (theta) for the next iteration

        theta += dtheta


# Create a turtle object named pepito

pepito = turtle.Turtle()


# Create a screen object to control the turtle window

screen = turtle.Screen()


# Set the background color of the turtle graphics window to red

screen.bgcolor("red")


# Call the draw_spiral function with the turtle object 'pepito' and 1000 line segments

draw_spiral(pepito, 1000, 5, 1, 0.1)


# Keep the window open

screen.mainloop()
