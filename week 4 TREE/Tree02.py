'''
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ และหาค่าที่น้อยและมากที่สุดของ Binary Search Tree

***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
      
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.min =0
        self.max=0
    def insert(self, data):
        if self.root == None :
            self.root = Node(data)
           
        else :
            now = self.root
            while now!=None : #ทำไปจนกว่าตัวชี้จะไปชี้Noneหรือก็คือตัวสุดท้ายแล้ว                
                if data < now.data :
                    if now.left == None :
                        now.left = Node(data)
                        break#ออกไปreturn root เลย
                    else :
                        now = now.left # ขยับตัวชี้ไป Node ซ้ายแล้ววนในลูปwhileอีกรอบ
                else :
                    if now.right == None :
                        now.right = Node(data)
                        break
                    else :
                        now = now.right
        return self.root
       
    def getMax(self):
        now =self.root
        while now.right!= None:
            now =now.right
        return now.data
    def getMin(self):
        node =self.root
        while node.left!= None:
            node = node.left
        return node.data


    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print("Min :",T.getMin())
print("Max :",T.getMax())