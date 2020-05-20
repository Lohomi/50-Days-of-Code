# Q-2 Very Easy

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                return True
        return False
            

# Q-3 Very Easy

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for x in nums:
            if(nums.count(x)==1):
                return x

# Q-4 Easy

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ints = list()
        hs1 = set()
        hs2 = set()
        for x in nums1:
            hs1.add(x)
        for y in nums2:
            hs2.add(y)
        n1 = len(hs1)
        n2 = len(hs2)
        if(n1>=n2):
            for x in hs2:
                for y in hs1:
                    if(x==y):
                        r = min(nums1.count(y),nums2.count(x))
                        while(r!=0):
                            ints.append(x)
                            r-=1
        else:
            for x in hs1:
                for y in hs2:
                    if(x==y):
                        r = min(nums1.count(x),nums2.count(y))
                        while(r!=0):
                            ints.append(x)
                            r-=1
        return ints

# Q-5 Very Easy

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(0)
        for x in digits:
            num+=x
            num*=10
        num = num//10 + 1
        digits.clear()
        while(num!=0):
            digits.append(num%10)
            num = num//10
        digits.reverse()
        return digits
        
