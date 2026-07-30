from heapq import heappushpop, heappush

class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points): return points

        res = []

        for p in points:
            dist = -(p[0]** 2 + p[1] ** 2)

            if len(res) < k:
                heappush( res, (dist, p) )
            else:
                heappushpop( res, (dist, p) )

        return [ p for  (dist, p) in res ]
