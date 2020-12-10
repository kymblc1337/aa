import erokhawatch
import std
import wine
import random
import datetime

COMPAREFUNC = erokhawatch.stopwatch

def checkMult(a, b, expect):
    print(f"{a} * {b}")
    print(f"Ожидаемый результат                      : {expect}")
    print(f"Стандартный алгоритм умножения матриц    : {std.stdMultiply(a, b)}")
    print(f"Правильно: {std.stdMultiply(a, b) == expect}\n")
    print(f"Алгоритм Винограда умножения матриц      : {wine.wineMultiply(a, b)}")
    print(f"Правильно: {wine.wineMultiply(a, b) == expect}\n")
    print(f"Алгоритм Винограда умножения матриц(опт) : {wine.wineOptimizedMultiply(a, b)}")
    print(f"Правильно: {wine.wineOptimizedMultiply(a, b) == expect}\n")

def checkMultEqu(a, b):
    return (std.stdMultiply(a, b) != wine.wineMultiply(a, b)) or (std.stdMultiply(a, b) != wine.wineOptimizedMultiply(a, b))


def manyTests(numOfTests):
    mas = 0
    for i in range(numOfTests):
        size = random.randint(5, 10)
        a = std.createRandomMatrix(size, size)
        b = std.createRandomMatrix(size, size)
        mas += checkMultEqu(a, b)
    print(f"Tests passed: {numOfTests - mas}/{numOfTests}")


def compareTime(mas1, mas2):
    stdTime = COMPAREFUNC(std.stdMultiply, [mas1, mas2])
    wineTime = COMPAREFUNC(wine.wineMultiply, [mas1, mas2])
    wineOptimizedTime = COMPAREFUNC(wine.wineOptimizedMultiply, [mas1, mas2])
    print(f"Wine optimized time: {wineOptimizedTime}")
    print(f"Wine           time: {wineTime}")
    print(f"Std            time: {stdTime}")


def compareTimeByRandomMatrixWithSize(size):
    mas1 = std.createRandomMatrix(size, size)
    mas2 = std.createRandomMatrix(size, size)
    compareTime(mas1, mas2)

def writeTimeToFile(filename, pfrom, pto, pstep):
    f = open(filename, 'w')
    std_result = {'label': 'std', 'x_array': [], 'y_array': []}
    wine_result = {'label': 'wine', 'x_array': [], 'y_array': []}
    optimized_wine_result = {'label': 'wine_optimized', 'x_array': [], 'y_array': []}
    for size in range(pfrom, pto, pstep):
        mas1 = std.createRandomMatrix(size, size)
        mas2 = std.createRandomMatrix(size, size)
        std_result['x_array'].append(size)
        std_result['y_array'].append(COMPAREFUNC(std.stdMultiply, [mas1, mas2]))

        wine_result['x_array'].append(size)
        wine_result['y_array'].append(COMPAREFUNC(wine.wineMultiply, [mas1, mas2]))
        optimized_wine_result['x_array'].append(size)
        optimized_wine_result['y_array'].append(COMPAREFUNC(wine.wineOptimizedMultiply, [mas1, mas2]))
        print(f"{datetime.datetime.now().time()} - passed size {size}")

    # writing std info
    f.write(f"{std_result['label']}\n")
    f.write(f"{std_result['x_array']}\n")
    f.write(f"{std_result['y_array']}\n")

    # writing wino info
    f.write(f"{wine_result['label']}\n")
    f.write(f"{wine_result['x_array']}\n")
    f.write(f"{wine_result['y_array']}\n")

    # writing optimized wine info
    f.write(f"{optimized_wine_result['label']}\n")
    f.write(f"{optimized_wine_result['x_array']}\n")
    f.write(f"{optimized_wine_result['y_array']}\n")

    f.close()


def fileWriteLatex(filename, pfrom, pto, pstep):
    f = open(filename, 'w')
    for size in range(pfrom, pto, pstep):
        '''Размер матрицы & std & vin & optVin'''
        mas1 = std.createRandomMatrix(size, size)
        mas2 = std.createRandomMatrix(size, size)
        stdtime = round(COMPAREFUNC(std.stdMultiply, [mas1, mas2]), 3)
        wineTime = round(COMPAREFUNC(wine.wineMultiply, [mas1, mas2]), 3)
        wineOptTime = round(COMPAREFUNC(wine.wineOptimizedMultiply, [mas1, mas2]), 3)
        str = f"{size} & {stdtime} & {wineTime} & {wineOptTime} \\\\"
        str += "\n"
        str += "\hline\n"
        f.write(str)
        print(f"{datetime.datetime.now().time()} - passed size {size}")

    f.close()
