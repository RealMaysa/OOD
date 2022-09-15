'''
จงเขียนฟังก์ชั่นสำหรับการ Merge LinkList 2 ตัวเข้าด้วยกันโดยห้ามสร้าง Class LinkList จะมีแต่ Class Node ซึ่งเก็บค่า value ของตัวเองและ Node ถัดไป โดยมีฟังก์ชั่นดังนี้

createList() สำหรับการสร้าง LinkList ที่รับ List เข้ามาโดยจะ return Head ของ Linklist

printList() สำหรับการ print LinkList โดยจะรับค่าเป็น head ของ Linklist และจะทำการ print ทุกตัวที่อยู่ใน Linklist ต่อจาก head จนครบทุกตัว

mergeOrderList() สำหรับการ merge linklist 2 ตัวเข้าด้วยกันโดยให้นำมาต่อกันโดยเรียงตามค่า value โดยที่ให้รับ parameter 2 ตัว และจะ return Head ของ Linklist ที่ทำการ merge แล้ว

****ห้ามใช้ sort() หากพบข้อนี้จะไม่ได้คะแนน****

****ห้ามสร้าง Class LinkList****

class node:
    def __init__(self,data,next = None ):
        ### Code Here ###
    def __str__(self):
        ### Code Here ###

def createList(l=[]):
    ### Code Here ###

def printList(H):
    ### Code Here ###

def mergeOrderesList(p,q):
    ### Code Here ###

#################### FIX comand ####################   
# input only a number save in L1,L2
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)
'''
class node:
    def __init__(self,data,next = None ):
        self.data = data
        if next is None :
            self.next = None
        else :
            self.next = next

    def __str__(self):
        return str(self.data)

def createList(l=[]):
    #การสร้างlinkedlist จาก list
    head = node(l[0])       #สร้างnodeแรกที่เก็บdataจาก list ในindex 0
    temp = head             #เริ่มจากเอาtempชี้headไว้
    for i in range(1,len(l)):#เริ่มสร้างnodeเก็บข้อมูลจากlist ในindexตำแหน่งอื่นๆที่เหลือ
        nxt = node(l[i])     
        temp.next = nxt     #ให้next ของtempชี้ที่nxt(ต่อnxtเข้ากับtemp)  
        temp = temp.next    #เลื่อนtempไปชี้อันถัดไป
    return head

def printList(H):
    temp = H
    while temp!=None:
        print(str(temp),end=" ")
        temp = temp.next
    print()

def mergeOrderesList(p,q):
    #ดูว่าค่าในไหนมากกว่า
    if int(p.data) < int(q.data):#ค่า head ของp มากกว่า ของq
        temp = p #temp ชี้ p
        #สร้างnextNode 2 ตัว
        nextNodeP = p.next  #ให้ Node ต่อไปที่จะเช็คใน p เป็น ตัวต่อไปของ p ได้เลย เนื่องจากเงื่อนไขifนี้ headของ p น้อยกว่าและถูกtempชี้อยู่แล้ว
        nextNodeQ = q #ให้ Node ต่อไปที่จะเช็คใน q ยังเป็น headของ qอยู่ เนื่องจาก เงื่อนไขifนี้ headของ q มากกว่า และไม่ได้โดนtempชี้
    else:#กรณีdataในheadของqน้อยกว่า
        temp = q
        nextNodeP = p
        nextNodeQ = q.next
    head = temp #้headเป็น Nodetemp เพื่อเริ่มต้น การ Merge
    while nextNodeP != None or nextNodeQ != None: #ให้ทำในลูปจนกว่าจะไม่มีNodeตัวต่อไปของpหรือqอย่างใดอย่างหนึ่ง
        #กรณีแรก nextNodeP และ nextNodeQ มีค่า
        if nextNodeP != None and nextNodeQ != None:
            if int(nextNodeP.data) < int(nextNodeQ.data):
                temp.next = nextNodeP #เอา nextNodeP เป็นตัวถัดไปของ temp
                temp = temp.next #เอา temp ไปชี้ ตัวถัดไปของ temp 
                nextNodeP = nextNodeP.next #สร้าง nextNodeP อันใหม่ที่เป็นอันถัดไป 
            else:
                temp.next = nextNodeQ #เอา nextNodeQ เป็นตัวถัดไปของtemp
                temp = temp.next #เอา temp ไปชี้ ตัวถัดไปของ temp นั้น
                nextNodeQ = nextNodeQ.next #สร้าง nextNodeQ อันใหม่ที่เป็นอันถัดไป

        #กรณีแรก nextNodeP มีค่า
        elif nextNodeP != None:
            temp.next = nextNodeP
            temp = temp.next
            nextNodeP = nextNodeP.next
        #กรณีแรก nextNodeQ มีค่า
        elif nextNodeQ != None:
            temp.next = nextNodeQ
            temp = temp.next
            nextNodeQ = nextNodeQ.next
    return head

list1,list2 = input("Enter 2 Lists : ").split()
L1 = list1.split(",")
L2 = list2.split(",")
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)