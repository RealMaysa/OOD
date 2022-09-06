'''
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา



E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผล Size ปัจจุบันของ QUEUE

D                 ให้ทำการแสดงผลของvalueที่อยู่หน้าสุดและindexของvalueนั้นจากนั้นทำการ De_QUEUE ถ้าหากไม่มี value อยู่ใน Queue ให้แสดงผลเป็น  -1

*** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty


'''

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
