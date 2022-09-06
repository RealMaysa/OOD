
PRIORITY = {'+':1, '-':1, '*':2, '/':2} 

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

def infix2postfix(exp) :
    
    s = Stack()
    i=0
    result=""
    while i<len(exp):
        e=exp[i]
        if e not in '+-*/()':
            result += e
        elif e =='(' :
            s.push(e)
        elif e == ')':
            while not s.isEmpty() and s.peek() != '(' :
                result+=s.pop()
            s.pop()
        else:
            while not s.isEmpty() and s.peek() != '(' and PRIORITY[e]<=PRIORITY[s.peek()]:
                result+=s.pop()
            s.push(e)
        i+=1
    while not s.isEmpty():
            result+=s.pop()
    return result



        

print(" ***Infix to Postfix***")

token = input("Enter Infix expression : ")

print("PostFix : ")

print(infix2postfix(token))