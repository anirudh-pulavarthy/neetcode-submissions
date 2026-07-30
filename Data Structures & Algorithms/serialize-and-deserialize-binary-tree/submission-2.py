# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node is None:
                ans.append('#')
            else:
                ans.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ','.join(ans)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(f"Data is {data}")
        nodes = data.split(',')

        if nodes[0] == '#':
            return None

        root = TreeNode(int(nodes[0]))
        queue = deque([root])

        index = 1
        while queue:
            node = queue.popleft()
            if nodes[index] != '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            
            if nodes[index] != '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1

        return root