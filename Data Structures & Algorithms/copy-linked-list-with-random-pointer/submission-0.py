"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pointers = {}
        
        def copy(node):
            if node is None: return None
            if node in pointers: return pointers[node]

            newNode = Node(node.val)
            pointers[node] = newNode
            
            newNode.random = copy(node.random)
            newNode.next = copy(node.next)
            return newNode

        return copy(head) 
