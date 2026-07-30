# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = ""
        
        def dfs(node):
            nonlocal serialized
            if node:
                serialized += str(node.val) + ","                
                dfs(node.left)
                dfs(node.right)
            else:
                serialized += "N,"
        
        dfs(root)

        return serialized
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        splitNodes = data.split(',')
        splitNodes.pop()

        def dfs():
            nonlocal index
            if splitNodes[index] == 'N':
                index += 1
                return None
            
            node = TreeNode(int(splitNodes[index]))
            index += 1

            node.left = dfs()
            node.right = dfs()
            return node

        index = 0
        return dfs()