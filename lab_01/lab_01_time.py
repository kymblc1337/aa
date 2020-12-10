import lab_01 as test
from time import process_time
import random as rand
import matplotlib.pyplot as plt


def plot_grapgics(title, xlabel, ylabel, params):
    plt.title(title) # заголовок
    plt.xlabel(xlabel) # ось абсцисс
    plt.ylabel(ylabel) # ось ординат

    for graph in params:
        plt.plot(*graph[0], label=graph[1])

    plt.legend()
    plt.show()

def getRandomString(len):
    letterset = set("qwertyuiopasdfghjklzxcvbnm")
    return ''.join(rand.sample(letterset, len))

def timeTester(a, b, f):
    start = process_time()
    f(a, b)
    end = process_time()
    return end - start



###############################shortfuncnames
dlr = test.damerauLevenstein
lrnomatrix = test.levensteinRecoursion
lrmatrix = test.levensteinRecoursionMatrix
lmatrix = test.levensteinMatrix
############################################
lmatrix_method = [[[], []], "Алгоритм поиска расстояний \nЛевенштейна(М)"]
lrnomatrix_method = [[[], []], "Алгоритм поиска расстояний \nЛевенштейна(Р)"]
lrmatrix_method = [[[], []], "Алгоритм поиска расстояний \nЛевенштейна(МР)"]
dlr_method = [[[], []], "Алгоритм поиска расстояний \nДамерау-Левенштейна(М)"]



for i in range(3, 8):
    print(f"len is {i}")
    a = getRandomString(i)
    b = getRandomString(i)
    s = str(i) + ' & '
    lmatrix_method[0][0].append(i)
    lmatrix_method[0][1].append(timeTester(a, b, lmatrix))
    lrnomatrix_method[0][0].append(i)
    lrnomatrix_method[0][1].append(timeTester(a, b, lrnomatrix))
    lrmatrix_method[0][0].append(i)
    lrmatrix_method[0][1].append(timeTester(a, b, lrmatrix))
    dlr_method[0][0].append(i)
    dlr_method[0][1].append(timeTester(a, b, dlr))

plot_grapgics("", "Размер строки", "Время", [lmatrix_method, lrnomatrix_method, lrmatrix_method, dlr_method])