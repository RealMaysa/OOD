'''
นักศึกษาจะได้รับ Input เป็น list<int> ของดาวเคราะห์น้อย
สำหรับดาวเคราะห์น้อยแต่ละดวงนั้น ค่าสัมบูรณ์ จะแสดงขนาดของมัน และเครื่องหมายแสดงถึงทิศทางของมัน (ถ้าเลขเป็นบวกแสดงว่าวิ่งไปทางขวา ,ลบทางซ้าย) โดยที่ดาวเคราะห์น้อยแต่ละดวงเคลื่อนที่ด้วยความเร็วเท่ากัน

ค้นหาสถานะของดาวเคราะห์น้อยหลังจากการชนกันทั้งหมด

1.หากดาวเคราะห์น้อยสองดวงมาพบกันดวงที่เล็กกว่าจะระเบิด

2.ถ้าทั้งสองมีขนาดเท่ากันทั้งคู่จะระเบิด

3.ดาวเคราะห์น้อยสองดวงที่เคลื่อนที่ไปในทิศทางเดียวกันจะไม่มีวันพบกัน

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

def asteroid_collision(asts):
    #Code Here

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))
'''
def asteroid_collision(asts):

    list = []

    def collisionCheck(list,asts) :
            if not list :
                list.append(asts)
            elif asts < 0 and list[-1] > 0 :
                if asts + list[-1] == 0 :
                    list.pop()
                elif asts + list[-1] < 0 :
                    list.pop()
                    collisionCheck(list, asts)
            else:
                list.append(asts)

    def recursiveLoop (i,asts) :
      
        if i != len(asts) :
        
            collisionCheck(list,asts[i]) 
            recursiveLoop(i+1,asts)

    recursiveLoop(0,asts)

    return list

x = input("Enter Input : ").split(",")
x = list(map(int,x))

print(asteroid_collision(x))