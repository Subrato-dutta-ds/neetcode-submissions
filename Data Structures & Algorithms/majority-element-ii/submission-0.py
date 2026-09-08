class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency = {}
        result = []
        n = len(nums)
         
        for num in nums:
            if num in frequency:
                frequency[num] +=1
            else:
                frequency[num] = 1
        for num in frequency:
            if frequency[num] > n/3:
                result.append(num)
        return result
        