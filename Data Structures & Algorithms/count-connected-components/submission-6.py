class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)

        visited = set()

        def dfs(i):
            visited.add(i)

            for j in adjList[i]:
                if j not in visited:
                    dfs(j)

        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count
