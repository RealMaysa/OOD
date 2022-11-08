'''
จงเขียนฟังก์ชั่นสำหรับการ insert แบบ Binary Search Tree (BST) โดยที่ input ตัวแรกจะเป็น root เสมอและจงเขียนฟังก์ชั่นสำหรับการหาค่าที่ใกล้เคียง input ที่รับเข้ามาที่สุดที่อยู่ใน BST ที่ทำการ insert ครบแล้ว

รูปแบบการรับ input จะแบ่งโดย '/'

1.ชุดของ BST ที่จะทำการ insert โดยตัวแรกจะเป็น root เสมอ

2.ค่าที่จะนำมาเปรียบเทียบกับค่าใน BST ที่ทำการ insert แล้ว

รูปแบบ output 

จะ printTree ทุกครั้งที่มีการ insert ค่าเข้าและเมื่อทำการ insert จบจะเรียกใช้ฟังก์ชั่น closestValue(root,value) และแสดงค่าที่ใกล้เคียงที่สุดจาก BST 

*** ถ้าหากค่าที่รับเข้ามาเทียบมีอยู่ใน BST ให้ return ค่านั้นออกมาได้เลย และหากมีค่าที่อยู่ใกล้มากกว่า 1 จำนวนให้แสดงจำนวนที่มากที่สุดที่อยู่ใกล้ค่านั้น ***


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
        if self.root == None :
            self.root = Node(data)
        else :
            now = self.root
            while True :
                if data < now.data :
                    if now.left == None :
                        now.left = Node(data)
                        break
                    else :
                        now = now.left
                else :
                    if now.right == None :
                        now.right = Node(data)
                        break
                    else :
                        now = now.right
        return self.root

    def searchNearest(self,data) :
        now = self.root
        data = int(data)
        minDiff = abs(now.data-data)
        ans = now.data

        while now :
            if now.right != None and now.left != None :
                diffRight = abs(now.right.data-data)
                diffLeft = abs(now.left.data-data)

                if diffRight < diffLeft :
                    if diffRight < minDiff :
                        minDiff = diffRight
                    now = now.right
                else :
                    if diffLeft < minDiff :
                        minDiff = diffLeft
                    now = now.left

            elif now.right != None and now.left == None :
                diff = abs(now.right.data-data)
                if diff < minDiff :
                    minDiff = diff
                now = now.right
            elif now.left != None and now.right == None :
                diff = abs(now.left.data-data)
                if diff < minDiff :
                    minDiff = diff
                now = now.left
            else :
                break
            
            if now.data > ans and abs(now.data-data) == abs(ans-data) :
                ans = now.data
            elif abs(now.data-data) < abs(ans-data) :
                ans = now.data

        return "Closest value of " + str(data) + " : " + str(ans)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp,goal = input('Enter Input : ').split("/")
inp = [int(i) for i in inp.split()]
goal = int(goal)
diff = []

for i in inp:
    root = T.insert(i)
    T.printTree(root)
    print("--------------------------------------------------")

print(T.searchNearest(goal))