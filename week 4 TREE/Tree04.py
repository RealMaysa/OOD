'''
ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

โดยมีการป้อน input ดังนี้

i <int> = insert data

d <int> = delete data

หมายเหตุ การลบนั้นจะใช้หลักการของ Inorder Successor และ จำนวน parameter มีได้มากสุด 3 ตัว


'''

class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            cur = self.root
            while True:
                if val < cur.data:
                    if cur.left == None:
                        cur.left = Node(val)
                        break
                    else:
                        cur = cur.left
                elif val > cur.data:
                    if cur.right == None:
                        cur.right = Node(val)
                        break
                    else:
                        cur = cur.right
                else:
                    break
        return self.root

    def delete(self,r, data):
        if r is None:
            print("Error! Not Found DATA")
            return
            #เช็ค self.rootครั้งแรกและครั้งเดียว
        elif self.root.left == None and self.root.right == None and self.root.data == data: #ถ้าไม่มีทั้งซ้ายและขวาให้ไปแล้วต้องการลบrootก็ให้rootเป็นNone
            self.root = None
        elif self.root.left == None and self.root.data == data:#ถ้าไม่มีซ้ายก็เลื่อนไปขวา 
            self.root = self.root.right
        elif self.root.right == None and self.root.data == data:#ถ้าไม่มีขวาก็เลื่อนไปซ้าย 
            self.root = self.root.left

        if r.data != data: #ถ้ายังไม่เจอ nodeที่ต้องการลบ
            if r.data > data:
                r.left = self.delete(r.left,data)#ไปซ้าย
            else:
                r.right = self.delete(r.right,data)#ไปขวา

        else:#หาเจอแล้ว
            if r.left is None: # left none
                r = r.right
                return r
            elif r.right is None: #right none
                r = r.left
                return r
            else: 
                #inorder successor
                now = r.right #เริ่มจากขวา
                while now.left != None: #ไปทางซ้ายเรื่อยๆ
                    now = now.left 
                r.data = now.data #ถึงสุดซ้ายแล้วเอาdataจากNodeนี้
                r.right = self.delete(r.right,now.data) #ไปซ็ายด้วยdataใหม่จากเมื่อกี้
        return r

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for i in data:
    command = i.split(" ")
    if command[0] == 'i':
        print("insert "+(command[1]))
        tree.insert(int(command[1]))
        printTree90(tree.root)
    elif command[0] == 'd':
        print("delete "+(command[1]))
        tree.delete(tree.root,int(command[1]))
        printTree90(tree.root)
