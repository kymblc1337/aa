from stopwatch import stopwatch
import sort_implementations
import graphics


def test_wrapper(size, sort_type):
    print('-' * 50)
    mas = sort_implementations.generate_random_massive(1000, sort_type)
    bubble_time = stopwatch(sort_implementations.bubble_sort, [mas])
    insert_time = stopwatch(sort_implementations.insertion_sort, [mas])
    quck_time = stopwatch(sort_implementations.quick_sort, [mas])
    print(f'size: {size}, type of raw array: {sort_type}')
    print(f'bubble sort time: {bubble_time}')
    print(f'insert sort time: {insert_time}')
    print(f'quick sort time : {quck_time}')

def black_box(func, size):
    print(f"Testing {func.__name__}:")
    mas = sort_implementations.generate_random_massive(size, sort_implementations.Sort.random)
    print(f"before sort: {mas}")
    res = sort_implementations.quick_sort(mas)
    print(f"after sort : {res}")

def all_sort(mas):
    bubble = sort_implementations.quick_sort(mas)
    insert = sort_implementations.quick_sort(mas)
    quick = sort_implementations.quick_sort(mas)
    mas.sort()
    print(f"expect: {mas}")
    print(f"bubble: {bubble}")
    print(f"insert: {insert}")
    print(f"quick : {quick}")

def show_graphic(start_size, end_size, sort_type):
    quick = [[], []]
    insert = [[], []]
    bubble = [[], []]
    for size in range(start_size, end_size, (end_size - start_size) // 15 + 1):
        array = sort_implementations.generate_random_massive(size, sort_type)
        array = [array]
        tmp = stopwatch(sort_implementations.quick_sort, array)
        quick[0].append(size)
        quick[1].append(tmp)

        tmp = stopwatch(sort_implementations.insertion_sort, array)
        insert[0].append(size)
        insert[1].append(tmp)

        tmp = stopwatch(sort_implementations.bubble_sort, array)
        bubble[0].append(size)
        bubble[1].append(tmp)
    graphics.plot_grapgics("Сравнение времени сортировок", "Время", "Размер массива", quick, insert, bubble)





#test_wrapper(100, sort_implementations.Sort.random)

#print(sort_implementations.insertion_sort([3, 5, 1, 2, 4]))
#test_wrapper(100, sort_implementations.Sort.reversed)
#mas = sort_implementations.generate_random_massive(10, sort_implementations.Sort.random)
#mas = sort_implementations.quick_sort(mas)
#print(mas)

#black_box(sort_implementations.bubble_sort, 10)

#all_sort(sort_implementations.generate_random_massive(15, sort_implementations.Sort.random, 0, 0))
#show_graphic(100, 1000, sort_implementations.Sort.reversed)

mas = sort_implementations.generate_random_massive(10, sort_implementations.Sort.reversed)
print(mas)
arr = sort_implementations.quick_sort(mas)
print(arr)