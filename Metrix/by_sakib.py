def input_matrix(m, n):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            num = int(input("Enter element (%d %d):" % (i + 1, j + 1)))
            row.append(num)
        matrix.append(row)
    display_matrix(matrix)
    return matrix


def display_matrix(m):
    for n in m:
        print(n)


def matrix_multiplication(a, b):
    # a,b = matrix, m = a row , p = a and b - col - row, n = b col
    # a =[[1, 5],[3, 6]]
    # b = [[3, 1, -2],[4, 0, 7]]
    result = []
    row = [[0 for i in range(len(b[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[i])):
            for k in range(len(b)):
                row[i][j] += a[i][k] * b[k][j]
    result.append(row)
    display_matrix(result)


matrix_multiplication(input_matrix(2, 2), input_matrix(2, 3))
