from data_structure import TreeNode, build_binary_tree


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        def dfs(node, deep):
            if node is None:
                return
            if deep == len(result):
                result.append([])
            result[deep].append(node.val)
            dfs(node.left, deep + 1)
            dfs(node.right, deep + 1)

        dfs(root, 0)

        for index in range(1, len(result), 2):
            result[index].reverse()
        return result


if __name__ == "__main__":
    print(Solution().zigzagLevelOrder(build_binary_tree(
        ((9,), 3, ((15,), 20, (7,)))
    )))
