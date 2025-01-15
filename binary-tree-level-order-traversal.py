# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        def level_order_traversal(nodes, output):
            new_nodes = []
            values = []
            for node in nodes:
                if node:
                    values.append(node.val)
                    new_nodes.append(node.left)
                    new_nodes.append(node.right)
            if not new_nodes:
                return output
            output.append(values)
            return level_order_traversal(new_nodes, output)

        return level_order_traversal([root], [])
