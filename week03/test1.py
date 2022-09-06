class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
       

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p=Node(item)
        if self.head==None:
            self.head=p
            
        else:
            t=self.head
            while t.next!=None:
                t=t.next
            t.next=p
        

    def addHead(self, item):
        p=Node(item)
        p.next=self.head
        self.head=p

    def search(self, item):
        t=self.head
        while t!=None:
            if t.value==item:
                return "Found"
            t=t.next
        
        return "Not Found"
        


    def index(self, item):
        t=self.head
        count=0
        while  t!=None:
                if t.value==item:
                    return count
                else:
                    count+=1
                t=t.next
        return -1

    def size(self):
        size=0
        t=self.head
        while  t!=None:
                t=t.next
                size+=1
        return size

    def pop(self, pos):
        
        if pos<0 or pos >= self.size():
            return "Out of Range"
        if pos==0 and self.size()>0:
            self.head=self.head.next
            return "Success" 
        else:
            p = self.head
            for i in range(0,pos-1):
                p = p.next 
            p.next = p.next.next
            return "Success"



L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
         print("{0} {1} in {2}".format(L.search(i[3:]), i[3:],L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)