from data_structure import build_binary_tree, TreeNode, ds_print


class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if node is None:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            if not left:
                node.left = None
            if not right:
                node.right = None
            return left or right or node.val == 1

        if not dfs(root):
            root = None
        return root


if __name__ == "__main__":
    root = build_binary_tree((1, ((0,), 0, (1,))))
    ds_print(Solution().pruneTree(root))
    root = build_binary_tree((((0,), 0, (0,)), 1, ((0,), 1, (1,))))
    ds_print(Solution().pruneTree(root))
    root = build_binary_tree(((((0,), 1), 1, (1,)), 1, ((0,), 0, (1,))))
    ds_print(Solution().pruneTree(root))
