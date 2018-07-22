# 4. Определить, какое число в массиве встречается чаще всего.


from random import random


N = 27000
num_arr = []
for i in range(N):
    num_arr.append(int(random() * 100))
    print("%3d" % num_arr[i], end='')
print()

count = 0
max_count = 0
max_num = num_arr[0]

num_set = set(num_arr)

for each in num_set:
    count = num_arr.count(each)
    if count > max_count:
        max_count = count
        max_num = each
    count = 0

if max_count > 1:
    print(max_num, max_count)
else:
    print("Все элементы уникальны")


###############################################################################################


count = 0
max_count = 0
max_num = num_arr[0]

num_set = set(num_arr)
num_dict = {each: num_arr.count(each) for each in num_set}

for each in num_dict:
    if num_dict.get(each) > max_count:
        max_num = each
        max_count = num_dict.get(each)

if max_count > 1:
    print(max_num, max_count)
else:
    print("Все элементы уникальны")

##############################################################################


count = 1
max_count = 0
max_num = num_arr[0]

for each in range(N - 1):
    for index in range(each + 1, N):
        if num_arr[each] == num_arr[index]:
            count += 1
    if count > max_count:
        max_count = count
        max_num = num_arr[each]
    count = 1

if max_count > 1:
    print(max_num, max_count)
else:
    print("Все элементы уникальны")


##############################################################################

count = 1
max_count = 0
max_num = num_arr[0]
each = 0

num_arr_cp = num_arr.copy()

while each < (N - 1):
    index = each + 1
    while index < N:
        if num_arr_cp[each] == num_arr_cp[index]:
            count += 1
            num_arr_cp.pop(index)
            N -= 1
        else:
            index += 1
    if count > max_count:
        max_count = count
        max_num = num_arr_cp[each]
    count = 1
    each += 1

if max_count > 1:
    print(max_num, max_count)
else:
    print("Все элементы уникальны")

