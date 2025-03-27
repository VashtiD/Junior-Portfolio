import turtle

def draw_circle(t, color, size, x, y):
    t.penup()
    t.color(color)
    t.fillcolor(color)
    t.goto(x, y)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    t.pendown()

def draw_flower(t, petal_color, center_color, num_petals, petal_size, center_size):
    # Draw center of the flower
    draw_circle(t, center_color, center_size, 0, 0)

    # Draw petals
    for _ in range(num_petals):
        draw_circle(t, petal_color, petal_size, 0, center_size + petal_size)
        t.right(360 / num_petals)  # Rotate for the next petal

# Set up turtle
tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(500)

# Draw a flower with specified colors and sizes
draw_flower(tommy, "red", "yellow", 6, 50, 30)

# Hide the turtle and complete the drawing
tommy.hideturtle()
turtle.done()
