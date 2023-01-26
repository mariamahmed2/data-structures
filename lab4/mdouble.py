class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

    def getPrev(self):
        return self.prev

    def setPrev(self, prev):
        self.prev = prev

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addLast(self, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
        else:
            p = self.head
            while (p.getNext() != None):
                p = p.getNext()
            p.setNext(newNode)
            newNode.setPrev(p)
        self.size += 1

    def addIndex(self, data, index):
        if index > self.size or index < 0:
            raise TypeError("")
        newNode = Node(data)
        p = self.head
        for i in range(0, index - 1):
            p = p.getNext()
        u = p.getNext()
        newNode.setNext(u)
        newNode.setPrev(p)
        p.setNext(newNode)
        u.setPrev(newNode)
        self.size += 1

    def listPrint(self):
        p = self.head
        print("[", end=""),
        while p is not None:
            if p.getNext() is not None:
                print(p.data, end=", ")
            else:
                print(p.data, end="")
            p = p.getNext()
        print("]")

    def getElement(self, index):
        if index >= self.size or index < 0:
            raise TypeError("")
        p = self.head
        for i in range(0, index):
            p = p.getNext()
        return p.getData()

    def setElement(self, data, index):
        if index >= self.size or index < 0:
            raise TypeError("")
        p = self.head
        for i in range(0, index):
            p = p.getNext()
        p.setData(data)

    def deleteElement(self, index):
        if index >= self.size or index < 0:
            raise TypeError("")
        if index == 0:
            p = self.head
            self.head = p.getNext()
            p.setNext(None)
        else:
            p = self.head
            for i in range(0, index - 1):
                p = p.getNext()
            u = p.getNext()
            w = u.getNext()
            p.setNext(w)
            w.setPrev(p)
            u.setNext(None)
            u.setPrev(None)
        self.size -= 1

    def clearList(self):
        while (self.size > 0):
            self.deleteElement(0)

    def sublist(self, startIndex, endIndex):
        if endIndex >= self.size:
            raise TypeError("")
        if endIndex < startIndex:
            raise TypeError("")
        p = self.head
        for i in range(0, startIndex):
            p = p.getNext()
        newSublist = DoublyLinkedList()
        for i in range(startIndex, endIndex + 1):
            newSublist.addLast(p.getData())
            p = p.getNext()
        return newSublist

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def listContain(self, data):
        p = self.head
        found = False
        for i in range(self.size):
            if p.getData() == data:
                found = True
            p = p.getNext()
        return found

    def initializeList(self, data):
        if data != "[]":
            data = data[1:-1]
            data = data.replace(" ", "").split(',')
            for i in range(len(data)):
                self.addLast(data[i])


Mylist = DoublyLinkedList()
inputList = input()
Mylist.initializeList(inputList)
command = input()
try:
    if command == "add":
        data = input("")
        Mylist.addLast(data)
        Mylist.listPrint()
    elif command == "addToIndex":
        index = int(input(""))
        data = input("")
        Mylist.addIndex(data, index)
        Mylist.listPrint()
    elif command == "get":
        index = int(input(""))
        print(Mylist.getElement(index))
    elif command == "set":
        index = int(input(""))
        data = input("")
        Mylist.setElement(data, index)
        Mylist.listPrint()
    elif command == "clear":
        Mylist.clearList()
        Mylist.listPrint()
    elif command == "isEmpty":
        print(Mylist.isEmpty())
    elif command == "remove":
        index = int(input(""))
        Mylist.removeIndex(index)
        Mylist.listPrint()
    elif command == "sublist":
        startIndex = int(input(""))
        endIndex = int(input(""))
        subList = Mylist.sublist(startIndex, endIndex)
        subList.listPrint()
    elif command == "contains":
        data = input("")
        print(Mylist.listContain(data))
    elif command == "size":
        print(Mylist.size)
except:
    print("Error")

    # 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