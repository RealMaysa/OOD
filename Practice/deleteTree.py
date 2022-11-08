class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root=None
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
    def delete(self,node,data):
        #ืไม่มี root
        if node==None:
            print("Error! Not Found DATA")
            return
        #ถ้าNodeที่ต้องการเป็นroot 
        elif self.root.left ==None and self.root.right==None and self.root.data==data:
            self.root=None
        elif self.root.left==None and self.root.data==data:
            self.root=self.root.right
        elif self.root.right==None and self.root.data==data:
            self.root=self.root.left
        #ถ้า Nodeที่ต้องการไม่ใช่root
        if node.data!=data:#ยังไม่เจอ
            if node.data>data:
                node.left = self.delete(node.left,data)
            else:
                node.right = self.delete(node.right,data)
        else:#เจอแล้ว
            if node.left==None:
                node=node.right
                return node
            elif node.right==None:
                node=node.left
                return node
            else:
                now=node.right
                while now.left!=None:
                    now=now.left
                node.data=now.data
                node.right=self.delete(node.right,now.data)
        return node
        
    def printTree(self,node,level=0):
        if node!=None:
            self.printTree(node.right,level+1)
            print('     '*level,node)
            self.printTree(node.left,level+1)
T=BST()
inp=input("Enter input : ").split(',')
for i in inp:
    command=i.split()
    if command[0]=='i':
        print("insert",command[1])
        T.insert(command[1])
        T.printTree(T.root)
    elif command[0]=='d':
        print("delete",command[1])
        T.delete(T.root,command[1])
        T.printTree(T.root)

