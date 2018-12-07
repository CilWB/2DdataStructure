# Q2 : tree
# double value of the node
# that the value more than the "input"
# def doubleMore(r,val) : # r for root & val for input value  

class node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)

def insert(r,val):
    if r != None :
        if val < r.data :
            r.left = insert(r.left,val) 
        else:
            r.right = insert(r.right,val)
        return r
    else:
        return node(val)
        

def print90(r,level=0):
    if r != None :
        print90(r.right,level+1)
        print('   '*level,r)
        print90(r.left,level+1)


x = node(7)
l = [4,10,3,6,13,9]
print('your L = ',l)
print('the tree is')
for i in l :
    x = insert(x,i)
print90(x)
print('---------------------')

def rank(r,v):
    #print('visit',r)
    if r != None :
        l = rank(r.left,v)
        return l + ( (1 + rank(r.right,v)) if r.data<=v else 0)
    else:
        return 0

print(rank(x,9))


def rank2(r,v): # same with rank 
    #print('visit',r)
    if r != None :
        ch = 0
        l = rank2(r.left,v)
        if r.data <= v:
            ch = 1
        r = rank2(r.right,v)
        return l+r+ch
    return 0

print(rank2(x,-1))