#Q-1 https://www.interviewbit.com/problems/fizzbuzz/
class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        Arr = list()
        Arr.append(0)
        for i in range(1,A+1):
            if(i%3==0 and i%15!=0):
                Arr.append('Fizz')
            elif(i%5==0 and i%15!=0):
                Arr.append('Buzz')
            elif(i%15==0):
                Arr.append('FizzBuzz')
            else:
                Arr.append(i)
        Arr.remove(0)
        return Arr
#Q-2 https://www.interviewbit.com/problems/trailing-zeros-in-factorial/
class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        sum = 0
        while(A!=0):
            sum+=A//5
            A = A//5
        return sum
