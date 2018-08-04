from random import random


class Node:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def add_child(self, data):
        if data > self.data:
            if self.right:
                self.right.add_child(data)
                return
            else:
                self.right = Node(data)
        else:
            if self.left:
                self.left.add_child(data)
                return
            else:
                self.left = Node(data)

    def append_to_list(self):

        list_ = []

        if self.left:
            list_.extend(self.left.append_to_list())
        list_.append(self.data)
        if self.right:
            list_.extend(self.right.append_to_list())

        return list_


class Tree:

    def __init__(self):
        self.root = None

    def add_node(self, data):
        if self.root:
            self.root.add_child(data)
        else:
            self.root = Node(data)

    def list_(self):
        if self.root:
            return self.root.append_to_list()
        else:
            return None


def median_find(num_list):

    print(num_list)

    if len(num_list) % 2 == 0:
        return "Не ищем медиану в массиве четной длины"

    index = 0
    bigger_sum = 0
    smaller_sum = 0
    same = -1

    num_set = frozenset(num_list)

    for num in num_set:
        median = num
        for each in num_list:
            if each > median:
                bigger_sum += 1
            elif each < median:
                smaller_sum += 1
            else:
                same += 1

        rest = same - abs(smaller_sum - bigger_sum)

        if rest >= 0 and rest % 2 == 0:
            return median
        else:
            index += 1
            bigger_sum = 0
            smaller_sum = 0
            same = -1


def median_find_sorted(num_list):
    new_tree = Tree()

    for num in num_list:
        new_tree.add_node(num)

    sorted_list = new_tree.list_()

    print(sorted_list)

    return sorted_list[len(sorted_list) // 2]


test_list = []
for i in range(19):
    test_list.append(int(random() * 20))

print("Медиана:", median_find(test_list))

print("Медиана:", median_find_sorted(test_list))

