numbers = input("Enter numbers separated by comma : ")

numbers = numbers.split(',')

summation = 0

for number in numbers:
    summation = summation + float(number)
print(summation)