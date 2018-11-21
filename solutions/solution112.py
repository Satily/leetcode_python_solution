from data_structure import TreeNode, build_binary_tree


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            return sum == root.val
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


if __name__ == "__main__":
    tree = build_binary_tree(
        ((((None, 7, None), 11, (None, 2, None)), 4, None), 5, ((None, 13, None), 8, (None, 4, (None, 1, None))))
    )
    print(Solution().hasPathSum(tree, 22))
    tree = build_binary_tree(
        (None, -2, (None, -3, None))
    )
    print(Solution().hasPathSum(tree, 0))
