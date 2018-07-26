# Урок 4. Задача 4. Определить, какое число в массиве встречается чаще всего.


from random import random


import cProfile


import timeit


def max_count_num(n):

    num_list = []
    for i in range(n):
        num_list.append(int(random() * 100))

    count = 1
    max_count = 0
    max_num = num_list[0]

    for each in range(n - 1):
        for index in range(each + 1, n):
            if num_list[each] == num_list[index]:
                count += 1
        if count > max_count:
            max_count = count
            max_num = num_list[each]
        count = 1

    if max_count > 1:
        return max_num, max_count
    else:
        return "Все элементы уникальны"


# 100 loops, best of 5: 14.7 usec per loop (10 элементов)
# 100 loops, best of 5: 708 usec per loop  (100 элементов)
# 100 loops, best of 5: 75.9 msec per loop (1000 элементов)

# cProfile.run("max_count_num(10000)")  # : 20004 function calls in 7.943 seconds
#                                       #   1    0.000    0.000    8.104    8.104 {built-in method builtins.exec}

def max_count_num_set(n):  # Создаем множество из элементов списка
    num_list = []
    for i in range(n):
        num_list.append(int(random() * 100))

    count_ = 0
    max_count = 0
    max_num = num_list[0]

    num_set = set(num_list)

    for each in num_set:
        count_ = num_list.count(each)
        if count_ > max_count:
            max_count = count_
            max_num = each
        count_ = 0

    if max_count > 1:
        return max_num, max_count
    else:
        return "Все элементы уникальны"


# 100 loops, best of 5: 8.64 usec per loop (10 элементов)
# 100 loops, best of 5: 179 usec per loop  (100 элементов)
# 100 loops, best of 5: 2.47 msec per loop (1000 элементов)


# cProfile.run("max_count_num_set(10000)")  # : 20104 function calls in 0.030 seconds
#                                           #   1    0.000    0.000    0.028    0.028 {built-in method builtins.exec}

#############################################################################################


# Урок 4. Задача 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.


def max_of_min_matrix(ROW_N, COL_N):

    matrix = []

    for col in range(COL_N):
        matrix.append([])
        for row in range(ROW_N):
            matrix[col].append(int(random() * 100))

    min_arr = []

    for col in matrix:
        min_num = col[0]
        for index in col:
            if min_num > index:
                min_num = index
        min_arr.append(min_num)

    max_min_num = min_arr[0]

    for each in min_arr:
        if each > max_min_num:
            max_min_num = each

    return max_min_num


# 100 loops, best of 5: 51.6 usec per loop (10 x 10)
# 100 loops, best of 5: 4.29 msec per loop (100 X 100)
# 100 loops, best of 5: 459 msec per loop  (1000 x 1000)

# cProfile.run("max_of_min_matrix(100, 100)") # : 20204 function calls in 0.008 seconds

def max_of_min_matrix_python_style(ROW_N, COL_N):

    matrix = []
    min_arr = []

    for col in range(COL_N):
        matrix.append([])
        for row in range(ROW_N):
            matrix[col].append(int(random() * 100))

    for col in matrix:
        min_arr.append(min(col))

    return max(min_arr)


# 100 loops, best of 5: 53.2 usec per loop (10 x 10)
# 100 loops, best of 5: 4.34 msec per loop (100 x 100)
# 100 loops, best of 5: 456 msec per loop  (1000 x 1000)

# cProfile.run("max_of_min_matrix_python_style(100, 100)") # : 20305 function calls in 0.007 seconds


##############################################################################################


# Урок 4. Задача 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


def sum_between(N):

    num_arr = []
    for i in range(N):
        num_arr.append(int(random() * 100))

    max_num = num_arr[0]
    max_index = 0
    min_num = num_arr[0]
    min_index = 0
    sum_ = 0

    for index in range(N):
        if num_arr[index] > max_num:
            max_num = num_arr[index]
            max_index = index
        elif num_arr[index] < min_num:
            min_num = num_arr[index]
            min_index = index

    if min_index > max_index:
        max_index, min_index = min_index, max_index

    for index in range(min_index + 1, max_index):
        sum_ += num_arr[index]

    return sum_


# 100 loops, best of 5: 6.96 usec per loop (10 элементов)
# 100 loops, best of 5: 53.5 usec per loop (100 элементов)
# 100 loops, best of 5: 541 usec per loop  (1000 элементов)
# 100 loops, best of 5: 5.47 msec per loop (10000 элементов)

# cProfile.run("sum_between(10000)") # : 20004 function calls in 0.009 seconds


def sum_between_python_style(N):

    num_arr = []
    for i in range(N):
        num_arr.append(int(random() * 100))

    sum_ = 0

    max_num = max(num_arr)
    min_num = min(num_arr)

    max_index = num_arr.index(max_num)
    min_index = num_arr.index(min_num)

    if min_index > max_index:
        max_index, min_index = min_index, max_index

    for index in range(min_index + 1, max_index):
        sum_ += num_arr[index]

    return sum_


# 100 loops, best of 5: 6.67 usec per loop (10 элементов)
# 100 loops, best of 5: 45.7 usec per loop (100 элементов)
# 100 loops, best of 5: 440 usec per loop  (1000 элементов)
# 100 loops, best of 5: 4.3 msec per loop  (10000 элементов)


# cProfile.run("sum_between_piython_style(10000)") # : 20008 function calls in 0.007 seconds

