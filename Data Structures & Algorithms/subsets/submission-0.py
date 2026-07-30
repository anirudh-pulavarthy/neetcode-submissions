class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        current_set = []

        length = len(nums)
        def find_subsets(index):
            if index == length:
                ans.append(current_set[:])
                return

            find_subsets(index + 1)

            current_set.append(nums[index])
            find_subsets(index + 1)
            current_set.pop()

        find_subsets(0)
        return ans