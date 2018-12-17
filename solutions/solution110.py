from data_structure import TreeNode, build_binary_tree


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def get_deep(node):
            if node is None:
                return 0
            left, right = get_deep(node.left), get_deep(node.right)
            if left is None or right is None:
                return None
            if abs(left - right) > 1:
                return None
            return max(left, right) + 1

        return get_deep(root) is not None


if __name__ == "__main__":
    print(Solution().isBalanced(build_binary_tree(
        ((((4,), 3), 2), 1, (2, (3, (4,))))
    )))
    print(Solution().isBalanced(build_binary_tree(
        ((9,), 3, ((15,), 20, (7,)))
    )))
    print(Solution().isBalanced(build_binary_tree(
        ((((4,), 3, (4,)), 2, (3,)), 1, (2,))
    )))
