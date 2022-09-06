class Queue():

    def __init__(self, ls = None):
        self.front = 0
        if ls is None:
            self.items = []
        else:
            self.items=ls

    def enQueue(self,i):

        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[self.front]
    



token = list(input("Enter Input : ").split(','))
Q=Queue()
i=0
while i<len(token):
    e=token[i].split()
    if e[0]=='E':
        Q.enQueue(e[1])
        print(Q.size())
        
    else:
        if not Q.isEmpty(): 
            print(Q.peek(),Q.items.index(Q.peek()))
            Q.deQueue()
        else: 
            print("-1")
            
    i+=1
if not Q.isEmpty():
    for q in Q.items:
        print(q,end=" ")
else :
    print("Empty")
