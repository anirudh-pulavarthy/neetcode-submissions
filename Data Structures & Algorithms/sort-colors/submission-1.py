class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = {0:0, 1:0, 2:0}
        for n in nums:
            counter[n] += 1
            
        i = 0
        for item, count in counter.items():
            for j in range(count):
                nums[i] = item
                i += 1

            