class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        theSet = set(nums)
        return len(theSet) != len(nums)
         