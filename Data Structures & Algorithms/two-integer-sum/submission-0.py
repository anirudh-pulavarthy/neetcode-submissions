class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time complexity O(n)
        Space complexity O(n)

        """
        prev_map = {} # value: index

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prev_map:
                return [prev_map[diff], i]
            
            prev_map[n] = i