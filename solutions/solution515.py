from data_structure import TreeNode, build_binary_tree


class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def dfs(node, deep):
            if node is None:
                return
            if len(result) == deep:
                result.append(node.val)
            else:
                result[deep] = max(result[deep], node.val)
            dfs(node.left, deep + 1)
            dfs(node.right, deep + 1)

        dfs(root, 0)
        return result


if __name__ == "__main__":
    print(Solution().largestValues(build_binary_tree(
        (((5,), 3, (3,)), 1, (2, (9,)))
    )))
