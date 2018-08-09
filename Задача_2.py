from collections import Counter


class HNode:

    def __init__(self, symbol=None, weight=None, left=None, right=None):
        self.weight = weight
        self.symbol = symbol
        self.left = left
        self.right = right

    def is_leaf(self):
        if not self.left and not self.right:
            return True
        else:
            return False

    def make_dict(self, dict_, code_=''):
        if self.is_leaf():
            dict_.update({self.symbol: code_})
        else:
            if self.left:
                self.left.make_dict(dict_, code_ + '0')
            if self.right:
                self.right.make_dict(dict_, code_ + '1')


class HTree:
    def __init__(self, symbol=None, weight=None, left_node=None, right_node=None):
        self.root = HNode(symbol, weight, left_node, right_node)

    def make_code_dict(self):
        if self.root:
            code_dict = {}
            if self.root.is_leaf():
                code_dict.update({self.root.symbol: "0"})
                return code_dict
            else:
                self.root.make_dict(code_dict)
                return code_dict
        else:
            return None


def make_h_tree(str_):
    c = Counter(str_)
    while c:
        # print(c)
        left = c.most_common()[-1]
        left_ = None
        try:
            left[0].root
            left_ = left[0]

        except AttributeError:
            left_ = HTree(left[0], left[1])

        c.pop(left[0])

        if c:
            right_ = None
            right = c.most_common()[-1]
            try:
                right[0].root
                right_ = right[0]

            except AttributeError:
                right_ = HTree(right[0], right[1])

            c.pop(right[0])

            new_tree = HTree(left_.root.symbol + right_.root.symbol, left_.root.weight + right_.root.weight,
                             left_.root, right_.root)

            c.update({new_tree: left_.root.weight + right_.root.weight})

        else:
            return left_


def haffman_encode(str_):
    if str_:
        c = Counter(str_)

        encoding_tree = make_h_tree(str_)

        encoding_dict = encoding_tree.make_code_dict()

        str_coded = ''

        for sign in str_:
            str_coded += encoding_dict.get(sign)

        return str_coded, encoding_dict
    else:
        return "", None


def haffman_decode(str_, code_dict={}):
    if str_:
        str_decoded = ""
        decode_dict = {}
        index = 0
        len_ = len(str_)

        for key in code_dict:
            decode_dict.update({code_dict.get(key): key})

        while index <= len_:

            for end_index in range(index, len_ + 1):
                if str_[index:end_index] in decode_dict:

                    str_decoded += decode_dict.get(str_[index:end_index])
                    index = end_index
                    break
            else:
                index += 1

        return str_decoded
    else:
        return ""


str_ = input("\nВведите строку для кодирования алгоритмом Хаффмана: \n\t")
#test_pattern = "War is peace. Freedom is slavery. Ignorance is strength."
#str_ = test_pattern

encoded = haffman_encode(str_)
print(f"Полученная кодировка:\n \t{encoded[1]}\n")
print(f"Закодированная строка:\n \t{encoded[0]}\n")

print(f"Раскодирование строки обратным словарем:\n \t{haffman_decode(encoded[0], encoded[1])}\n")




