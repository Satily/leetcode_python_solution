from data_structure import TreeNode, build_binary_tree, ds_print


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def flatten_append(node, append_node):
            if node is None:
                return append_node
            node.right = flatten_append(node.left, flatten_append(node.right, append_node))
            node.left = None
            return node

        flatten_append(root, None)


if __name__ == "__main__":
    root = build_binary_tree((((3,), 2, (4,)), 1, (5, (6,))))
    Solution().flatten(root)
    ds_print(root)
