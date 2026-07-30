class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1] * n
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x, y):
            parentX = find(x)
            parentY = find(y)

            if parentX == parentY: return

            if rank[parentX] > rank[parentY]:
                parent[parentY] = parentX
            elif rank[parentX] < rank[parentY]:
                parent[parentX] = parentY
            else:
                parent[parentY] = parentX
                rank[parentX] += 1

        for e in edges:
            (x, y) = e
            union(x, y)
        
        roots = {find(x) for x in range(n)}
        print(roots)
        return len(roots)
