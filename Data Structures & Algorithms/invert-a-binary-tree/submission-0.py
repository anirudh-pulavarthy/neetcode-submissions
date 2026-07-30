# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertChild(node):
            if not node: return
            if not (node.left or node.right): return

            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left:
                invertChild(node.left)
            if node.right:
                invertChild(node.right)
        
        invertChild(root)
        return root