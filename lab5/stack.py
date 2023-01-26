# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_index(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def list_print(self):
        p = self.head
        print("[", end=""),
        while p:
            if p.next:
                print(p.data, end=", ")
            else:
                print(p.data, end="")
            p = p.next
        print("]")

    def get_element(self):
        index = self.size - 1
        if self.not_in_bound(index):
            raise TypeError("")
        p = self.head
        for i in range(0, index):
            p = p.next
        return p.data

    def not_in_bound(self, index) -> bool:
        return index >= self.size or index < 0

    def delete_element(self):
        index = self.size - 1
        if self.not_in_bound(index):
            raise TypeError("")

        if index == 0:
            p = self.head
            self.head = p.next
        else:
            cur = self.head
            prev = None
            for i in range(0, index):
                prev = cur
                cur = cur.next
            prev.next = cur.next
        self.size -= 1

    def is_empty(self):
        if self.size == 0 or self.head is None:
            return True
        return False

    def contains(self, data):
        p = self.head
        for i in range(self.size):
            if p.data == data:
                return True
            p = p.next
        return False

    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def initialize(self, data_):
        if data_ != "[]":
            data_ = data_[1:-1]
            data_ = data_.replace(" ", "").split(',')
            for i in range(len(data_)):
                self.add_index(data_[i])


if __name__ == "__main__":
    my_list = SingleLinkedList()
    input_list = input()
    my_list.initialize(input_list)
    command = input()
    try:
        if command == "push":
            data = input()
            my_list.reverse()
            my_list.add_index(data)
            my_list.list_print()
        elif command == "peek":
            print(my_list.get_element())
        elif command == "isEmpty":
            print(my_list.is_empty())
        elif command == "pop":
            my_list.delete_element()
            my_list.reverse()
            my_list.list_print()
        elif command == "size":
            print(my_list.size)
        else:
            print("Error")
    except TypeError:
        print("Error")