# lab test 3rd 
# dataStructure 
# by CXZ
# when i bore to read  other subject ;(
# 1st December 2018
# 8:23 PM
# @K4station LKB with korw
# @NoThaankCafe with pejoyable and suugar


# hash 
# key is english number
# data is france number 

# 'one'
# 'two'
# 'three'
# 'four'
# 'five'
# 'ten'
# 'eleven'

# testcase
# size of table         = 5 
# max collision chain   = 5
# put only
# quaddratic probe


class record:
    def __init__(self,key,data):
        self.key = key
        self.data = data 
    def __str__(self):
        return '('+str(self.key)+','+str(self.data)+')'

class hash:
    def __init__(self,size,maxCollision):
        self.size = size
        self.table = [None]*size
        self.num = 0
        self.maxCollision = maxCollision
    def printTable(self):
        for i in range(len(self.table)) :
            print('#',i+1,'\t',self.table[i],sep ='')
        print('---------------------------')

    def put(self,rec):
        if self.size <= self.num :
            print('this table is FULLLL!!!!!')
            return
        got = False
        n_collision =0
        while not got :
            index = self.hash(rec.key,n_collision)
            if self.table[index] == None :
                self.table[index] = rec
                got = True
                self.num += 1
                self.printTable()
                n_collision = 0
            elif n_collision < self.maxCollision :
                n_collision+=1
                print('collitoin number',n_collision,'at',index)
            else:
                print('Max of collisionChain')
                got = True
                self.printTable()


    def hash(self,s,numCollision):
        ans = 0
        for i in s :
            ans += ord(i)
        return (ans + (numCollision*numCollision) )%self.size
r= [
record('one','Un')
,record('two','Deux')
,record('three','Trois')
,record('four','Quatre')
,record('five','Cinq')
,record('ten','Dix')
,record('eleven','Onze')
]

h = hash(5,5)
h.printTable()

for i in r:
    h.put(i)


    
# 1st December 2018
# start X:XX PM
# @NoThaankCafe with Pejoable and suugar