class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) // 2

            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                break
            
        if not (l <= r): return False

        row = (l + r) // 2
        l, r = 0, n -1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return False