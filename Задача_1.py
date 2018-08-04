from random import random


def bubble(num_list):
    print(num_list)
    len_ = len(num_list)
    n = 1
    while n < len_:
        flag = False
        for i in range(len_ - n):
            if num_list[i] < num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
                flag = True
        if not flag:
            break
        n += 1

    return num_list


test_list = [14, 9, 15, -12, -19, 9, 5, 7, 0, -8, 9, 14, 4, 1, 5, -4, 14, 4, 2, 12]


print(bubble(test_list))

