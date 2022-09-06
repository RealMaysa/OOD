class Queue():
    def __init__(self,ls=None):
        if ls is None:
            self.items = []
        else:
            pass
    
    def enqueue(self, item):
            self.items.append(item)

    def dequeue(self):
        if(self.isEmpty() != True):
            return self.items.pop(0)

    def isEmpty(self):
        return self.items== []

    def peek(self):
        if(self.isEmpty() != True):
            return self.items[0]
    def size(self):
        return len(self.items)
    
class Stack() :

    items = []
    def __init__(self) :
        self.items = []
    def push(self,i) :  
        self.items.append(i)
    def pop(self) :  
        self.items.pop()
    def peek(self) :  
        return self.items[-1]
    def isEmpty(self)  : 
        if len(self.items)==0:
            return True
        else:
            return False
    def size(self) :
        return len(self.items)   

q= Queue()
n= Queue()
s= Stack()
InterruptedBomb =0
haveBomb = 0
mirror_count = 0
normal_count =0 
mirror_pop =[]
normal_pop =[]
normal,mirror = str(input("Enter Input (Normal, Mirror) : ")).split(" ")
mirror=mirror[::-1]
for i in mirror:
    mirror_pop.append(i)
for i in normal:
    normal_pop.append(i)
indx = 2
loopbreakMax = len(normal_pop)
while True:
    if len(mirror_pop) < 3 :
        break
    if mirror_pop[indx] == mirror_pop[indx-1] and mirror_pop[indx] == mirror_pop[indx-2] :
        q.enqueue(mirror_pop[indx])
        mirror_pop.pop(indx-2)
        mirror_pop.pop(indx-2)
        mirror_pop.pop(indx-2)
        haveBomb += 1
    else:
        indx+=1
        haveBomb -=1
    if len(mirror_pop) ==0 or haveBomb < -len(mirror_pop):
        break
    if indx == len(mirror_pop) or indx > len(mirror_pop):
        indx =2
mirror_count = len(q.items)
indx = 2
haveBomb=0
while True:
    if len(normal_pop) < 3 :
        break
    if normal_pop[indx] == normal_pop[indx-1] and normal_pop[indx] == normal_pop[indx-2] and not q.isEmpty() :
        normal_pop.insert(indx,q.dequeue())
        if normal_pop[indx] == normal_pop[indx-1] and normal_pop[indx] == normal_pop[indx-2] :
            n.enqueue(normal_pop[indx])
            normal_pop.pop(indx-2)
            normal_pop.pop(indx-2)
            normal_pop.pop(indx-2)
            haveBomb += 1
            InterruptedBomb+=1
            continue
    if normal_pop[indx] == normal_pop[indx-1] and normal_pop[indx] == normal_pop[indx-2] :
            n.enqueue(normal_pop[indx])
            normal_pop.pop(indx-2)
            normal_pop.pop(indx-2)
            normal_pop.pop(indx-2)
            haveBomb += 1
    else:
        indx+=1
        haveBomb -=1
    if len(normal_pop) ==0 or haveBomb < -len(normal_pop)*2:
        break
    if indx == len(normal_pop) or indx > len(normal_pop):
        indx =2
normal_count = len(n.items)
print("NORMAL :")
print(len(normal_pop))
if len(normal_pop) > 0:
    print(''.join(reversed(normal_pop)))
else :
    print("Empty")
print("{} Explosive(s) ! ! ! (NORMAL)".format(len(n.items)-InterruptedBomb))
if InterruptedBomb > 0:
    print("Failed Interrupted {} Bomb(s)".format(InterruptedBomb))
print("------------MIRROR------------")
print(": RORRIM")
print(len(mirror_pop))
if len(mirror_pop) > 0:
    print(''.join(reversed(mirror_pop)))
else :
    print("ytpmE")
print("(RORRIM) ! ! ! (s)evisolpxE {}".format(mirror_count))
