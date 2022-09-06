class Queue:
    def __init__(self,L=None) :
        self.front=0
        if L==None:
            self.item=[]
        else:
            self.item=L
    
    def enQueue(self,e):
        self.item.append(e)
    
    def deQueue(self):
        return self.item.pop(0)
    
    def is_Empty(self):
        return len(self.item)==0
    
    def size(self):
        return len(self.item)

    def peek(self):
        return self.item[self.front]

