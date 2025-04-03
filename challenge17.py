#Vashti Dalchand
#April 3, 2025
#period 1-2
#Python Coding Challenges 17

def is_power(a, b):
    #if a is smaller than b, it cannot be a power of b
    if a < b:
        return False
    #if a equals b, it is b raised to the power of 1
    if a == b:
        return True
    #Recursive case: check if a is divisible by b
    if a % b == 0:
        return is_power(a // b, b)
    #If a is not divisible by b, return False
    return False


print(is_power(27, 3))  # True, because 27 = 3^3
print(is_power(16, 2))  # True, because 16 = 2^4
print(is_power(25, 5))  # True, because 25 = 5^2
print(is_power(30, 3))  # False, because 30 is not a power of 3
