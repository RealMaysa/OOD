'''
จงเขียน ฟังก์ชั่นสำหรับการ encode และ decode ของ String ที่รับมาโดยให้ทำเป็นรูปแบบ Queue

รูปแบบการรับ Input โดยจะคั่นแต่ละตำแหน่งด้วย คอมม่า(',') :

    - ตำแหน่งที่หนึ่ง string ไม่จำกัดความยาวโดยที่จะไม่นับช่องว่าง(spacebar)

    - ตำแหน่งที่สอง ชุดตัวเลข(1-9)

โดยที่รูปแบบการ encode คือ การนำ String ที่รับมาเพิ่มค่า ascii เท่ากับค่าของชุดตัวเลขในตำแหน่งแรก หลังจากนั้นให้ dequeue ชุดตัวเลขออกไปไว้ข้างหลังสุด เช่น ตัวอักษรตำแหน่งแรกคือ i และชุดตัวเลขในตำแหน่งแรกคือ 2 ดังนั้นตัวอักษรที่ได้จากการ encode คือ k โดยจะทำการวนชุดตัวเลขไปเรื่อยๆจนกระทั่งทำการ encode ทุกตัวอักษรใน String ครบ ถ้าหากผลลัพธ์จากการเพิ่มหรือลดค่า ascii ไม่ใช่ตัวอักษรให้กลับมาวนในชุดตัวอักษร เช่น อักษร z ทำการ encode ด้วยเลข 2 จะได้ b และหากทำการ decode ตัวอักษร A ด้วย 2 จะได้ Y 

โดยการ decode หลังจาก encode ต้องให้คำตอบที่มีค่าเท่ากับ String เดิมก่อนทำการ encode 

***ให้ใช้วิธี enqueue และ dequeue ในการเลื่อนตำแหน่ง เท่านั้น***

โดยรูปแบบการ run ดังนี้ :

q1 = Queue(string)

q2 = Queue(number)

encodemsg(q1, q2)

decodemsg(q1, q2)


'''


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
            self.queue.append(item)

    def dequeue(self):
        if(self.isEmpty() != True):
            return self.queue.pop(0)

    def isEmpty(self):
        return self.queue == []

    def peek(self):
        if(self.isEmpty() != True):
            return self.queue[0]
    def size(self):
        return len(self.queue)
score=0
me = Queue()
you = Queue()
me_str =[]
you_str =[]
me_list =[]
you_list =[]
inn = str(input("Enter Input : ")).split(",")
for i in inn:
    me_str,you_str = i.split(" ")
    me_list.append(me_str)
    you_list.append(you_str)
    me.enqueue(me_str)
    you.enqueue(you_str)
print("My   Queue = ",end="")
for i in range(len(me_list)):
    print(me_list[i],end="")
    if i != len(me_list)-1:
        print(", ",end="")
print("")
print("Your Queue = ",end="")
for i in range(len(you_list)):
    print(you_list[i],end="")
    if i != len(you_list)-1:
        print(", ",end="")
print("")
print("My   Activity:Location = ",end="")
for i in range(len(me_list)):
    ac_me,loc_me=str(me_list[i]).split(":")
    if ac_me == "0":
        print("Eat:",end="")
    elif ac_me == "1":
        print("Game:",end="")
    elif ac_me == "2":
        print("Learn:",end="")
    elif ac_me == "3":
        print("Movie:",end="")
    if loc_me == "0":
        print("Res.",end="")
    elif loc_me == "1":
        print("ClassR.",end="")
    elif loc_me == "2":
        print("SuperM.",end="")
    elif loc_me == "3":
        print("Home",end="")
    if i != len(me_list)-1:
        print(", ",end="")
    else :
        print("")
print("Your Activity:Location = ",end="")
for i in range(len(me_list)):
    ac_you,loc_you=str(you_list[i]).split(":")
    if ac_you == "0":
        print("Eat:",end="")
    elif ac_you == "1":
        print("Game:",end="")
    elif ac_you == "2":
        print("Learn:",end="")
    elif ac_you == "3":
        print("Movie:",end="")
    if loc_you == "0":
        print("Res.",end="")
    elif loc_you == "1":
        print("ClassR.",end="")
    elif loc_you == "2":
        print("SuperM.",end="")
    elif loc_you == "3":
        print("Home",end="")
    if i != len(you_list)-1:
        print(", ",end="")
    else :
        print("")

    
while me.isEmpty() != True and you.isEmpty() != True:
    ac_me,loc_me=str(me.peek()).split(":")
    ac_you,loc_you=str(you.peek()).split(":")
    if ac_me == ac_you and loc_me!=loc_you:
        score+=1
    elif ac_me != ac_you and loc_me==loc_you:
        score+=2
    elif ac_me == ac_you and loc_me==loc_you:
        score+=4
    elif ac_me != ac_you and loc_me!=loc_you:
        score-=5
    me.dequeue()
    you.dequeue()
if score >= 7:
    print("Yes! You're my love! : Score is {}.".format(score))
elif score <7 and score >0:
    print("Umm.. It's complicated relationship! : Score is {}.".format(score))
elif score <= 0:
    print("No! We're just friends. : Score is {}.".format(score))