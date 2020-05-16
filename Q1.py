def minmaxdigit(n):               # Finds the minimum and maximum digits of a number
    digit = list()
    while (n!=0):
        digit.append(n%10)
        n = n//10
    digit.sort()
    x=len(digit)
    return digit[0],digit[x-1]
    
def nextnumfinder(x):            # Finds the next number in the sequence
    mind, maxd = minmaxdigit(x)
    return (x + mind*maxd)
      
def solver(in_num,n):            # Finds the kth number given the first number
    if(n==1):
        return in_num
    else:
        count = 0
        prevnum = in_num
        while(count!=(n-1)):
            nextnum = nextnumfinder(prevnum)
            prevnum = nextnum
            count+=1
        return nextnum

t = int(input())
for x in range(t):
    a1, k = map(int,input().split())
    ans = solver(a1,k)
    print(ans)

      
      

    
