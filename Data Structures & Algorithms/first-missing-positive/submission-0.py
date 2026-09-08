class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        numbers = set(nums)
        i =1 
        while i in numbers:
            i+=1
        return i

        