a = int(input("Enter the first value:"))
b = int(input("Enter the second value:"))
c = int(input("Enter the third value:"))

if a > b and a > c:
    print(f"Larger Number is : {a}")
elif b > a and b > c:
    print(f"Larger Number is : {b}")
else:
    print(f"Larger Number is : {c}")
