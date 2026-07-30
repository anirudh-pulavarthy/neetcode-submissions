class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    # def print(self):
    #     node = self.head
    #     while node:
    #         print(node.value, end = '')
    #         node = node.next
    #     print('\nDone..\n')

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node        

    def moveToHead(self, node):
        # print('Trying to move to head')
        self.removeNode(node)
        # self.print()

        self.addToHead(node)
        # self.print()

    def removeNode(self, node):
        # print(f'Trying to remove {node.value}')
        prevN = node.prev
        nextN = node.next

        # print(f'Trying to update {prevN.value} next to {nextN.value}')
        prevN.next = nextN
        nextN.prev = prevN

        node.prev = None
        node.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        # print(f"Getting {key}")
        if key in self.cache:
            self.moveToHead(self.cache[key])
            return self.cache[key].value

        return -1

    def put(self, key: int, value: int) -> None:
        # print(f"Putting {key}, {value}")
        if key in self.cache:
            node = self.cache[key]
            self.moveToHead(node)
            self.cache[key].value = value
        else:
            newNode = Node(key, value)
            self.addToHead(newNode)
            self.cache[key] = newNode

            if len(self.cache) > self.capacity:
                lruNode = self.tail.prev
                self.removeNode(lruNode)
                del self.cache[lruNode.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)