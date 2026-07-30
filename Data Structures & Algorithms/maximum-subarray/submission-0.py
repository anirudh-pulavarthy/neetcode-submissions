class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curSum = nums[0]

        for i in range(1, len(nums)):
            curSum = max(nums[i], curSum + nums[i])
            ans = max(ans, curSum)

        return ans