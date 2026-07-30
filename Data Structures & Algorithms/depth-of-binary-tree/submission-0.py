# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, depth):
            if node:
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

            else:
                self.ans = max(self.ans, depth)

        dfs(root, 0)

        return self.ans
            
