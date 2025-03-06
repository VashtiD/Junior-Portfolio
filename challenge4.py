#Vashti Dalchand
#Period 1-2
#3-6-2025
#Python Coding Challenge #4

def print_beam():
    print("+----", end=" ")

def print_post():
    print("|    ", end="")

def do_twice(f):
    f()
    f()

def print_beams():
    do_twice(print_beam)
    print("+")  # Closing the beam line

def print_posts():
    do_twice(print_post)
    print("|")  # Closing the post line

def do_four(f):
    do_twice(f)
    do_twice(f)

def row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(row)
    print_beams()

print_grid()
print(" ")

def print_grid_twice():
    do_four(row)
    print_beams()

print_grid_twice()
