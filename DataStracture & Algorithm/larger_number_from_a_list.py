numbers = input('Input numbers and separated by comma :')

numbers = numbers.split(',')

larger = 0

for number in numbers:
    if larger < int(number):
        larger = int(number)

print(f"The larger number is: {larger}")
