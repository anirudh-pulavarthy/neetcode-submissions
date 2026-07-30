class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        if left == right: return nums[left]
        
        while nums[left] > nums[right]:
            mid = (left + right) // 2

            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid

        if left == right:
            return nums[left + 1]
        else:
            return nums[left]