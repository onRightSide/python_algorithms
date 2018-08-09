import hashlib


def new_search(s):
    def sub_search(sub):
        pattern = hashlib.sha1(sub.encode("UTF-8")).hexdigest()
        sub_len = len(sub)

        s_len = len(s)
        sub_counter = 0
        for index in range(s_len - sub_len + 1):
            if pattern == hashlib.sha1(s[index: index + sub_len].encode("UTF-8")).hexdigest():
                sub_counter += 1

        return sub_counter

    return sub_search


while True:
    print("\nВведите строку, в которой будет производится поиск\n"
          "Или введте пустую строку ''(Нажмите Enter) для выхода")
    search_in = input("\tИсходная строка: ")

    if search_in:
        quote_search = new_search(search_in)

        while True:
            print("\nВведите искомую подстроку\n"
                  "Или введте пустую строку ''(Нажмите Enter) для возврата")
            search_for = input("\tИскомая подстрока: ")

            if search_for:
                print(f"\tИскомая подстрока встречается в исходной строке {quote_search(search_for)} раз")
            else:
                break
    else:
        break
