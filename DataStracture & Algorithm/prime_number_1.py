startFrom = 1
endTo = 10

for number in range(startFrom, endTo+1):

    if number > 1:
        for num in range(2, number):
            if (number % num) == 0:
                break
        else:
            print(number)
