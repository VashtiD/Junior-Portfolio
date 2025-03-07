#Vashti Dalchand
#Period 1-2
#3-7-2025
#Python Coding Challenge #5

def check_fermat(a, b, c, n):
    if n > 2:
        if a**n + b**n == c**n:
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn’t work.")
    else:
        print("Please enter a value of n greater than 2.")

check_fermat(3, 4, 5, 3)
check_fermat(3, 4, 5, 2)
check_fermat(1, 2, 3, 3)
check_fermat(2, 2, 2, 3)
