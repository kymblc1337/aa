from random import randint
def createZeroMatrix(n1, n2):
    mas = [[0 for _ in range(n2)] for _ in range(n1)]
    return mas

def createRandomMatrix(n1, n2):
    mas = [[randint(1, 100) for _ in range(n1)] for _ in range(n2)]
    return mas


def stdMultiply(mas1, mas2):
    col1, row1 = len(mas1[0]), len(mas1)
    col2, row2 = len(mas2[0]), len(mas2)

    if col1 == row2:
        tmp = createZeroMatrix(col1, row2)
        for i in range(row1):
            for j in range(col2):
                for k in range(col1):
                    tmp[i][j] += int(mas1[i][k] * mas2[k][j])
        return tmp
    else:
        return 'error'
