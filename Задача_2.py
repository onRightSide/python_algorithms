# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
# со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 0, 3, 4, 5
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

from random import random


N = 27
# num_arr = [1, 2, 2, 3, 3, 4, 4]
num_arr = []
for i in range(N):
    num_arr.append(int(random() * 100))
    print("%3d" % num_arr[i], end='')
print()

index_arr = []
index = 0

for each in num_arr:
    if each % 2 == 0:
        index_arr.append(index)
    index += 1

print(index_arr)

