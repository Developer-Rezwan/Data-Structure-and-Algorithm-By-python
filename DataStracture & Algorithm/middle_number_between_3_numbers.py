a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if b > a > c or c > a > b:
    print(a)
elif a > b > c or c > b > a:
    print(b)
else:
    print(c)
