from random import randint
from enum import Enum
from copy import deepcopy


class Sort(Enum):
    sorted = "sorted"
    reversed = "reversed"
    random = "random"


def generate_random_massive(size: int, sort: Sort) -> list:
    massive = []
    if sort == Sort.sorted:
        for i in range(size):
            massive.append(i + 1)
    elif sort == Sort.reversed:
        for i in range(size, 0, -1):
            massive.append(i)
    else:
        for i in range(size):
            massive.append(randint(1, size))

    return massive

# def generate_random_massive(size: int, sort: Sort, start = 1, ) -> list:
#     massive = []
#     if sort == Sort.sorted:
#         for i in range(size):
#             massive.append(i + 1)
#     elif sort == Sort.reversed:
#         for i in range(size, 0, -1):
#             massive.append(i)
#     else:
#         for i in range(size):
#             massive.append(randint(start, end))
#
#     return massive

def bubble_sort(massive):
    array = deepcopy(massive)

    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def insertion_sort(massive):
    array = deepcopy(massive)

    for i in range(1, len(array)):
        insert = array[i]
        j = i - 1
        while j >= 0 and array[j] > insert:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = insert

    return array


def python_sort(massive):
    array = deepcopy(massive)

    array = array.sorted()

    return array


def quick_sort_impl(array):
    if len(array) < 2:
        return array
    q = array[len(array) // 2]
    left, middle, right = [], [], []
    for i in array:
        if i < q:
            left.append(i)
        elif i > q:
            right.append(i)
        else:
            middle.append(i)

    return quick_sort_impl(left) + middle + quick_sort_impl(right)


def quick_sort(massive):
    array = deepcopy(massive)
    return quick_sort_impl(array)
