from heapq import heappop, heappush
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjList = defaultdict(list)
        for u,v,w in edges:
            adjList[u].append((w, v))
        
        ans = {}
        minHeap = [(0, src)]
        while minHeap:
            cost_to_u, u = heappop(minHeap)
            if u in ans: continue

            ans[u] = cost_to_u

            for weight, v in adjList[u]:
                if v not in ans:
                    heappush(minHeap, (weight + cost_to_u, v))

        for i in range(n):
            if i not in ans:
                ans[i] = -1
        
        return ans