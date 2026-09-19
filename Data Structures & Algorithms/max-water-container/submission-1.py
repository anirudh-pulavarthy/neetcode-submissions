class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        ans = 0
        capacity = lambda left, right: (right - left) * min(heights[left], heights[right])
        
        i, j = 0, len(heights) - 1
        while i < j:
            ans = max(ans, capacity(i, j))
            
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        
        return ans
