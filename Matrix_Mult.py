# Quick implementation of Strassen's matrix multiplication algorithm
# Input: n x n integer matrices x and y
# Output: z = x times y
# Assumption: n is a power of 2
def std_mult(a, b):
    result = [[a[0][0] * b[0][0] + a[0][1] * b[0][1], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
              [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]
    return result


def matrix_addition(a, b):
    return [[a[row][col] + b[row][col]
             for col in range(len(a[row]))] for row in range(len(a))]


def matrix_subtraction(a, b):
    return [[a[row][col] - b[row][col]
             for col in range(len(a[row]))] for row in range(len(a))]


def split_matrix(a):
    n = len(a)
    m = n // 2
    upper_left = [[a[i][j] for j in range(m)] for i in range(m)]
    upper_right = [[a[i][j] for j in range(m, n)] for i in range(m)]
    lower_left = [[a[i][j] for j in range(m)] for i in range(m, n)]
    lower_right = [[a[i][j] for j in range(m, n)] for i in range(m, n)]
    return upper_left, upper_right, lower_left, lower_right


def strassen(x, y):
    result = []
    if len(x) == 2:
        return std_mult(x, y)

    a, b, c, d = split_matrix(x)
    e, f, g, h = split_matrix(y)

    p1 = strassen(a, matrix_subtraction(f, h))
    p2 = strassen(matrix_addition(a, b), h)
    p3 = strassen(matrix_addition(c, d), e)
    p4 = strassen(d, matrix_subtraction(g, e))
    p5 = strassen(matrix_addition(a, d), matrix_addition(e, h))
    p6 = strassen(matrix_subtraction(b, d), matrix_addition(g, h))
    p7 = strassen(matrix_subtraction(a, c), matrix_addition(e, f))

    upper_left = matrix_addition(matrix_subtraction(matrix_addition(p5, p4), p2), p6)
    upper_right = matrix_addition(p1, p2)
    lower_left = matrix_addition(p3, p4)
    lower_right = matrix_subtraction(matrix_subtraction(matrix_addition(p1, p5), p3), p7)

    for i in range(len(upper_right)):
        result.append(upper_left[i] + upper_right[i])
    for i in range(len(lower_right)):
        result.append(lower_left[i] + lower_right[i])

    return result


matrix_a = [[1, 2, 3, 4], [3, 4, 5, 6], [1, 2, 3, 4], [5, 6, 7, 8]]
matrix_b = [[5, 6, 7, 8], [7, 8, 9, 10], [1, 2, 3, 4], [3, 4, 5, 6]]

test = matrix_addition(matrix_a, matrix_b)
test2 = matrix_subtraction(matrix_b, matrix_a)
test3 = split_matrix(matrix_a)
test4 = strassen(matrix_a, matrix_b)
print(test)
print(test2)
print(test3)
print(test4)
