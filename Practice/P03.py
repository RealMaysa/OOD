class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self):
        self.root=None
        self.n=0
    def insert(self,val):
        #ยังไม่มีroot
        if self.root==None:
            self.root=Node(val)
        #มี root
        else:
            now=self.root
            while now:
         #น้อยกว่าหรือมากกว่า
                if now.data>val:
                    #มีnodeรึยัง
                    if now.left==None:
                        now.left=Node(val)
                        break
                    else:
                        now=now.left
                else:
                    if now.right==None:
                        now.right=Node(val)
                        break
                    else:
                        now=now.right
        return self.root
        #return root

    def getMin(self):
        now=self.root
        while now.left!=None:
            now=now.left
        return now.data
    def getMax(self):
        now=self.root
        while now.right!=None:
            now=now.right
        return now.data
    def less_than(self,node,val):
        if node==None:
            return ""
        s=""
        s+=self.less_than(node.left,val)
        if node.data <= val:
            s+=str(node.data)+' '
        s+=self.less_than(node.right,val)
        return s
    def parents(self,node,data):
        #โหนดที่ต้องการหาคือรูท
        if self.root.data==data:
            return "None Because {0} is root".format(str(data))
        #โหนดที่ต้องการหาอยู่ติดกับรูท
            #ไม่มีซ้ายขวา
        if self.root.data==data and node.left==None and node.right==None :
            return "not found Data"
            #มีโหนดด้านซ้ายขวา
        if (node.left is not None and node.left.data==data) or (node.right is not None and node.right.data==data) :
            return node
        if node.data>data:
            return self.parents(node.left,data)
        if node.data<data:
            return self.parents(node.right,data)
    def printTree(self,node,level=0):
        if node:
            self.printTree(node.right,level+1)
            print('        '*level,node)
            self.printTree(node.left,level+1)
    def delete(self,node,val):
        #root is None
        #print("Error")
        #return 
        #delete root 
            #left and right not have
            #left not have
            # - move right
            #right not have
            # - move left 
        #not delete root
            # not found
                #> or <= move by delete 
            #found
                #left not have 
                # - move right return node
                #right not have
                # - move left retutn node
                #Inorder successor
                  #start right
                  #while left
                  #pick data
                  #found right by node.right and data
        if self.root==None:
            print("Error")
            return
        elif self.root.data ==val and self.root.left==None and self.root.right== None:
            self.root=None
        elif self.root.data==val and self.root.left==None:
            self.root=self.right
        elif self.root.data==val and self.root.right==None:
            self.root=self.left

        else:    
            if node.data!=val:
                if node.data>val:
                    node.left=self.delete(node.left,val)
                else:
                    node.right=self.delete(node.right,val)
            else:
                if node.left==None:
                    node=node.right
                    return node
                if node.right==None:
                    node= node.left
                    return node
                else:
                    now=node.right
                    while now.left!=None:
                        now=now.left
                    node.data=now.data
                    node.right=self.delete(node.right,node.data)
        return node
    