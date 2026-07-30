class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1 # the last position

        goal = n

        for i in range(n - 1, -1, -1):
            if nums[i] + i >= goal:
                goal = i

            if goal == 0: return True

        return goal == 0
