def getStartMas(na: int, nb: int):
    mas = [[0 for _ in range(nb + 1)] for _ in range(na + 1)]
    for i in range(na):
        mas[i + 1][0] = mas[i][0] + 1

    for i in range(nb):
        mas[0][i + 1] = mas[0][i] + 1

    return mas

def levensteinRecoursion(stra: str, strb: str):
    if len(stra) == 0:
        return len(strb)
    if len(strb) == 0:
        return len(stra)
    payfine = 1 if stra[-1] != strb[-1] else 0

    return min(levensteinRecoursion(stra, strb[:-1]) + 1, levensteinRecoursion(stra[:-1], strb) + 1,
               levensteinRecoursion(stra[:-1], strb[:-1]) + payfine)


def levensteinMatrix(stra: str, strb: str):
    mas = getStartMas(len(stra), len(strb))

    for i in range(1, len(stra) + 1):
        for j in range(1, len(strb) + 1):
            payfine = 1 if stra[i - 1] != strb[j - 1] else 0

            mas[i][j] = min(mas[i - 1][j] + 1,
                            mas[i][j - 1] + 1,
                            mas[i - 1][j - 1] + payfine)
    return mas[len(stra)][len(strb)]


def levensteinRecoursionMatrix(stra: str, strb: str, mas=[]):
    if len(mas) == 0:
        mas = [[-1 for _ in range(len(strb))] for _ in range(len(stra))]
    if len(stra) == 0:
        return len(strb)
    if len(strb) == 0:
        return len(stra)
    payfine = 1 if stra[-1] != strb[-1] else 0

    if mas[len(stra) - 1][len(strb) - 1] == -1:
        mas[len(stra) - 1][len(strb) - 1] = min(levensteinRecoursionMatrix(stra, strb[:-1], mas) + 1,
                                                levensteinRecoursionMatrix(stra[:-1], strb, mas) + 1,
                                                levensteinRecoursionMatrix(stra[:-1], strb[:-1], mas) + payfine)
    return mas[len(stra) - 1][len(strb) - 1]

def damerauLevenstein(stra: str, strb: str):

    mas = getStartMas(len(stra), len(strb))

    for i in range(1, len(stra) + 1):
        for j in range(1, len(strb) + 1):
            payfine = 1 if stra[i - 1] != strb[j - 1] else 0
            mas[i][j] = min(mas[i - 1][j] + 1,
                            mas[i][j - 1] + 1,
                            mas[i - 1][j - 1] + payfine)
            if i >= 2 and j >= 2 and stra[i-1] == strb[j-2] and stra[i-2] == strb[j-1]:
                mas[i][j] = min(mas[i][j], mas[i - 2][j - 2] + 1)

    return mas[len(stra)][len(strb)]

