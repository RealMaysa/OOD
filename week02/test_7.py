'''
จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue

โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้

แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ

แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ

ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2

จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2] จนกว่าแถวหลักจะหมด

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

token = list(input("Enter people : "))
Q=Queue()
Q2=Queue()
i=1
count=0
count2=0
while token!= []:
    e=token[0]
    if count%3==0 and count!= 0:
        Q.deQueue()
    if count2%2==0 and count2!= 0:
        Q2.deQueue()
    if Q.size()==5:
        Q2.enQueue(e)
    else:
        Q.enQueue(e)
   
    if Q.isEmpty() != True:
        c1timerun = True
    else :
        c1timerun = False
    if Q2.isEmpty() != True:
        c2timerun = True
    else :
        c2timerun = False
    token.pop(0)
    print(i,token,Q.items,Q2.items)
    if c1timerun:
        count+=1
    if c2timerun:
        count2+=1
    i+=1           
    
    

    
    