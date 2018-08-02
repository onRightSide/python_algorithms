import sys


from random import random


def add_all_to_dict(dict_, *args):
    for each in args:
        if dict_.get(each.__class__) is None:
            dict_.update({each.__class__ : sys.getsizeof(each)})
        else:
            dict_.update({each.__class__: dict_.get(each.__class__) + sys.getsizeof(each)})
    return dict_


def add_variables_to_dict(dict_, **kwargs):
    for key, value in kwargs.items():
        dict_.update({key: (value.__class__, sys.getsizeof(value))})
    return dict_


def all_memory_show(variables_dict):

    print(variables_dict)

    memory_sum = 0
    max_size_type = None
    max_size_memory = 0

    for each in variables_dict:
        memory_sum += variables_dict.get(each)
        if variables_dict.get(each) > max_size_memory:
            max_size_memory = variables_dict.get(each)
            max_size_type = each
    return f'\tНаибольшие затраты памяти одного типа(класса): {max_size_type} -> {max_size_memory}\n'\
           f'\tВсего затрачено памяти: {memory_sum}\n'


def variables_memory_show(variables_dict):

    print(variables_dict)

    memory_sum = 0
    max_size_type = None
    max_size_memory = 0
    max_size_variable = None

    for each in variables_dict:
        memory_sum += variables_dict.get(each)[1]
        if variables_dict.get(each)[1] > max_size_memory:
            max_size_memory = variables_dict.get(each)[1]
            max_size_type = variables_dict.get(each)[0]
            max_size_variable = each
    return f'\tНаибольшие затраты памяти одной переменной: {max_size_variable} -> {max_size_type} -> {max_size_memory}\n' \
           f'\tВсего затрачено памяти: {memory_sum}\n'


# Функция теста №1: Урок 3. Задача 7. В одномерном массиве целых чисел определить два наименьших элемента.
def two_min(n):

    num_list = []
    for i in range(n):
        num_list.append(int(random() * 100))

    min_num = num_list[0]
    min_num_2 = num_list[1]

    if min_num_2 < min_num:
        min_num, min_num_2 = min_num_2, min_num

    for i in range(2, n):
        if num_list[i] < min_num_2:
            if num_list[i] < min_num:
                min_num_2 = min_num
                min_num = num_list[i]
            else:
                min_num_2 = num_list[i]

    var_dict = {}
    var_dict = add_variables_to_dict(var_dict, **{"n": n, "min_num": min_num, "min_num_2":  min_num_2, "i": i})

#    return min_num, min_num_2

    return var_dict


def two_min_float(n):

    num_list = []
    for i in range(n):
        num_list.append(float(random() * 100))

    min_num = num_list[0]
    min_num_2 = num_list[1]

    if min_num_2 < min_num:
        min_num, min_num_2 = min_num_2, min_num

    for i in range(2, n):
        if num_list[i] < min_num_2:
            if num_list[i] < min_num:
                min_num_2 = min_num
                min_num = num_list[i]
            else:
                min_num_2 = num_list[i]

    var_dict = {}
    var_dict = add_variables_to_dict(var_dict, **{"n": n, "min_num": min_num, "min_num_2":  min_num_2, "i": i})

#    return min_num, min_num_2

    return var_dict


# Функция теста №2: Урок 2. Задача 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером
# 32 и заканчивая 127-м включительно.
def print_symbols():
    start = 32
    stop = 128
    counter = 0
    for i in range(start, stop):
#         print(f"{i:3}: {chr(i):3}", end=" ")
        counter += 1
        if counter == 10:
            counter = 0
#             print()

    var_dict = {}
    var_dict = add_variables_to_dict(var_dict, **{"start": start, "stop": stop, "counter": counter, "i": i})

    return var_dict


# Функция теста №3: Урок 3. Задача 2. Во втором массиве сохранить индексы четных элементов первого массива.
def find_index_of_even(n):

    num_arr = []
    for each in range(n):
        num_arr.append(int(random() * 100))
#         print("%3d" % num_arr[i], end='')
#     print()

    index_arr = []
    index = 0

    for each in num_arr:
        if each % 2 == 0:
            index_arr.append(index)
        index += 1

#     print(index_arr)

    var_dict = {}
    var_dict = add_variables_to_dict(var_dict, **{"n": n, "index": index, "each": each})

    return var_dict


# Функции теста №4 : Урок 4. Задача 4. Определить, какое число в массиве встречается чаще всего.
def max_count_num(n):

    num_list = [ ]

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

    var_dict = {}
    var_dict = add_all_to_dict(var_dict, *[n, count, max_count, each, index, max_num, num_list])

#     if max_count > 1:
#         return max_num, max_count
#     else:
#         return "Все элементы уникальны"

    return var_dict


def max_count_num_set(n):
    num_list = []
    for i in range(n):
        num_list.append(int(random() * 100))

    max_count = 0
    max_num = num_list[0]

    num_set = set(num_list)

    for each in num_set:
        count_ = num_list.count(each)
        if count_ > max_count:
            max_count = count_
            max_num = each
        count_ = 0

    var_dict = {}
    var_dict = add_all_to_dict(var_dict, *[n, max_count, max_num, each, num_list, num_set])

    #     if max_count > 1:
    #         return max_num, max_count
    #     else:
    #         return "Все элементы уникальны"

    return var_dict


def max_count_num_frozenset(n):
    num_list = []
    for i in range(n):
        num_list.append(int(random() * 100))

    max_count = 0
    max_num = num_list[0]

    num_set = frozenset(num_list)

    for each in num_set:
        count_ = num_list.count(each)
        if count_ > max_count:
            max_count = count_
            max_num = each
        count_ = 0

    var_dict = {}
    var_dict = add_all_to_dict(var_dict, *[n, max_count, max_num, each, num_list, num_set])

    #     if max_count > 1:
    #         return max_num, max_count
    #     else:
    #         return "Все элементы уникальны"

    return var_dict


# Тест №1
print(f'Разрядность ОС: {sys.platform}\n'
      f'Версия Python: 3.7.0\n')

print(variables_memory_show(two_min(10)))
print(variables_memory_show(two_min(100)))
print(variables_memory_show(two_min(1000)))
print(variables_memory_show(two_min(10000)))

print(variables_memory_show(two_min_float(10)))
print(variables_memory_show(two_min_float(100)))
print(variables_memory_show(two_min_float(1000)))
print(variables_memory_show(two_min_float(10000)))

print("####################################################################################\n")
# При изменении типа данных элементов списка, в котором идет поиск, потребление памяти увеличивается.
#

# Тест №2
print(f'Разрядность ОС: {sys.platform}\n'
      f'Версия Python: 3.7.0\n')

print(variables_memory_show(print_symbols()))

print("####################################################################################\n")
# Стабильный расход памяти, т.к не подразумевается использование других типов данных и изменение параметров цикла вывода
# символов.

# Тест №3
print(f'Разрядность ОС: {sys.platform}\n'
      f'Версия Python: 3.7.0\n')

print(variables_memory_show(find_index_of_even(10)))
print(variables_memory_show(find_index_of_even(100)))
print(variables_memory_show(find_index_of_even(1000)))
print(variables_memory_show(find_index_of_even(10000)))

print("####################################################################################\n")
# При изменении типа данных элементов списка, в котором идет поиск, потребление памяти увеличивается.
# Наиболее стабильной и эффективной является программа №2.

# Тест №4
print(all_memory_show(max_count_num(10)))
print(all_memory_show(max_count_num(100)))
print(all_memory_show(max_count_num(1000)))
print(all_memory_show(max_count_num(10000)))

print(all_memory_show(max_count_num_set(10)))
print(all_memory_show(max_count_num_set(100)))
print(all_memory_show(max_count_num_set(1000)))
print(all_memory_show(max_count_num_set(10000)))

print(all_memory_show(max_count_num_frozenset(10)))
print(all_memory_show(max_count_num_frozenset(100)))
print(all_memory_show(max_count_num_frozenset(1000)))
print(all_memory_show(max_count_num_frozenset(10000)))

print("####################################################################################\n")
# При относительно небольшой в процентном соотношении потере памяти из-за использования frozenset получаем
# значительное ускорение работы программы - необходимо искать баланс между скоростью и памятью.
# При смене типа данных элементов списка с int на float многократно растет потреблениие памяти set и frozenset.
#
