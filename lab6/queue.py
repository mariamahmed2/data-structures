class Queue:
    def __init__(self):
        self.llist = []
        self.size = 0

    def add_front(self, data):
        self.llist.insert(0, data)
        self.size += 1


    def list_print(self):
        print(self.llist)


    def delete_element(self):
        self.llist.pop()
        self.size -= 1


    def is_empty(self):
        if self.size == 0:
            return True
        return False


    def initialize(self, data_):
        if data_ != "[]":
            data_ = data_[1:-1]
            data_ = data_.replace(" ", "").split(',')
            res = [eval(i) for i in data_]
            self.llist = res
            self.size = len(res)

if __name__ == "__main__":
    my_list = Queue()
    input_list = input()
    my_list.initialize(input_list)
    command = input()
    try:
        if command == "enqueue":
            data = int(input())
            if data:
                my_list.add_front(data)
                my_list.list_print()
            else:
                print("Error")
        elif command == "isEmpty":
            print(my_list.is_empty())
        elif command == "dequeue":
            my_list.delete_element()
            my_list.list_print()
        elif command == "size":
            print(my_list.size)
        else:
            print("Error")
    except TypeError:
        print("Error")