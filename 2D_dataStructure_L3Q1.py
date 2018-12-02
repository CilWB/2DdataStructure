#lab test 3rd 
# dataStructure 
# by CXZ

# 1st December 2018
# start 8:27 PM
# @NoThaankCafe with Pejoable and suugar


list = [-1,8,3,1,9,11,15,20,6,4,9]

def insertion(l):
    ans = []
    for i in range(len(l)):
        #print('consider->',l[i])
        print('pass #',i,end ='\t-> ')
        index = 0
        for j in range(len(ans)):
            #print('compare ',l[i],ans[j])
            if l[i] < ans[j] :
                #print('break')
                break
            else:
                index = j+1
        ans.insert(index,l[i])
        print(ans)
    return ans
print(insertion(list))

# stop 2:36 PM
# 3rd December 2018
# @theHome2409 
