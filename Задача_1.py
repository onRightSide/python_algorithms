import collections


company_dict = collections.defaultdict()

while True:
    print("Опции: \n"
          "1 - ввод данных о компании\n"
          "0 - продолжить\n")
    choise = input()
    if choise == "0":
        break
    elif choise == "1":
        sum_ = 0
        name = input("Название: ")
        for i in range(4):
            try:
                sum_ += float(input("Введите прибыль компании за квартал: "))
            except ValueError:
                print("Ошибка! Введенные данные должны быть числом.")
                i -= 1
                break
        else:
            company_dict.update({name: sum_ / 4})
    else:
        print("Опция отсутствует.")

sum_ = 0
number = 0

for each in company_dict:
    sum_ += company_dict.get(each)
    number += 1

middle = sum_ / number

lower_list = []
upper_list = []

for each in company_dict:
    if company_dict.get(each) > middle:
        upper_list.append(each)
    elif company_dict.get(each) < middle:
        lower_list.append(each)
    else:
        continue

print(f"Средняя прибыль для всех компаний: {middle:.2f}")
print(f"Компаниии с меньшей средней прибылью: {lower_list}")
print(f"Компании с большей прибылью: {upper_list}")

