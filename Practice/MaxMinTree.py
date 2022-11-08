class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            if self.root.data == data:
                print("This information is a duplicate of what already exists.")
                return
            now=self.root
            while now!=None:
                if data<now.data:
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
    def printInorder(self,node):
         if node!=None:
            self.printInorder(node.left)
            print(node.data,end =' ')
            self.printInorder(node.right)
    
    def getMax(self):
        now=self.root
        while now.right!=None:
            now=now.right
        return now.data
    def getMin(self):
        now=self.root
        while now.left!=None:
            now=now.left
        return now.data

    def printTree(self,node,level=0):
        if node!=None:
            self.printTree(node.right,level+1)
            print('     '*level,node)
            self.printTree(node.left,level+1)
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root) #เอาrootเข้าไป
print('--------------------------------------------------')
T.printInorder(root)
print("Min :",T.getMin())
print("Max : ",T.getMax())

                
        