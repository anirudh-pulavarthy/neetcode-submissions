class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        put = m + n - 1
        while put >= 0:
            if (p2 < 0) or (p1 >= 0 and nums1[p1] > nums2[p2]):
                nums1[put] = nums1[p1]
                p1 -= 1
            else:
                nums1[put] = nums2[p2]
                p2 -= 1
            put -= 1