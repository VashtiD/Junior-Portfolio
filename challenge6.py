def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Yes")
    else:
        print("No")

def input_lengths():
    try:
        a = int(input("Enter the length of the first stick: "))
        b = int(input("Enter the length of the second stick: "))
        c = int(input("Enter the length of the third stick: "))
        is_triangle(a, b, c)  # Call is_triangle with the lengths
    except ValueError:
        print("Please enter valid integer lengths.")

input_lengths()
