from data_structure import TreeNode, build_binary_tree, ds_print


import sys


class Result(object):
    def __init__(self):
        self.node = None
        self.deep = -1
        self.current_deep = sys.maxsize


class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        result = Result()

        def longest_deep(node, deep):
            if node is None:
                return 0
            left = longest_deep(node.left, deep + 1)
            right = longest_deep(node.right, deep + 1)
            if left == right and (right + 1 > result.deep or right + 1 == result.deep and result.current_deep < deep):
                result.node, result.deep, result.current_deep = node, left + 1, deep
            return max(left, right) + 1

        longest_deep(root, 0)
        return result.node


if __name__ == "__main__":
    ds_print(Solution().subtreeWithAllDeepest(build_binary_tree(
        (1,)
    )))
    ds_print(Solution().subtreeWithAllDeepest(build_binary_tree(
        (((6,), 5, ((7,), 2, (4,))), 3, ((0,), 1, (8,)))
    )))
    ds_print(Solution().subtreeWithAllDeepest(build_binary_tree(
        ((2,), 0, ((3,), 1,))
    )))
