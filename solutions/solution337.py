from data_structure import TreeNode, build_binary_tree

from itertools import product


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dp(node):
            if node is None:
                return [0, 0]
            left_dp, right_dp = dp(node.left), dp(node.right)
            return [max(map(sum, product(left_dp, right_dp))), left_dp[0] + right_dp[0] + node.val]
        return max(dp(root))


if __name__ == "__main__":
    print(Solution().rob(build_binary_tree(
        ((2, (3,)), 3, (3, (1,)))
    )))
    print(Solution().rob(build_binary_tree(
        (((1,), 4, (3,)), 3, (5, (1,)))
    )))
