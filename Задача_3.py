# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


from random import random


N = 10
# num_arr = [1, 2, 2, 3, 3, 4, 4]
num_arr = []
for i in range(N):
    num_arr.append(int(random() * 100))
    print("%3d" % num_arr[i], end='')
print()

max_num = num_arr[0]
max_num_index = 0
min_num = num_arr[0]
min_num_index = 0

print(num_arr)

index = 0

for each in num_arr:
    if each > num_arr[max_num_index]:
        max_num_index = index
    elif each < num_arr[min_num_index]:
        min_num_index = index
    index += 1

if max_num_index < min_num_index:
    max_num = num_arr.pop(max_num_index)
    min_num_index -= 1
    min_num = num_arr.pop(min_num_index)
else:
    max_num = num_arr.pop(max_num_index)
    min_num = num_arr.pop(min_num_index)

num_arr.insert(min_num_index, max_num)
num_arr.insert(max_num_index, min_num)

print(num_arr)

########################################################################

max_num = max(num_arr)
min_num = min(num_arr)

max_num_index = num_arr.index(max_num)
min_num_index = num_arr.index(min_num)

num_arr[max_num_index], num_arr[min_num_index] = num_arr[min_num_index], num_arr[max_num_index]

print(num_arr)