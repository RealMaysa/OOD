class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self):
        self.root=None
        self.n=0

    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            now=self.root
            while now!=None:
                if now.data>data:
                    if now.left==None:
                        now.left=Node(data)
                        break
                    else:
                        now=now.left
                else:
                    if now.right==None:
                        now.right=Node(data)
                        break
                    else:
                        now=now.right
        return self.root

    def getMin(self):
        now=self.root
        while now.left:
            now=now.left
        return now.data
    
    def getMax(self):
        now=self.root
        while now.right:
            now=now.right
        return now.data

    def less_than(self,node,val):
        if node==None:
            return ''
        s=""
        s+=self.less_than(node.left,val)
        if int(node.data)<=int(val):
            s+=str(node.data)+' '
            self.n+=1
        s+=self.less_than(node.right,val)
        return s
        

    def printTree(self,node,level=0):
        if node!=None:
            self.printTree(node.right,level+1)
            print('        '*level,node)
            self.printTree(node.left,level+1)
    def printInorder(self,node):
        if node:
            self.printInorder(node.left)
            print(str(node.data)+' ',end='')
            self.printInorder(node.right)
    def parent(self,node,val):
        if node.data==val:
            return "None because {} is root".format(val)
        if node.left ==None and node.right==None:
            return "Not Found Data"
        if (node.left!=None and node.left.data==val) or (node.right!=None and node.right.data==val):
            return node

        if  node.data>val:
            return self.parent(node.left,val)
        if node.data<val:
            return self.parent(node.right,val) 
    def delete(self,node,val):
        if self.root==None:
            print("Error")
            return 
        elif self.root.data==val and self.root.left==None and self.root.right==None:
            self.root=None
        elif self.root.data==val and self.root.left==None:
            self.root=self.root.right
        elif self.root.data==val and self.root.right==None:
            self.root=self.root.left
        
        if node.data!=val:
            if node.data>val:
                node.left=self.delete(node.left,val)
            else:
                node.right=self.delete(node.right,val)
        else:
            if node.left==None:
               node=node.right
               return node
            if node.right==None:
                node=node.left
                return node
            else:
                now=node.right
                while now.left!=None:
                    now=now.left
                node.data=now.data
                node.right=self.delete(node.right,node.data)
        return node 

T=BST()
inp=input("Enter input : ").split(',')
for i in inp:
    command=i.split()
    if command[0]=='i':
        print("insert",command[1])
        T.insert(command[1])
        T.printTree(T.root)
    if command[0]=='d':
        print("delete",command[1])
        T.delete(T.root,command[1])
        T.printTree(T.root)
    


'''  
T = BST()
inp,k=input('Enter Input : ').split('/')
inplist = [int(i) for i in inp.split()]
for i in inplist:
    root = T.insert(i)
T.printTree(root) 
print('--------------------------------------------')
print("Max :",T.getMax())
print("Min :",T.getMin())

if T.getMin()<int(k):
    print(T.less_than(root,int(k)))
else:
    print("Not have")

T.printInorder(root)
print('\n'+str(T.parent(root,int(k))))
'''

