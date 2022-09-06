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