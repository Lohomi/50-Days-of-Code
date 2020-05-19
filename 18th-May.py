#18th May Q1
def getNthUgly(n):
    ugly = [0]*n 
    ugly[0] = 1 
    i2 = i3 = i5 = 0
    next_multiple_of_2 = 2 
    next_multiple_of_3 = 3 
    next_multiple_of_5 = 5 
    for i in range(1,n):
        ugly[i] = min(next_multiple_of_5,next_multiple_of_3,next_multiple_of_2)
        if(ugly[i]==next_multiple_of_2):
            i2+=1 
            next_multiple_of_2=ugly[i2]*2 
        if(ugly[i]==next_multiple_of_3):
            i3=i3+1 
            next_multiple_of_3=ugly[i3]*3 
        if(ugly[i]==next_multiple_of_5):
            i5+=1 
            next_multiple_of_5=ugly[i5]*5 
        
    return ugly[-1]

for _ in range(int(input())):
    n = int(input())
    print(getNthUgly(n))

#Dynamic Programing

#18th May Q2
# Fibonacci Series using Dynamic Programming  
def fibonacci(n):  
      
    # Taking 1st two fibonacci nubers as 0 and 1  
    FibArray = [0, 1]  
      
    while len(FibArray) < n + 1:  
        FibArray.append(0)  
      
    if n <= 1:  
        return n  
    else:  
        if FibArray[n - 1] == 0:  
            FibArray[n - 1] = fibonacci(n - 1)  
  
        if FibArray[n - 2] == 0:  
            FibArray[n - 2] = fibonacci(n - 2)  
              
    FibArray[n] = FibArray[n - 2] + FibArray[n - 1]  
    return FibArray[n]  
      
print(fibonacci(9))  

#18May 3rd Leetcode Nuy and sell Stocks II (Easy) (DP)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        for i in range(1,n):
            profit+=max(prices[i]-prices[i-1],0)
        return profit
