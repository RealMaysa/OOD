class Node:
    def __init__(self, data,left=None,right=None): #แก้การสร้างNodeให้เป็นแบบนี้ด้วย
        self.data = data  
        self.left = left  
        self.right = right  
    def __str__(self):
        return str(self.data)
class Stack:
    def __init__(self,list=None):
        if list==None:
            self.item=[]
        else:
            self.item=list
    def pop(self):
        return self.item.pop()
    def push(self,i):
        return self.item.append(i)
    def size(self):
        return str(len(self.item))
    def isEmpty(self):
        return len(self.item)==0
def printTree(node,level=0):
    if node!=None:
        printTree(node.right,level+1)
        print('       '*level,node)
        printTree(node.left,level+1)

s = Stack()

def infix(node):
    if node==None:#ไม่มี node
        return ""
    s = ""
    if node.left is not None and node.right is not None:#ไม่มีซ้ายและขวา
        s+='(' #ใส่วงเล็บ
    s += infix(node.left)+str(node.data)+infix(node.right)#inorder
    if node.left is not None and node.right is not None:
        s+=')'
    return s
def prefix(node):
    if node==None:#ไม่มี node
        return ""
    s=""
    s+=str(node.data)+prefix(node.left)+prefix(node.right)#preorder
    return s


postfix = input("Enter Postfix : ")

for i in range(len(postfix)):
    if postfix[i] in '+-*/':
        node1 = s.pop()
        node2 = s.pop()
        s.push(Node(postfix[i],node2,node1))
    else:
        s.push(Node(postfix[i]))

root = s.pop()

print("Tree :")
printTree(root)
print("--------------------------------------------------")
print("Infix :",infix(root))
print("Prefix :",prefix(root))

    
