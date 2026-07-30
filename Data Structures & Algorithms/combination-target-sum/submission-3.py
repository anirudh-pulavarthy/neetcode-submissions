class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, currentTarget):
            # print(f"dfs({i}, {currentTarget}) is called")
            if currentTarget < 0 or i >= len(nums):
                return

            if currentTarget == 0:
                # path.append(nums[i])
                res.append(path[:])
                # path.pop()
                return

            j = i
            while j < len(nums) and currentTarget - nums[j] >= 0:
                path.append(nums[j])
                dfs(j, currentTarget - nums[j])
                path.pop()
                j += 1
        
        nums.sort()
        dfs(0, target)

        return res