# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(tree1, tree2):
            if not tree1 and not tree2: return True
            if not tree1 or not tree2: return False
            return tree1.val == tree2.val \
                and isSame(tree1.left, tree2.left) \
                and isSame(tree1.right, tree2.right)

        self.ans = False
        def dfs(node):
            if not node: return

            if node.val == subRoot.val and isSame(node, subRoot):
                self.ans = True
            else:
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return self.ans