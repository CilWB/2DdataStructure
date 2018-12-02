#lab test 3rd 
# dataStructure 
# by CXZ
# 1st December 2018
# start 8:27 PM
# @NoThaankCafe with Pejoable and suugar

# this adjacenct matrixistranferr frpm the problem 
# you can ask for [ic of thisgraph frome me :)
adj = [
#    0 1 2 3 4 5 6
    [0,1,0,0,1,0,0], # 0 
    [0,0,1,0,1,0,0], # 1
    [0,0,0,0,1,0,1], # 2 
    [1,0,0,0,0,0,0], # 3 
    [0,0,0,1,0,0,1], # 4
    [0,0,0,0,1,0,1], # 5
    [0,0,0,0,0,0,0]]  # 6


walked = [False]*7



def dfs(start,stop,w=[False]*7,ans = [] ):
    global adj
    if start == stop :
        return ans + [stop]
    else:
        if w[start] == False :
            w[start] = True
            #print('now at',start)
            for i in range(len(adj[start])):
                #print(adj[start],i)
                if adj[start][i] != 0 and w[i] == False:
                    #print('walk to',i)
                    l = dfs(i,stop,w,ans+[start])
                    if l != [] :
                        return l
    return []


def clear(l):
    for i in range(len(l)) :
        l[i] = False
    return l
for i in range(7):
    for j in range(7):
        print('from',i,'to',j,'path is ',dfs(i,j,clear(walked)))
        #walked =  clear(walked)
        #print(walked)




# stop 2:17 PM
# 3rd December 2018
# @theHome2409 
