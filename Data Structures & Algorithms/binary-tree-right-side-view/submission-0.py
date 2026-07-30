# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root: return ans

        queue = deque([root])
        while queue:
            nodes_in_level = len(queue)
            last_node = queue[nodes_in_level - 1]
            ans.append(last_node.val)

            for _ in range(nodes_in_level):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return ans