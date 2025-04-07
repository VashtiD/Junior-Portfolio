def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print("GCD of 48 and 18:", gcd(48, 18))
print("GCD of 56 and 98:", gcd(56, 98))
print("GCD of 101 and 10:", gcd(101, 10))
print("GCD of 42 and 56:", gcd(42, 56))
print("GCD of 17 and 13:", gcd(17, 13))
