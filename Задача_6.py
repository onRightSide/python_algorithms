# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


from random import random


N = 27
num_arr = []
for i in range(N):
    num_arr.append(int(random() * 100))
    print("%3d" % num_arr[i], end='')
print()

num_set = set(num_arr)

max_num = num_arr[0]
min_num = num_arr[0]
sum_ = 0

for each in num_set:
    if each > max_num:
        max_num = each
    elif each < min_num:
        min_num = each

# max_num = max(num_set)
# min_num = min(num_set)

max_index = num_arr.index(max_num)
min_index = num_arr.index(min_num)

if min_index > max_index:
    max_index, min_index = min_index, max_index

for index in range(min_index + 1, max_index):
    sum_ += num_arr[index]
    print(num_arr[index], end=" ")
print()

print(sum_)

