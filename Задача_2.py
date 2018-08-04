from random import random


def insert(num_list, start, stop):

    temp = [] * stop
    middle = int((stop + start) / 2)

    if stop - start > 1:
        left_list = insert(num_list, start, middle)
        right_list = insert(num_list, middle, stop)
    else:
        temp.append(num_list[start])
        return temp

    k = 0

    for i in range(0, len(left_list)):
        for j in range(0 + k, len(right_list)):
            if left_list[i] > right_list[j]:
                temp.append(right_list[j])
                k += 1
            else:
                temp.append(left_list[i])
                break
        else:
            temp.append(left_list[i])

    if k != stop - middle:
        for i in range(k, stop - middle):
            temp.append(right_list[i])

    return temp


test_list = []
for i in range(30):
    test_list.append(int(random() * 100))

print(test_list)

print(insert(test_list, 0, len(test_list)))


