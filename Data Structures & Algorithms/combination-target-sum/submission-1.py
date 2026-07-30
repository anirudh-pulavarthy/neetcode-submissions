class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, currentTarget):
            if currentTarget < 0 or i >= len(nums):
                return

            if currentTarget == 0:
                res.append(path[:])

            path.append(nums[i])
            dfs(i, currentTarget - nums[i])
            path.pop()
                
            j = i + 1
            while j < len(nums) and currentTarget - nums[j] >= 0:
                path.append(nums[j])
                dfs(j, currentTarget - nums[j])
                path.pop()
                j += 1
        
        nums.sort()
        for i in range(len(nums)):
            path.append(nums[i])
            dfs(i, target - nums[i])
            path.pop()

        return res