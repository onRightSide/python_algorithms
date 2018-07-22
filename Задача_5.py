# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


from random import random


N = 2700
num_arr = []
for i in range(N):
    num_arr.append(int(random() * 100) - 50)
    print("%3d" % num_arr[i], end='')
print()

min_num = 0
min_num_index = 0
num_set = set(num_arr)

for each in num_set:
    if each < 0:
        min_num = each
        min_num_index = num_arr.index(each)
        break

if min_num < 0:
    for each in num_set:
        if each < 0 and (each > min_num):
            min_num = each
            min_num_index = num_arr.index(min_num)
    print(min_num, min_num_index)
else:
    print("Отсутсвуют отрицательные элементы")




