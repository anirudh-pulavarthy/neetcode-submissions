class Solution:
    def helper(self, arr):
        rob1, rob2 = 0, 0
        temp = 0
        for n in arr:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return temp

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))