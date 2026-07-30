from heapq import heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for i, j, time in times:
            adjList[i].append((j, time))

        # ans = {i: float("inf") for i in range(n)}
        ans = {}

        minHeap = [(0, k)]
        while minHeap:
            time, node = heappop(minHeap)

            if node in ans: continue
            ans[node] = time

            for neighbor, time_to_neighbor in adjList[node]:
                if neighbor in ans: continue
                heappush(minHeap, (time + time_to_neighbor, neighbor))
        
        if len(ans) != n: return -1
        total_time = max(time for node, time in ans.items())
        return total_time