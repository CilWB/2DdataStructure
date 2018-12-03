# problem #1 
# queue q = [1,2,3,4,5]
# q = mirror(q)
# result q = [1,2,3,4,5,5,4,3,2,1]
# *** use only stack and queue method ***

# start 4:32 PM
# 9/21/2018
# by CXZ

class stack:
    def __init__(self):
        self.items = []
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return None if self.isEmpty() else self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def __str__(self):
        return 'stack -> ' + str(self.items)
    
class queue:
    def __init__(self,l=[]):
        self.items = l
    def enQ(self,data):
        self.items.append(data)
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
    def deQ(self):
        return None if self.isEmpty() else self.items.pop(0)
    def __str__(self):
        return 'queue -> ' + str (self.items)

def mirror(q):
    s = stack()
    for i in range(q.size()):
        t = q.deQ()
        q.enQ(t)
        s.push(t)
    while not s.isEmpty():
        q.enQ(s.pop())
    return q

#################### FIX comand ####################   

q = queue( [c for c in input().split()])
print(q)
q  = mirror(q)
print(q)

####################################################

# finish 4:50 PM
# 9/21/2018