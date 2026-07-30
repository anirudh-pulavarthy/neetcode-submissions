from heapq import heapify, heapreplace, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top = nums[:k]
        heapify(self.top)

        for i in range(k, len(nums)):
            if nums[i] > self.top[0]:
                heapreplace(self.top, nums[i])

    def add(self, val: int) -> int:
        if len(self.top) < self.k:
            heappush(self.top, val)
        elif val > self.top[0]:
            heapreplace(self.top, val)

        return self.top[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)