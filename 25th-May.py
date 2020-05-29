# Q-1 https://www.interviewbit.com/problems/add-one-to-number/
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
            num = 0
            for x in A:
                num+=x
                num*=10
            num=num//10
            num+=1
            A.clear()
            A = map(int, str(num))
            return A
