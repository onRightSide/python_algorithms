# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.


from random import random


N = 100
# num_arr = [1, 2, 2, 3, 3, 4, 4]
num_arr = []
for i in range(N):
    num_arr.append(int(random() * 100))
    print("%3d" % num_arr[i], end='')
print()

min_num = num_arr[0]
min_num_2 = num_arr[1]

if min_num_2 < min_num:
    min_num, min_num_2 = min_num_2, min_num

for i in range(2, N):
    if num_arr[i] < min_num_2:
        if num_arr[i] < min_num:
            min_num_2 = min_num
            min_num = num_arr[i]
        else:
            min_num_2 = num_arr[i]

print(min_num, min_num_2)


