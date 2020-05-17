def binomialCoeff(n , k): 
    C = [[0 for x in range(k+1)] for x in range(n+1)]
    
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if(j==0 or j==i):
                C[i][j] = 1 
            else:
                C[i][j]=C[i-1][j-1]+C[i-1][j]
    return C[n][k]
    
for _ in range(int(input())):
    n, k = map(int,input().split())
    ans = binomialCoeff(n-1,k-1)
    print(ans)
#DynamicProgramming
#TLE

#Optimised Method
def binomialCoeff(n , k): 
    ans = 1
    if(k>n//2):
        k=n-k
    for i in range(k):
        ans*=n
        ans = ans//(i+1)
        n = n-1
    return ans
for _ in range(int(input())):
    n, k = map(int,input().split())
    ans = binomialCoeff(n-1,k-1)
    print(ans)
#Accepted
