# problem #2 
# Linklist LL = 5->5->2->3->0->3->4->4->7->7->5->4->8->9
# p = delRepeat(LL)
# result p = 2->0->8->9
#  **** DO NOT IMPLEMENT LINKLIST CLASS ***
# *** CAN USE ONLY NODE CLASS(data,next) ***

# start 2:47 AM
# 9/22/2018
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


######################################################
def delRepeat(L):
    #your code
    h = node('dummy',L)
    #printList(h)
    std = h
    now = h.next
    before = h
    while now != None :
        std = now
        tmp = now.next
        found = False
        #print('clear-> ',now.data,end= ' ')
        while tmp != None :
            #print('tmp->',tmp.data)
            if tmp.data == now.data :
                std.next = tmp.next
                found = True
            else:
                std = tmp
            tmp = tmp.next
        
        #print('before->',before)
        if found:
            before.next = now.next
        else:
            before = now
        #print('next before->',before)
        now = now.next
        #print('\tL-> ',end = '')
    printList(h.next)

#################### FIX comand ####################   
# input only a number 
L1 = [5,5,2,3,0,3,4,4,7,7,7,7,5,4,8,9]
LL = createList(L1)
print('the list \t-> ',end = '')
printList(LL)
print('del repeat \t-> ',end = '')
delRepeat(LL)


####################################################


# finish  PM
# 9/22/2018
