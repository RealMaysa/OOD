'''
จงเขียนโปรแกรมโดยใช้ Stack เพื่อคำนวณหา ค่าของนิพจน์แบบ postfix 

โดยให้แสดงผลลัพธ์ตามตัวอย่าง



class Stack():

    def __init__(self, ls = None):

    def push(self,i):

    def pop(self):

    def isEmpty(self):

    def size(self):

def postFixeval(st):

    s = Stack()

    ### Enter Your Code Here ###

    return s.pop()

            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))


'''


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

def postFixeval(st):

    s = Stack()
    i=0
    while i<len(st):
        e=st[i]
        if e not in '+-*/':
            s.push(e)
        else:
            if e =='+':
                x=float(s.pop())
                y=float(s.pop())
                s.push(y+x)
             
            elif e =='-':
                x=float(s.pop())
                y=float(s.pop())
                s.push(y-x)
            elif e =='*':
                x=float(s.pop())
                y=float(s.pop())
                s.push(y*x)
            else:
                x=float(s.pop())
                y=float(s.pop())
                s.push(y/x)
            
        i+=1

    return s.pop()

            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))