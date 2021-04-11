from data_structure import TreeNode, build_binary_tree


class Solution:
    def averageOfLevels(self, root):
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
        return list(map(lambda x: sum(x) / len(x), result))


if __name__ == "__main__":
    print(Solution().averageOfLevels(build_binary_tree(
        ((9,), 3, ((15,), 20, (7,)))
    )))
