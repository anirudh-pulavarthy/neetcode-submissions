class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        path = []
        def backtrack(i):
            if i == len(nums):
                res.add(tuple(path[:]))
                return

            backtrack(i + 1)

            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

        backtrack(0)
        return list(list(a) for a in res)