class Stack():

    def __init__(self, ls = None):
        if ls is None:
            self.items = []
        else:
            pass

    def push(self,i):

        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self) :  
        return self.items[-1]


    def Curse(self):
        self.temp = []
        for i in self.items:
            if int(i)%2==0:
                self.temp.append(int(i)-1)
            else:
                self.temp.append(int(i)+2)
        self.items = self.temp

def stackCheck(st):
    S = Stack()
    if len(st)==0:
        return '0'
    else:
        test = int(st[len(st)-1]) 
        S.push(test)
        for i in range(len(st)-2,-1,-1):
            if int(st[i])>test:
                test = int(st[i])
                S.push(test)
        return S.size()
            
S = Stack()
inp = input('Enter Input : ').split(',')
for i in inp:
    l = i.split()
    if l[0]=='A':
        S.push(l[1])
    elif l[0]=='B':
        print(stackCheck(S.items))
    elif l[0]=='S':
        S.Curse()













