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
       # if data_ != "[]":
        #data_ = data_[1:-1]
        data_ = list(data_)
        #    data_ = data_.replace(" ", "").split(',')
        for i in range(len(data_)):
            self.add_index(data_[i])



    def isOperand(self, ch):
        return ch.isalpha()

    def notGreater(self, i):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3}
        if self.get_element() == '(':
            return False
        a = precedence[i]
        b = precedence[self.get_element()]
        if a <= b:
            return True
        else:
            return False

    def infixToPostfix(self, exp):
        output = ""
        for i in exp:

            if self.isOperand(i) == True:  # check if operand add to output
                print(i, "~ Operand push to stack")
                output = output + i

            # If the character is an '(', push it to stack
            elif i == '(':
                self.reverse()
                self.add_index(i)
                print(i, " ~ Found ( push into stack")

            elif i == ')':  # if ')' pop till '('
                while (self.is_empty() != True and self.get_element() != '('):
                    self.delete_element()
                    n = self.reverse()
                    output = output + n
                    print(n, "~ Operator popped from stack")
                if (self.is_empty() != True and self.get_element() != '('):
                    print("_________")
                    return -1
                else:
                    self.delete_element()
                    x= self.reverse()
                    print(x, "Popping and deleting (")
            else:
                while (self.is_empty() != True and self.notGreater(i)):
                    self.delete_element()
                    c= self.reverse()
                    output = output + c
                    print(c, "Operator popped after checking precedence from stack")
                self.reverse()
                self.add_index(i)
                print(i, "Operator pushed to stack")

        # pop all the operator from the stack
        while self.is_empty() != True:
            self.delete_element()
            xx = self.reverse()
            output = output + xx
            print(xx, "~ pop at last")
        print(output)
        self.list_print()



if __name__ == "__main__":
   # my_list = SingleLinkedList()
    input_list = input()
    #my_list.initialize(input_list)
    a = input("a=", )
    b = input("b=", )
    c = input("c=", )

    try:
        if a.isdigit() and b.isdigit() and c.isdigit():
            my_list = SingleLinkedList()
            my_list.initialize(input_list)
            my_list.infixToPostfix(input_list)
        else:
            print("Error")
    except TypeError:
        print("Error")
