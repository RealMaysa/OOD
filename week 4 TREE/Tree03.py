'''
ให้น้องรับ input เป็น list กับ k และจากนั้นให้สร้าง Binary Search Tree จาก list ที่รับเข้ามา และหาว่าใน Binary Search Tree นั้นมีกี่ Node ที่มีค่าน้อยกว่าหรือเท่ากับ k
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

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        node = self.root
        while True:
            if data < node.data:
                if node.left == None:
                    node.left = Node(data)
                    return self.root
                node = node.left
            else:
                if node.right == None:
                    node.right = Node(data)
                    return self.root
                node = node.right
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def less_than(self, node, data):#inorder แบบมีตัวนับ n ข้างใน ใช้Inorderเพราะมันเดินทางจากน้อยไปมาก
        if node == None: #สุดสายแล้ว
            return 0
            
        n=0 #กำหนด n เริ่มต้น
        n += self.less_than(node.left, data) #ไปทางซ้า่ย
        #จัดการกับข้อมูล
        if node.data <= data:#ถ้าเจอค่าที่น้อยกว่าหรือเท่ากับkให้บวก n เพิ่ม
            n += 1
        n += self.less_than(node.right, data)#ไปทางขวา
        return n

T = BST()
inp, k = input('Enter Input : ').split('/')
inp = [int(i) for i in inp.split()]
for i in inp:
        root = T.insert(i)
T.printTree(root)

print('--------------------------------------------------')
print(T.less_than(root, int(k)))