from data_structure import TreeNode, build_binary_tree, ds_print


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invert(node):
            if node is None:
                return
            invert(node.left)
            invert(node.right)
            node.left, node.right = node.right, node.left

        invert(root)
        return root


if __name__ == "__main__":
    ds_print(Solution().invertTree(build_binary_tree((((1,), 2, (3,)), 4, ((6,), 7, (9,))))))
