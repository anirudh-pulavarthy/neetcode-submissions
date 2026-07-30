# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        if not root: return ans
        
        queue = deque([root])

        while queue:
            n = len(queue)
            level = []

            for _ in range(n):

                # collect all nodes in the level
                node = queue.popleft()
                level.append(node.val)

                # add their children (l & r) to the queue
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            ans.append(level.copy())

        return ans            