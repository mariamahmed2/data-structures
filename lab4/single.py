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




def add(F1, F2):
    size1 = F1.size
    size2 = F2.size
    finalSize = max(size1, size2)
    finalList = SingleLinkedList()
    p1 = F1.head
    p2 = F2.head
    if size1 >= size2:
        for i in range(size2):
            finalList.add_last(int(p1.data) + int(p2.data))
            p1 = p1.next
            p2 = p2.next

        for i in range(size2, size1):
            finalList.add_last(int(p1.data))
            p1 = p1.next

    else:
        for i in range(size1):
            finalList.add_last(int(p1.data) + int(p2.data))
            p1 = p1.next
            p2 = p2.next

        for i in range(size1, size2):
            finalList.add_last(int(p2.data))
            p2 = p2.next
    return finalList


def sub(F1, F2):
    size1 = F1.size
    size2 = F2.size
    finalSize = max(size1, size2)
    finalList = SingleLinkedList()
    p1 = F1.head
    p2 = F2.head
    if size1 >= size2:
        for i in range(size2):
            finalList.add_last(int(p1.data) - int(p2.data))
            p1 = p1.next
            p2 = p2.next

        for i in range(size2, size1):
            finalList.add_last(int(p1.data))
            p1 = p1.next

    else:
        for i in range(size1):
            finalList.add_last(int(p1.data) - int(p2.data))
            p1 = p1.next
            p2 = p2.next

        for i in range(size1, size2):
            finalList.add_last(-int(p2.data))
            p2 = p2.next
    return finalList


def mul(F1, F2):
    size1 = F1.size
    size2 = F2.size
    finalSize = size1 + size2 - 1
    finalList = SingleLinkedList()
    finalList.initialize("[" + "0, " * (finalSize - 1) + "0]")
    for i in range(size1):
        for j in range(size2):
            finalList.set_element(int(finalList.get_element(i + j)) + int(F1.get_element(i)) * int(F2.get_element(j)),
                                  i + j)

    return finalList


def clear(F1):
    F1.clear()


def eval(F1, x):
    result = 0
    size = F1.size
    for i in range(size):
        result = x * result + int(F1.get_element(i))
    return result


def print_equation(F1):
    temp = []
    size = F1.size
    for power in range(size - 1, -1, -1):
        coeff = int(F1.get_element(size - power - 1))
        if coeff == 0:
            continue
        if (coeff == 1) and (power == size - 1):
            temp.append(power_format(power))
        else:
            temp.append(coeff_format(coeff))
            temp.append(power_format(power))
    temp[0] = temp[0].lstrip("+")
    return ''.join(temp)


def coeff_format(coeff):
    if coeff == 1:
        return "+"
    return str(coeff) if coeff < 0 else "+{0}".format(coeff)


def power_format(power):
    if power == 0:
        return ''
    elif power == 1:
        return 'x'.format(power)
    else:
        return 'x^{0}'.format(power)

def return_var(input):
    if (input == "A") or (input == "a"):
        return A
    elif (input == "B") or (input == "b"):
        return B
    elif (input == "C") or (input == "c"):
        return C
    elif (input == "R") or (input == "r"):
        return R
    else:
        raise Exception

if __name__ == "__main__":

    global R
    R = SingleLinkedList()
    print_times = 0
    try:
        while (1):
            command = input()
            if command == "set":
                sym = input()
                if sym not in ["A", "a", "B", "b", "C", "c", "R", "r"]:
                    raise TypeError("")
                if (sym == "A") or (sym == "a"):
                    Aa = input()
                    global A
                    A = SingleLinkedList()
                    A.initialize(Aa)
                elif (sym == "B") or (sym == "b"):
                    Bb = input()
                    global B
                    B = SingleLinkedList()
                    B.initialize(Bb)
                elif (sym == "C") or (sym == "c"):
                    Cc = input()
                    global C
                    C = SingleLinkedList()
                    C.initialize(Cc)
                else:
                    raise TypeError("")

            elif command == "print":
                letter_print = input()
                if letter_print not in ["A", "a", "B", "b", "C", "c", "R", "r"]:
                    raise TypeError("")
                if (letter_print == "A") or (letter_print == "a"):
                    print(print_equation(A))
                elif (letter_print == "B") or (letter_print == "b"):
                    print(print_equation(B))
                elif (letter_print == "C") or (letter_print == "c"):
                    print(print_equation(C))
                elif (letter_print == "R") or (letter_print == "r"):
                    print(print_equation(R))
                print_times+=1
                if print_times == 3:
                    break

            elif command == "eval":
                eval_letter = input()
                value = input()
                if value.isdigit():
                    if (eval_letter == "A") or (eval_letter == "a"):
                        print(eval(A, value))
                    elif (eval_letter == "B") or (eval_letter == "b"):
                        print(eval(B, value))
                    elif (eval_letter == "C") or (eval_letter == "c"):
                        print(eval(C, value))
                    else:
                        raise TypeError("")
                    break
                else:
                    raise TypeError("")
                break



            elif command == "add":
                operand1 = return_var(input())
                operand2 = return_var(input())
                R = add(operand1, operand2)
                print(print_equation(R))
                break

            elif command == "sub":
                operand1 = return_var(input())
                operand2 = return_var(input())
                R = sub(operand1, operand2)
                print(print_equation(R))
                break

            elif command == "mult":
                operand1 = return_var(input())
                operand2 = return_var(input())
                R = mul(operand1, operand2)
                print(print_equation(R))
                break

            elif command == "clear":
                clear_letter = return_var(input())
                print([])
                break
            else:
                raise Exception
    except:
        print("Error")


#
#
#
# p1 = SingleLinkedList()
# p1.initialize("[32, 41, 67]")
#
# p2 = SingleLinkedList()
# p2.initialize("[2, 3, 1]")
#
# sum = mul(p1, p2)
# sum.list_print()
# print(eval(p2, 2))
# p1.list_print()
# print(print_equation(p1))

# set
# A
# [1,-13,50,-56]
# eval
# A
# 5