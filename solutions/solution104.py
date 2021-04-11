from data_structure import TreeNode, build_binary_tree


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == "__main__":
    print(Solution().maxDepth(build_binary_tree(
        ((9,), 3, ((15,), 20, (7,)))
    )))
