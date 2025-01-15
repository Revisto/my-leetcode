# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        def level_order_traversal_zigzag(nodes, is_reversed, output):
            new_nodes = []
            values = []
            for node in nodes:
                if node:
                    values.append(node.val)
                    new_nodes.append(node.left)
                    new_nodes.append(node.right)
            if not new_nodes:
                return output

            if is_reversed:
                values = values[::-1]
            output.append(values)

            return level_order_traversal_zigzag(new_nodes, not is_reversed, output)

        return level_order_traversal_zigzag([root], False, [])
