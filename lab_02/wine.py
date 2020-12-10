from std import createZeroMatrix


def wineMultiply(mas1, mas2):
    col1, row1 = len(mas1[0]), len(mas1)
    col2, row2 = len(mas2[0]), len(mas2)

    result = createZeroMatrix(row1, col2)
    hBuf = [0 for _ in range(row1)]
    vBuf = [0 for _ in range(col2)]
    if col1 == row2:
        for i in range(row1):
            for j in range(col1 // 2):
                hBuf[i] += mas1[i][j * 2] * mas1[i][j * 2 + 1]
        for i in range(col2):
            for j in range(row2 // 2):
                vBuf[i] += mas2[j * 2][i] * mas2[j * 2 + 1][i]
        for i in range(row1):
            for j in range(col2):
                result[i][j] = -hBuf[i] - vBuf[j]
                for k in range(col1 // 2):
                    result[i][j] += (mas1[i][2 * k + 1] + mas2[2 * k][j]) * (mas1[i][2 * k] + mas2[2 * k + 1][j])
        if col1 % 2:
            for i in range(row1):
                for j in range(col2):
                    result[i][j] += mas1[i][col1 - 1] * mas2[col1 - 1][j]
    return result


def wineOptimizedMultiply(mas1, mas2):
    col1, row1 = len(mas1[0]), len(mas1)
    col2, row2 = len(mas2[0]), len(mas2)

    result = [[0 for _ in range(col2)] for j in range(row1)]
    hBuf = [0 for _ in range(row1)]
    vBuf = [0 for _ in range(col2)]
    a_2 = col1 // 2
    b_2 = row2 // 2

    if col1 == row2:
        for i in range(row1):
            for j in range(a_2):
                hBuf[i] += mas1[i][j * 2] * mas1[i][(j * 2) + 1]

        for i in range(col2):
            for j in range(b_2):
                vBuf[i] += mas2[j * 2][i] * mas2[(j * 2) + 1][i]

        for i in range(row1):
            for j in range(col2):
                tmp = -hBuf[i] - vBuf[j]
                for k in range(a_2):
                    tmp += (mas1[i][(k * 2) + 1] + mas2[k * 2][j]) * (mas1[i][k * 2] + mas2[(k * 2) + 1][j])
                result[i][j] = tmp

        if col1 % 2:
            for i in range(row1):
                for j in range(col2):
                    result[i][j] += mas1[i][col1 - 1] * mas2[col1 - 1][j]

    return result



