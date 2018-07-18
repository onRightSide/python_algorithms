# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

num_arr = input("Введите поседовательность чисел через пробел: ").split(" ")
max_sum = 0
new_sum = 0
num = 0


for each in num_arr:
    each = int(each)
    i = 0
    while each // pow(10, i):
        new_sum += each // pow(10, i) % 10
        i += 1
        # print(new_sum)
    if max_sum < new_sum:
        max_sum = new_sum
        num = each
    new_sum = 0
print(f"Число {num} является наибольшим по сумме своих цифр: {max_sum}!")
