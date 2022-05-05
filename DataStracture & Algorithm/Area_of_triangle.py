import math

a = float(input("Triangle first side :"))
b = float(input("Triangle second side :"))
c = float(input("Triangle third side :"))

if a+b > c and b+c > a and c+a > b:
    s = (a+b+c)/2
    Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"{Area} square-unit")
else:
    print("This is not a triangle!")
