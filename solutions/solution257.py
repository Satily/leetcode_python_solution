from data_structure import TreeNode, build_binary_tree


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        result = []

        def dfs(root, path):
            path.append(root.val)
            if root.left is None and root.right is None:
                result.append(path.copy())
            else:
                if root.left is not None:
                    dfs(root.left, path)
                if root.right is not None:
                    dfs(root.right, path)
            path.pop()

        dfs(root, [])
        return list(map(lambda x: '->'.join(map(lambda y: str(y), x)), result))


if __name__ == "__main__":
    print(Solution().binaryTreePaths(build_binary_tree(((2, (5,)), 1, (3,)))))
