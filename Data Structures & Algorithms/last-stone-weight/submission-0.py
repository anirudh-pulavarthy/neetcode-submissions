from heapq import heapify, heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def maxheapify(arr):
            arr[:] = [-x for x in arr]

            #print(f"before {arr}")
            heapify(arr)
            #print(f"after {arr}")

        
        def push(arr, num):
            heappush(arr, -num)

        def pop(arr):
            return -heappop(arr)

        maxheapify(stones)
        #print(stones)

        while len(stones) >= 2:
            s1 = pop(stones)
            s2 = pop(stones)
            #print(s1, s2)

            if s1 != s2:
                push(stones, abs(s1 - s2))

        return -stones[0] if len(stones) > 0 else 0