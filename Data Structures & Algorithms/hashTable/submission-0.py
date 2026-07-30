class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.data = {}

    def insert(self, key: int, value: int) -> None:
        self.data[key] = value
        self.size += 1

        if self.getSize() >= 0.5 * self.getCapacity():
            self.resize()


    def get(self, key: int) -> int:
        return self.data.get(key, -1)

    def remove(self, key: int) -> bool:
        if key not in self.data: return False

        del self.data[key]
        self.size -=1
        return True

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
