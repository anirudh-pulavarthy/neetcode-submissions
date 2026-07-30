class Graph:
    
    def __init__(self):
        self.graph = defaultdict(set)

    def addEdge(self, src: int, dst: int) -> None:
        self.graph[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if dst in self.graph[src]:
            self.graph[src].remove(dst)
            return True
        
        return False


    def hasPath(self, src: int, dst: int) -> bool:

        visited = set()
        queue = deque([src])
        while queue:
            node = queue.popleft()

            if node == dst: return True
            visited.add(node)

            for i in self.graph[node]:
                if i not in visited:
                    queue.append(i)
        
        return False