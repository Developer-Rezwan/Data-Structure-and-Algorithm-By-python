def search(array, item):
    i = 0
    n = len(array)
    while i <= n:
        if i == n:
            return "Not Found"

        if array[i] == item:
            return f"Location : {i}"

        i = i+1


myArr = [12, 232, 43245, 34, 3, 43, 45, 3, 45, 3, 543, 53, 4, 53, 45, 34, 53, 53, 5, 3, 453, 45, 3, 5, 345, 3, 5, 3,
         453, 4, 530]

result = search(myArr, 530)
print(result)

