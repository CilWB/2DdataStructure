# problem #2 
# Linklist LL1 and LL2 is a increased ordered input
# LL1 = 1->2->3->5->5->8->11
# LL2 = 2->6->7->9->10
# m = mergeOrderesList(LL1,LL2)
# result m = 1->2->2->3->5->5->6->7->8->9->10->11
#  **** DO NOT IMPLEMENT LINKLIST CLASS ***
# *** CAN USE ONLY NODE CLASS(data,next) ***

# start 4:59 PM
# 9/21/2018
# by CXZ

class node:
    def __init__(self,data,next = None ):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    if l == [] :
        return node(None)
    else:
        h = node(l[0])
        t = h 
        for i in range(1,len(l)):
            t.next = node(l[i])
            t = t.next
        return h
def printList(L):
    s = ''
    tt = L
    while tt != None :
        #print(tt)
        s += str(tt) +' '
        tt = tt.next
    print(s)

def mergeOrderesList(p,q):
    h = p if p.data < q.data else q
    t_p = p.next if p.data < q.data else p
    t_q = q if p.data < q.data else q.next
    #print(h)
    #print(t_p,t_q)
    #print(t_p.next,t_q.next)
    t = h
    while t_p != None and t_q != None :
        if t_p.data < t_q.data :
            t.next = t_p
            t_p = t_p.next
        else:
            t.next = t_q
            t_q = t_q.next
        t = t.next
    #printList(h)
    if t_p == None:
        t.next = t_q
    else:
        t.next = t_p
    return h

#################### FIX comand ####################   
# input only a number 
L1 = [1,3,5,7,10,20,22]
L2 = [4,6,7,8,15]
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 -> ',end='')
printList(LL1)
print('LL2 -> ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2) # can swap LL1 and LL2 to check the result it's should be the same
print('mrg -> ',end='')
printList(m)
print('LL1 -> ',end='')
printList(LL1)
print('LL2 -> ',end='')
printList(LL2)

# and now
# i'm so very lazy and hungry now ;(
####################################################


# finish 5:32 PM
# 9/21/2018