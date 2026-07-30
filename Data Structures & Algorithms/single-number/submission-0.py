class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        solo = 0

        for num in nums:
            solo ^= num
        
        return solo
        