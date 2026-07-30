class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []
        for i in range(len(nums) - 2):
            if i and nums[i] == nums[i - 1]: continue
            
            j, k = i + 1, len(nums) - 1

            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

                elif current_sum > 0:
                    k -= 1
                else:
                    j += 1
            
        return result
                