class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumOfnums = n * (n + 1) // 2
        return sumOfnums - sum(nums)