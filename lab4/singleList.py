class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new_node
        self.size += 1

    def add_index(self, data, index):
        if index > self.size or index < 0:
            raise TypeError("")
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            p = self.head
            for i in range(0, index - 1):
                p = p.next
            u = p.next
            new_node.next = u
            p.next = new_node
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

    def get_element(self, index):
        if self.not_in_bound(index):
            raise TypeError("")
        p = self.head
        for i in range(0, index):
            p = p.next
        return p.data

    def set_element(self, data, index):
        if self.not_in_bound(index):
            raise TypeError("")
        p = self.head
        for i in range(0, index):
            p = p.next
        p.data = data

    def not_in_bound(self, index) -> bool:
        return index >= self.size or index < 0

    def delete_element(self, index):
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

    def clear(self):
        # while (self.size > 0):
        #   self.deleteElement(0)
        self.head = None
        self.size = 0

    def sublist(self, start_index, end_index):
        if self.not_in_bound(start_index) or \
                self.not_in_bound(end_index) or \
                end_index < start_index:
            raise TypeError("")
        p = self.head
        for i in range(0, start_index):
            p = p.next
        new_sublist = SingleLinkedList()
        for i in range(start_index, end_index + 1):
            new_sublist.add_last(p.data)
            p = p.next
        return new_sublist

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

    def initialize(self, data_):
        if data_ != "[]":
            data_ = data_[1:-1]
            data_ = data_.replace(" ", "").split(',')
            for i in range(len(data_)):
                self.add_last(data_[i])


if __name__ == "__main__":
    my_list = SingleLinkedList()
    input_list = input()
    my_list.initialize(input_list)
    command = input()
    try:
        if command == "add":
            data = input()
            my_list.add_last(data)
            my_list.list_print()
        elif command == "addToIndex":
            index = int(input())
            data = input()
            my_list.add_index(data, index)
            my_list.list_print()
        elif command == "get":
            index = int(input())
            print(my_list.get_element(index))
        elif command == "set":
            index = int(input())
            data = input()
            my_list.set_element(data, index)
            my_list.list_print()
        elif command == "clear":
            my_list.clear()
            my_list.list_print()
        elif command == "isEmpty":
            print(my_list.is_empty())
        elif command == "remove":
            index = int(input())
            my_list.delete_element(index)
            my_list.list_print()
        elif command == "sublist":
            start_index = int(input())
            end_index = int(input())
            subList = my_list.sublist(start_index, end_index)
            subList.list_print()
        elif command == "contains":
            data = input()
            print(my_list.contains(data))
        elif command == "size":
            print(my_list.size)
        else:
            print("Error")
    except TypeError:
        print("Error")
