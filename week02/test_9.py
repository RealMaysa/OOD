'''
สมมติว่านักศึกษาแอบชอบคนๆหนึ่งอยู่ โดยที่นักศึกษาและคนๆนั้นจะมีกิจกรรมและสถานที่ที่ไปแตกต่างกันในแต่ละวัน
ให้นักศึกษาเขียนโปรแกรมที่จะหาว่าสิ่งที่นักศึกษาและคนๆนั้นทำในแต่ละวันจะทำให้ได้คบกันหรือไม่ โดยใช้ Queue

กิจกรรม                                       สถานที่
0 = กินข้าว(Eat)                           0 = ร้านอาหาร(Res.)
1 = เล่นเกม(Game)                      1 = ห้องเรียน(ClassR.)
2 = ทำโจทย์ datastruc(Learn)      2 = ห้างสรรพสินค้า(SuperM.)
3 = ดูหนัง(Movie)                        3 = บ้าน(Home)

โดยการรับ Input จะประกอบด้วย

กิจกรรม:สถานที่(ของนักศึกษาและของคนๆนั้น) โดยในแต่ละวันจะคั่นด้วยเครื่องหมาย ,

เช่น วันที่ 1 นักศึกษาไปกินข้าวที่ร้านอาหาร และ คนๆนั้นไปนั่งทำโจทย์ datastruc ที่ร้านอาหาร 
       วันที่ 2 นักศึกษาไปเล่นเกมที่บ้าน และ คนๆนั้นไปดูหนังที่ห้างสรรพสินค้า
จะได้ว่า 0:0 2:0,1:3 3:2

***มีการคิดคะแนนดังนี้***

·       กิจกรรมเดียวกันแต่คนละสถานที่         +1

·       สถานที่เดียวกันแต่ทำกิจกรรมต่างกัน    +2

·       กิจกรรมเดียวกันและสถานที่เดียวกัน    +4

·       ไม่เหมือนกันเลย                                   - 5

หากมีคะแนนมากกว่าหรือเท่ากับ 7 จะถือว่าได้คบกัน แต่ถ้าคะแนนน้อยกว่า 7 แต่มากกว่า 0 เป็นคนคุย น้อยกว่านั้นถือว่าเป็นได้แค่เพื่อน

โดยในแต่ละขั้นตอนให้แสดงผลดังตัวอย่าง


'''



class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        if len(self.items)>0:
            return self.items.pop(0)
    def copy(self,i):
        self.items = i
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    

def encodemsg(q1, q2):
    enlist = []
    numlist = q2.items.copy()
    for i in range(q1.size()):
        temp = q1.deQueue()
        num = q2.deQueue()
        asci = ord(temp)
        if asci >= 65 and asci <= 90:
            if asci + int(num) > 90:
                asci = 65 + asci + int(num) - 91
                enlist.append(chr(asci))
            else:
                enlist.append(chr(asci + int(num)))
        elif asci >= 97 and asci <= 122:
            if asci + int(num) > 122:
                asci = 97 + asci + int(num) - 123
                enlist.append(chr(asci))
            else:
                enlist.append(chr(asci + int(num)))
        q2.enQueue(num)
    q1.copy(enlist)
    q2.copy(numlist)
    print("Encode message is :  "+str(q1.items))

def decodemsg(q1, q2):
    delist = []
    numlist = q2.items.copy()
    for i in range(q1.size()):
        temp = q1.deQueue()
        num = q2.deQueue()
        asci = ord(temp)
        if asci >= 65 and asci <= 90:
            if asci - int(num) < 65:
                asci = 90 - (65 - (asci - int(num))) + 1
                delist.append(chr(asci))
            else:
                delist.append(chr(asci - int(num)))
        elif asci >= 97 and asci <= 122:
            if asci - int(num) < 97:
                asci = 122 - (97 - (asci - int(num))) + 1
                delist.append(chr(asci))
            else:
                delist.append(chr(asci - int(num)))
        q2.enQueue(num)
    q1.copy(delist)
    q2.copy(numlist)
    print("Decode message is :  "+str(q1.items))

stri,num = input("Enter String and Code : ").split(',')
stri = stri.replace(" ","")
string = []
number = []
for i in range(len(stri)):
    string.append(stri[i])
for i in range(len(num)):
    number.append(num[i])
q1 = Queue(string)
q2 = Queue(number)
encodemsg(q1, q2)
decodemsg(q1, q2)