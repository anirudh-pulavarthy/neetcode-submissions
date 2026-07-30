class UnionFind:
    
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        parent_x = self.find(x)
        parent_y = self.find(y)

        return parent_x == parent_y

    def union(self, x: int, y: int) -> bool:
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y: return False

        if self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_y] = parent_x
        elif self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_x] = parent_y
        else:
            # print(f"Union of {x} and {y} => parent is {x}")
            self.parent[parent_y] = parent_x
            self.rank[x] += 1
        
        return True


    def getNumComponents(self) -> int:
        for i in range(len(self.parent)):
            self.parent[i] = self.find(i)

        # print(self.parent)
        return len(set(self.parent))
