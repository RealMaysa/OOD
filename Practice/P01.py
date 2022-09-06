


class Stack:
    def __init__(self,L=None):
        if L==None:
            self.item=[]
        else:
            self.item=L
    
    def push(self,e):
        self.item.append(e)

    def pop(self):
        if len(self.item)==0:
            return print('Stack is empty')
        else:
            return self.item.pop()

    def peek(self):
        return self.item[-1]

    def isEmpty(self):
        return len(self.item)==0

    def size(self):
        return len(self.item)


print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(),"Data in stack : ",s.item)

while not s.isEmpty():

    s.pop()

print(s.size(),"Data in stack : ",s.item)
        