'''ให้น้องๆใช้ Linked List (เขียนเป็น class)  ในการทำ Radix Sort  (มีอยู่ในสไลด์เรียน 2 หน้าสุดท้าย)  ในรูปแบบมากไปน้อย

โดยผลลัพธ์ให้ออกมาเป็นการทำ Radix Sort แบบจำนวนรอบน้อยที่สุด และแสดงผลในแต่ละรอบว่าได้ผลลัพธ์เป็นอย่างไร  3 บรรทัดสุดท้ายจะเป็น ( จำนวนรอบที่น้อยที่สุด , Data ก่อนทำ Radix Sort และ Data หลังทำ Radix Sort )

'''

class SinglyLinkedListNoDummy :     
    class Node :                    
        def __init__(self, data, next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.head = None
            self.tail = None
            self.size = 0
            
    def __str__(self):                
        s = ''
        p = self.head
        while p != None :
            if p.next !=None :
                s += str(p.data) + " -> "
            else :
                s += str(p.data)
            p = p.next
        return s
          
    def __len__(self) :               
        return self.size         
            
    def isEmpty(self) :              
        return self.size == 0         
        
    def indexOf(self,data) :          
        p = self.head
        for i in range(len(self)) :
            if p.data == data :
                return i
            p = p.next
        return -1
            
    def isIn(self,data) :            
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :             
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p
    
    def append(self,data):          
        if self.head is None :
          p = self.Node(data)
          self.head = p
          self.tail = p
          self.size += 1
        else :                        
          self.addTail(data)
          
    
    def insertAfter(self,i,data) :       
        q = self.nodeAt(i)
        p = self.Node(data)
        p.next = q.next
        q.next = p
        self.size += 1
    
    def addTail(self,data) :
        q = self.tail
        p = self.Node(data)
        q.next = p
        self.tail = p
        self.size += 1

    def removeTail(self) :
        if self.size > 0 :
          q = self.nodeAt(len(self)-2)
          self.tail = q
          q.next = None
          self.size -= 1

    def deleteAfter(self,i) :           
        if self.size > 0 : 
          q = self.nodeAt(i)  
          q.next = q.next.next
          self.size -= 1
    
    def delete(self,i) :                
        if self.size > 0 :
          if i == 0 :    
            self.head = self.head.next
            self.size -= 1
          elif i == len(self) - 1 :
            self.removeTail()
          else :
            self.deleteAfter(i-1)      
        
    def removeData(self,data) :         
        if self.isIn(data) :
            self.deleteAfter(self.indexOf(data)-1)
          
    def addHead(self,data) :
        if self.isEmpty() :
          p = self.Node(data)
          self.head = p
          self.size += 1
        else :
          p = self.Node(data,self.head)
          self.head = p
          self.size += 1
    
maxDigit = 0
maxDigitNev =0
currentDigit = 0
digitcap = 0
maxVal =0
minVal = 0
radix = input("Enter Input : ").split(" ")
L = SinglyLinkedListNoDummy()
nL = SinglyLinkedListNoDummy()
#เริ่มจาก หาจำนวนหลักที่มากที่สุด โดยใช้การค่าหาจำนวนเลขที่มากที่สุดแล้วเก็บค่าความยาวไว้ 
for e in radix :
    currentDigit = int(e)
    if maxVal < currentDigit and currentDigit >=0:
        maxVal = currentDigit
        maxDigit = len(str(currentDigit)) #จำนวนหลักของMaxVal
    elif minVal > currentDigit and currentDigit < 0 : #กรณีเป็นเลขติดลบ
        minVal = currentDigit
        maxDigitNev = len(str(currentDigit))-1 #-1 เพราะไม่นับความยาวของเครื่องหมายลบ
    #หลุดจาก if กับ elif ตอนต้นแล้วมาเช็คกับ if else ข้างล่างนี้
    #สร้าง SinglyLinkList จาก List ของ radix ที่รับเข้ามา ถ้าเป็นจำนวนเต็มบวกเก็บในL จำนวนเต็มลบเก็บใน nL
    if int(e) >= 0:
            L.append(str(e))
    else :
            nL.append(str(e)[1:]) #ใส่ค่าตั้งแต่ตัวที่ 1 ไปยังตัวสุดท้าย

#กรณีตัวเลขจากmaxdigitที่ติดลบมีจำนวนหลักมากกว่าจำนวนที่ไม่ติดลบ
if maxDigitNev >= maxDigit:
    digitcap = maxDigitNev
else :
    digitcap = maxDigit

beforeRadix = " -> ".join(radix)
digit = -1
indx= 0
digitList = [SinglyLinkedListNoDummy() for e in range(maxDigit+1)] #Listที่สร้าง SinglyLinkedList ตามจำนวนตั้งแต่0 จนถึง maxDigit+1 ตามจำนวนหลัก
while indx < maxDigit+1 : #ทำตามจำนวนหลัก สมมุติ หลักที่มากสุดเป็น 3 จะทำการวน 3 รอบ 0->1->2->3
    if indx != 0: #ตรวจสอบหลักถัดไป
        for i in reversed(range(10)) :
            headDigit = digitList[indx-1].head
            while headDigit != None:
                if len(str(headDigit.data)) < -digit and i == 0: #จำนวนหลักน้อยกว่า
                            digitList[indx].append(headDigit.data) 
                elif len(str(headDigit.data)) >= -digit:
                    if i == int(str(headDigit.data)[digit]):
                            digitList[indx].append(headDigit.data)
                headDigit = headDigit.next
    else : #ตรวจสอบหลักหน่วยของNodeใน L
        for i in reversed(range(10)) : #ใช้reverseเนื่องจากเราจะ sort จากมากไปน้อย
            headDigit = L.head
            #i จะไม่เพิ่มขึ้นจนกว่าข้อมูลใน L จะถูกเช็คโดยตัวเงื่อนไข ด้านล่าง ครบทั้งหมดแล้ว
            while headDigit != None:
                if i == int(str(headDigit.data)[digit]) : # เช็คดูหลักหน่วยของค่าใน L.head ว่าตรงกับiตามจำนวนรอบมั้ย? 
                        digitList[indx].append(headDigit.data) 
                headDigit = headDigit.next #เลื่อนheadDigit ไป Node ตัวถัดไป ใน L
    indx+=1 #เป็นรอบของการวนซ้ำ 0-4
    digit-=1 #หลักที่ต้องการจะตรวจสอบ หน่วย สิบ ร้อย พัน
#ทำเหมือนกันมีดัดแปลงนิดหน่อย
digit = -1
indx=0
digitListNev = [SinglyLinkedListNoDummy() for e in range(maxDigitNev+1)]
while indx < maxDigitNev+1 :
    if indx != 0:
        for i in range(10) : #ไม่ใช้reverseเนื่องจากเราจะ sort จากน้อยไปมาก
            headDigit = digitListNev[indx-1].head
            while headDigit != None:
                if len(str(headDigit.data)) < -digit and i == 0:
                        digitListNev[indx].append(headDigit.data)
                elif len(str(headDigit.data)) >= -digit:
                    if i == int(str(headDigit.data)[digit]):
                        digitListNev[indx].append(headDigit.data)
                headDigit = headDigit.next
    else :             
        for i in range(10) :
            headDigit = nL.head
            while headDigit != None:
                if i == int(str(headDigit.data)[digit]) :
                    digitListNev[indx].append(headDigit.data)
                headDigit = headDigit.next
    indx+=1
    digit-=1 #อย่าลืมบวกลบส่วนท้าย!!

radix_sort = SinglyLinkedListNoDummy()
radix_sort_display = SinglyLinkedListNoDummy()
posNum = digitList[-1].head
nevNum = digitListNev[-1].head
#กรณีที่มีทั้งค่าลบและค่าบวกปนกัน
while nevNum != None: 
        if posNum == None:
            radix_sort.append(nevNum.data)
            radix_sort_display.append(int("-"+str(nevNum.data)))
            nevNum = nevNum.next
        else:
            radix_sort.append(posNum.data)
            radix_sort_display.append(int(posNum.data))
            posNum = posNum.next
#กรณีมีค่าบวกอย่างเดียว
while posNum!=None:
            radix_sort.append(posNum.data)
            radix_sort_display.append(int(posNum.data))
            posNum = posNum.next
check = 0
count = 1
stop = False
exp = 1
print("------------------------------------------------------------")
while not stop :
    print("Round : "+str(count))
    for i in range(10):
        display = radix_sort_display.head
        print(str(i)+" :",end=" ")
        while display != None:
            if  i == ((-display.data//exp)%10) and display.data < 0:
                print(display.data,end=" ")
                if i==0:
                    check+=1
            elif i == ((display.data//exp)%10) and display.data >= 0:
                print(display.data,end=" ")
                if i==0:
                    check+=1
            display = display.next
        print("")
    count +=1
    if check == radix_sort_display.size :
        stop = True
    check=0
    if len(str(exp)) > digitcap :
        stop = True
    exp *= 10
    print("------------------------------------------------------------")

print(str(count-2)+" Time(s)")
print("Before Radix Sort : ",end="")
print(beforeRadix)
print("After  Radix Sort : ",end="")
print(radix_sort_display)