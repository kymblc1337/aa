import matplotlib.pyplot as plt


def plot_grapgics(title, xlabel, ylabel, quick, insert, bubble):
    plt.title(title) # заголовок
    plt.xlabel(xlabel) # ось абсцисс
    plt.ylabel(ylabel) # ось ординат

    plt.plot(*quick, label="quick sort")
    plt.plot(*insert, label="insert sort")
    plt.plot(*bubble, label="bubble sort")
    plt.legend()
    plt.show()

