# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
# равенство: 1+2+...+n = n(n+1)/2, где n – любое натуральное число.


def progression(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def progression_sum(n): 
    return n*(n + 1)/2


for i in range(0, 11):
    print(progression(i) == progression_sum(i))