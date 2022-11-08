class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class Stack:
    def __init__(self,list=None):
        if list is None:
            self.items=[]
        else:
            self.items=list
    def pop(self):
        return self.items.pop()
    def push(self,data):
        return self.items.append(data)
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.size==0
def infix(node):
    if node==None:
        return ""
    s=""
    if node.left is not None and node.right is not None:
        s+='('
    s+=infix(node.left)+str(node.data)+infix(node.right)
    if node.left is not None and node.right is not None:
        s+=')'
    return s
def prefix(node):
    if node==None:
        return ""
    s=""
    s+=str(node.data)+prefix(node.left)+prefix(node.right)
    return s
def printTree(node,level=0):
    if node:
        printTree(node.right,level+1)
        print('       '*level,node)
        printTree(node.left,level+1)
s=Stack()

inp=input("Enter input : ")
for i in range(len(inp)):
    if inp[i]=='+-*/':
        node1=s.pop()
        node2=s.pop()
        s.push(Node(inp[i],node2,node1))
    else:
        s.push(Node(inp[i]))

root=s.pop()

printTree(root)




