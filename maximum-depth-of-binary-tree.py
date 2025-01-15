# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        def search(node, depth):
            if not node:
                return depth

            if not node.left and not node.right:
                return depth

            depth += 1

            return max(search(node.right, depth), search(node.left, depth))

        return search(root, 1)
