import collections


def sum_hex(first_num, second_num):

    num_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11,
                "C": 12, "D": 13, "E": 14, "F": 15}

    char_dict = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B",
                 12: "C", 13: "D", 14: "E", 15: "F"}

    a = list(first_num)
    a_decue = collections.deque(a)

    b = list(second_num)
    b_decue = collections.deque(b)

    answer = collections.deque()

    first_len = len(a)
    second_len = len(b)

    res = 0

    if second_len > first_len:
        first_len, second_len = second_len, first_len

    for i in range(second_len):
        sum_ = num_dict.get(collections.deque.pop(a_decue)) + num_dict.get(collections.deque.pop(b_decue)) + res
        if sum_ >= 16:
            res = sum_ // 16
        else:
            res = 0
        collections.deque.appendleft(answer, char_dict.get(sum_ % 16))

    if len(a) > len(b):
        for i in range(second_len, first_len):
            sum_ = num_dict.get(collections.deque.pop(a_decue)) + res
            if sum_ >= 16:
                res = sum_ // 16
            else:
                res = 0
            collections.deque.appendleft(answer, char_dict.get(sum_ % 16))

    else:
        for i in range(second_len, first_len):
            sum_ = num_dict.get(collections.deque.pop(b_decue)) + res
            if sum_ >= 16:
                res = sum_ // 16
            else:
                res = 0
            collections.deque.appendleft(answer, char_dict.get(sum_ % 16))

    while res > 0:
        collections.deque.appendleft(answer, char_dict.get(res % 16))
        res = res // 16

    answer = list(answer)

    return answer


def mult_hex(first_num, second_num):

    num_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11,
                "C": 12, "D": 13, "E": 14, "F": 15}

    char_dict = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B",
                 12: "C", 13: "D", 14: "E", 15: "F"}

    a = list(first_num)
    b = list(second_num)
    a_decue = collections.deque(a)

    prev_sum = collections.deque()
    curr_sum = collections.deque()

    first_len = len(a)
    second_len = len(b)

    for i in range(first_len):
        multiplier = num_dict.get(collections.deque.pop(a_decue))
        for k in range(i):
            collections.deque.append(curr_sum, "0")
        res = 0
        for j in range(second_len - 1, -1, -1):
            mult_ = multiplier * num_dict.get(b[j]) + res
            if mult_ >= 16:
                res = mult_ // 16
            else:
                res = 0
            collections.deque.appendleft(curr_sum, char_dict.get(mult_ % 16))

        while res > 0:
            collections.deque.appendleft(curr_sum, char_dict.get(res % 16))
            res = res // 16

        prev_sum = collections.deque(sum_hex(list(prev_sum), list(curr_sum)))
        collections.deque.clear(curr_sum)

    prev_sum = list(prev_sum)
    return prev_sum


check_set = frozenset("0123456789ABCDEF")

while True:
    first = input("Введите первое шестнадцатиричное число: ")
    if not set(first).issubset(check_set):
        print("Ошибка ввода шестнадцатиричного числа!")
        continue
    first = list(first)
    break

while True:
    second = input("Введите Второе шестнадцатиричное число: ")
    if not set(second).issubset(check_set):
        print("Ошибка ввода шестнадцатиричного числа!")
        continue
    second = list(second)
    break

print(f"{first} + {second} = {sum_hex(first, second)}")

print(f"{first} * {second} = {mult_hex(first, second)}")

