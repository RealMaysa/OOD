'''
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา
A  <value>  ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK
P  ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น -1
*** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty
'''
class Stack :
    def __init__(self,L=None):
        if L==None:
            self.item=[]
        else:
            self.item=L
    
    def push(self,e):
        self.item.append(e)
    
    def is_Empty(self):
        return len(self.item)==0
    
    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def size(self):
        return str(len(self.item))

ls=input('Enter input: ').split(',')
s=Stack()
i=0

while i<len(ls):
    e=ls[i].split(' ')
    if e[0]=='A':
        s.push(e[1])
        print(s.size())
    elif e[0]=='P':
        
        if s.is_Empty()==True:
            print('-1')
        else:
            print(s.peek())
            print(s.item.index(s.peek()))
            print(s.pop())
    i+=1        
if s.is_Empty()!=True:
    print(s.item)
else:
    print('Empty')



