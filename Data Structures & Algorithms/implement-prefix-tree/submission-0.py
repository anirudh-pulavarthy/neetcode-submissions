class Node:
    def __init__(self):
        # self.letter = char
        self.children = [None] * 26
        self.end = False
        
class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root

        for c in word:
            index = ord(c) - ord('a')
            if current.children[index] is None:
                current.children[index] = Node()
            
            current = current.children[index]

        current.end = True

    def search(self, word: str) -> bool:
        current = self.root

        for c in word:
            index = ord(c) - ord('a')
            if current.children[index] is None:
                return False
            
            current = current.children[index]

        return current.end

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for c in prefix:
            index = ord(c) - ord('a')
            if current.children[index] is None:
                return False
            
            current = current.children[index]

        return True
        