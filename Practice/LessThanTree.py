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

    def lessThan(self,node,val):
        if node==None:
            return ''
        belowlist=''#เริ่มต้นสร้างlist
        #inoder LVR
        belowlist+=self.lessThan(node.left,val)
        if int(node.data) <= int(val):#จัดการกับข้อมูลที่อยู่ในNodeตามลำดับ
            self.n+=1
            belowlist += str(node.data) + ' '
        belowlist+=self.lessThan(node.right,val)
        return belowlist 

    def printTree(self,node,level=0):
        if node!=None:
            self.printTree(node.right,level+1)
            print('      '*level,node)
            self.printTree(node.left,level+1)
        
T=BST()
inp,k=input("Enter input : ").split('/')
inplist=[int(i) for i in inp.split()]
for i in inplist:
    root=T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
belowlist = T.lessThan(root,k)
if belowlist=='':
    print("Below {0} : Not have".format(str(k)))
    print(str(T.n))
else:
    print("Below {0} : {1}".format(str(k),belowlist))
    print(str(T.n))

    

                    

