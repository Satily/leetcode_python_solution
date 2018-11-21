from data_structure import TreeNode, build_binary_tree


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_symmetric(r0, r1):
            if r0 is None and r1 is None:
                return True
            elif r0 is None or r1 is None or r0.val != r1.val:
                return False
            return check_symmetric(r0.left, r1.right) and check_symmetric(r1.left, r0.right)

        if root is None:
            return True
        return check_symmetric(root.left, root.right)


if __name__ == "__main__":
    root = build_binary_tree(
        (((3,), 2, (4,)), 1, ((4,), 2, (3,)))
    )
    print(Solution().isSymmetric(root))
    root = build_binary_tree(
        ((2, (3,)), 1, (2, (3,)))
    )
    print(Solution().isSymmetric(root))
