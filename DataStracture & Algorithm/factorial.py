n = int(input("Enter the n value : "))

Fact = 1

if n == 1 or n == 0:
    print("Factorial is : 1")
elif n < 0:
    print("Negative number is not acceptable!")
else:
    for i in range(1, n+1):
        Fact = Fact*i
    print(Fact)
