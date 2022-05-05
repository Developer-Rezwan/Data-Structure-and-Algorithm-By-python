import math

startNumber = 1
endNumber = 100


def is_prime(number):
    for num in range(2, int(math.sqrt(number)) + 1):
        if (number % num) == 0:
            return False
    return True


for i in range(startNumber, endNumber+1):
    if is_prime(i):
        print(i)
