class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head is None :
          p = Node(item)
          self.head = p
          self.tail = p
        else :
            q = self.tail
            p = Node(item)
            q.next = p
            p.previous = self.tail
            self.tail = p

    def addHead(self, item):
        if self.head is None :
            p = Node(item)
            self.head = p
            self.tail = p
        else :
            p = Node(item)
            self.head.previous = p
            self.head.previous.next = self.head
            self.head = p


    def insert(self, pos, item):
        indx = 0
        q = Node(item)
        p = self.head
        if self.size() > pos and pos>0 :
            while p != None :
                if indx != pos:
                    p = p.next
                    indx+=1
                else :
                    q.previous = p.previous
                    q.next = p
                    p.previous.next = q
                    p.previous =q
                    p = p.next
                    indx+=1
        elif pos >= self.size():
            self.append(item)
        elif pos == 0 or -pos > self.size():
            self.addHead(item)
        else :
            p = self.tail
            indx =-1
            while p != None :
                if indx != pos:
                    p = p.previous
                    indx-=1
                else :
                    q.previous = p.previous
                    q.next = p
                    p.previous.next = q
                    p.previous =q
                    p = p.previous
                    indx-=1

    def search(self, item):
        p = self.head
        while p != None:
            if p.value == item:
                return "Found"
            p = p.next
        return "Not Found"

    def index(self, item):
        p = self.head
        indx = 0
        while p != None:
            if p.value == item:
                return indx
            else :
                indx+=1
            p = p.next
        return -1

    def size(self):
        size = 0
        p =self.head
        while p != None:
            size +=1
            p = p.next
        return size

    def pop(self, pos):
        indx = 0
        p = self.head
        if self.size() != 0:
            if self.size()-1 > pos and pos > 0:
                while p != None :
                    if pos ==indx:
                        p.previous.next = p.next
                        p.next.previous = p.previous
                    indx +=1
                    p = p.next
            elif pos ==0 and self.size()==1:
                self.head = None
                self.tail = None
            elif pos ==0 :
                p.next.previous = None
                self.head = p.next
            elif pos == self.size()-1:
                p = self.tail
                p.previous.next = None
                self.tail = p.previous
            else :
                return "Out of Range"
            return "Success"
        else :
            return "Out of Range"


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())