'''

จงเขียนโปรแกรมเพื่อตรวจสอบว่า นิพจน์มีวงเล็บครบถ้วนหรือไม่ โดยใช้ Stack ช่วยในการแก้ปัญหา

โดยสามารถแจ้งได้ว่าข้อผิดพลาดที่เกิดขึ้นเกิดจากสาเหตุใด

1. มี วงเปิดไม่ตรงชนิดกับวงเล็บปิด

2. วงเล็บปิดเกิน

3. วงเล็บเปิดเกิน

แล้วให้แสดงผลตามตัวอย่าง
'''

ls = str(input("Enter expresion : "))

       
class Stack:


    def __init__(self):
        self.items=[]
        

    def push(self,i):

        self.items.append(i)
        

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def match(op,cl):
            return (op=='('and cl ==')') or \
                (op=='{'and cl =='}') or\
                    (op=='['and cl ==']')

def perenMatching(ls):
    s = Stack() 
    i=0
    error=0

    while i<len(ls) and error==0:
        e=ls[i]
        if e in '{[(':
            s.push(e)
        else:
            if e in '}])':
                if s.size()>0:
                    if not match(s.pop(),e) :
                        error=1
                else:
                    error=2

        i+=1

    if s.size()>0 and error == 0:
        error=3

    return error,e,i,s


error,e,i,s=perenMatching(ls)


if error==1:
    print(ls,"Unmatch open-close")
elif error==2:
    print(ls,"close paren excess")
elif error==3:
    print(ls,f'open paren excess   {s.size()} : ',end='')
    for e in s.items:
        print(e,end='')
else:
    print(ls,'MATCH')



