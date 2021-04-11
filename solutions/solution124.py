from data_structure import TreeNode, ds_print, build_binary_tree
import sys


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        def dfs(root: TreeNode):
            if root is None:
                return -sys.maxsize, 0
            left_ans, left_max_sum = dfs(root.left)
            right_ans, right_max_sum = dfs(root.right)

            return max(left_ans, right_ans, root.val + max(left_max_sum, 0) + max(right_max_sum, 0)), max(left_max_sum, right_max_sum, 0) + root.val

        return dfs(root)[0] if root is not None else 0


if __name__ == '__main__':
    print(Solution().maxPathSum(build_binary_tree("[1,2,3]")))
    print(Solution().maxPathSum(build_binary_tree("[-10,9,20,null,null,15,7]")))
    print(Solution().maxPathSum(build_binary_tree("[-3]")))
    print(Solution().maxPathSum(build_binary_tree("[9,6,-3,null,null,-6,2,null,null,2,null,-6,-6,-6]")))
