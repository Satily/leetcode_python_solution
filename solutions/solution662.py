from data_structure import TreeNode, build_binary_tree


class Solution:
    def widthOfBinaryTree(self, root: 'TreeNode') -> 'int':
        def dfs(node: TreeNode, deep: int, path: int, paths: list):
            if node is None:
                return
            if len(paths) == deep:
                paths.append([])
            paths[deep].append(path)
            dfs(node.left, deep + 1, (path << 1) + 0, paths)
            dfs(node.right, deep + 1, (path << 1) + 1, paths)

        paths = []

        dfs(root, 0, 0, paths)

        return max(map(lambda path_line: max(path_line) - min(path_line), paths)) + 1
        # return paths


if __name__ == "__main__":
    print(Solution().widthOfBinaryTree(build_binary_tree((((5,), 3, (3,)), 1, (2, (9,))))))
    print(Solution().widthOfBinaryTree(build_binary_tree((((5,), 3, (3,)), 1))))
    print(Solution().widthOfBinaryTree(build_binary_tree((((5,), 3,), 1, (2,)))))
    print(Solution().widthOfBinaryTree(build_binary_tree(((((6,), 5,), 3), 1, (2, (9, (7,)))))))
