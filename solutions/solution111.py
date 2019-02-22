from data_structure import TreeNode, build_binary_tree


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left, right = self.minDepth(root.left), self.minDepth(root.right)
        if left == 0:
            return right + 1
        elif right == 0:
            return left + 1
        else:
            return min(left, right) + 1


if __name__ == "__main__":
    print(Solution().minDepth(build_binary_tree(
        ((9,), 3, ((15,), 20, (7,)))
    )))
