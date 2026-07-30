class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >=0 : return [n * n for n in nums]

        l = 0
        while l + 1 < len(nums) and nums[l + 1] < 0:
            l += 1

        r = l + 1

        ans = []
        while l >= 0 or r < len(nums):
            if l < 0:
                ans.append(nums[r] ** 2)
                r += 1
            elif r == len(nums) or abs(nums[l]) <= abs(nums[r]):
                ans.append(nums[l] ** 2)
                l -= 1
            else:
                ans.append(nums[r] ** 2)
                r += 1

        return ans
