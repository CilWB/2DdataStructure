# Q1 : recursive function
# desin your own parameter
# return sum of "even" number in the list

l=[1,2,3,4,5,6,7,8,9,10]

def sumEven(l,idx=0):
    if idx < len(l) :
        if l[idx]%2==0:
            return l[idx] + sumEven(l,idx+1)
        else:
            return sumEven(l,idx+1)
    else:
        return 0

print(sumEven(l))
