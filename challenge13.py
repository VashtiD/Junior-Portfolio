import turtle
import math

def draw_isosceles_triangle(t, length, angle):
    t.begin_fill()
    t.forward(length)
    t.left(180 - angle)
    t.forward(length)
    t.left(180 - angle)
    t.forward(length)
    t.end_fill()

def draw_pie_chart(t, radius, slices, angle):
    for _ in range(slices):
        t.fillcolor("blue")
        draw_isosceles_triangle(t, radius, angle)
        t.right(360 / slices)

def main():
    turtle.speed(0)
    turtle.penup()
    
    sizes = [50, 75, 100, 125]
    for size in sizes:
        turtle.goto(0, -size) 
        turtle.pendown()
        draw_pie_chart(turtle, size, 12, 60)
        turtle.penup()
        turtle.setheading(0)
        turtle.goto(0, 0)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
