class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        frequency ={}
        for num in nums:
            if num in frequency:
                frequency[num] +=1
            else:
                frequency[num] =1
        i = 0
        for num in frequency:
            nums[i] = num
            i+=1
        return i
            
        
        