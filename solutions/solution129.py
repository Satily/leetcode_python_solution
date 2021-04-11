from data_structure import TreeNode, build_binary_tree


class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, num):
            num = num * 10 + node.val
            if node.left is None and node.right is None:
                return num
            left, right = 0, 0
            if node.left is not None:
                left = dfs(node.left, num)
            if node.right is not None:
                right = dfs(node.right, num)
            return left + right

        if root is None:
            return 0
        else:
            return dfs(root, 0)


if __name__ == "__main__":
    print(Solution().sumNumbers(build_binary_tree(
        ((2,), 1, (3,))
    )))
    print(Solution().sumNumbers(build_binary_tree(
        (((5,), 9, (1,)), 4, (0,))
    )))
