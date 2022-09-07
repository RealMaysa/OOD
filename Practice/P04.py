
'''
จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้
A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack
P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )
D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  
LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )
MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )
การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม
*** Hint ***
ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ
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
def ManageStack(ls):
    s=Stack()
    temp=Stack()
    for i in ls:
        e=ls[i].split(' ')
        if e[0]=='A':
            s.push(e)
        elif e[0]=='P':
            if(s.is_Empty()):
                print('-1')
            else:
                print(s.pop())
        elif e[0]=='D':
            
            if(s.is_Empty()):
                print('-1')
            else:
                for i in s.item:
                    if e[1]==s.item[i]:
                        s.item.remove(s.item[i])
                    else:
                        pass

        elif e[0]=='LD':
            if(s.is_Empty()):
                print('-1')
            else:
                temp.push(e[1])
                if s.
        elif e[0]=='MD':

    if s.is_Empty()!= True:
        for i in s:
            print(s.pop())

inp = input('Enter Input : ').split(',')

