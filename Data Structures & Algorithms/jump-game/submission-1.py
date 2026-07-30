class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans = [-1] * len(nums)

        def dfs(i):
            if i == len(nums) - 1: return True
            end = min(nums[i] + i, len(nums) - 1)
            for j in range(i + 1, end + 1):
                if dfs(j): return True

            return False
    
        return dfs(0)