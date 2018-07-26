# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.


import math


import cProfile


def prime_eratosfen(n):

    list_range = 11
    n -= 1

    while True:

        top_border = 100 * (n // list_range + 1)
        num_list = [num for num in range(2, top_border + 1)]

        index = 0

        while index < math.sqrt(top_border):

            if index == n:
                return num_list[n]

            step = num_list[index]
            p = step
            mult = 2

            while p * mult < top_border:

                step = p * mult
                try:
                    num_list.remove(step)
                    mult += 1
                except ValueError:
                    mult += 1
            index += 1
        try:
            if num_list[n]:
                return num_list[n]
        except IndexError:
            list_range -= 1


# 100 loops, best of 5: 133 usec per loop  (10 номер)
# 100 loops, best of 5: 8.11 msec per loop (100 номер)
# 100 loops, best of 5: 615 msec per loop  (1000 номер)

# cProfile.run("prime_eratosfen(1000)"):  19056 function calls in 0.561 seconds


def prime_eratosfen_modified(n):

    list_range = 11

    while True:

        top_border = 100 * (n // list_range + 1)
        num_list = [num for num in range(top_border + 1)]
        prime_list = []

        for i in range(2, top_border - 1):
            if num_list[i] != -1:
                prime_list.append(num_list[i])
                for j in range(i, top_border + 1 - i, i):
                    num_list[j] = -1

        return prime_list[n - 1]


# 100 loops, best of 5: 32.5 usec per loop (10 номер)
# 100 loops, best of 5: 347 usec per loop  (100 номер)
# 100 loops, best of 5: 3.33 msec per loop (1000 номер)


# cProfile.run("prime_eratosfen_modified(1000)"): 1140 function calls in 0.004 seconds


def prime(n):
    list_range = 11
    while True:
        top_border = 100 * (n // list_range + 1)
        prime_list = []

        index = 0

        for num in range(2, top_border):
            for div in prime_list:
                if num % div == 0:
                    break
            else:
                index += 1
                prime_list.append(num)
                if index == n:
                    return num


# 100 loops, best of 5: 9.37 usec per loop (10 номер)
# 100 loops, best of 5: 434 usec per loop  (100 номер)
# 100 loops, best of 5: 41.8 msec per loop (1000 номер)

# cProfile.run("prime(1000)"): 1004 function calls in 0.042 seconds

