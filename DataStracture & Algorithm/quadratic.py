import math

a = int(input("Enter the first value : "))
b = int(input("Enter the second value : "))
c = int(input("Enter the third value : "))

# determination
D = b**2 - 4*a*c

if D < 0:
    print("Roots are imaginary!!!")
elif D == 0:
    x = -b/2*a
    print(f"x = {x}")
else:
    x1 = (-b + math.sqrt(D))/2*a
    x2 = (-b - math.sqrt(D))/2*a

    print(f"x1 = {x1} \nx2 = {x2}")
