from data_structure.binary_tree_with_next import Node


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        levels = []

        def dfs(node: 'Node', deep: int):
            if node is None:
                return
            if len(levels) == deep:
                levels.append(node)
            else:
                levels[deep].next = node
                levels[deep] = node
            dfs(node.left, deep + 1)
            dfs(node.right, deep + 1)

        dfs(root, 0)
        return root


if __name__ == "__main__":
    root = Node(
        1,
        Node(
            2,
            Node(4, None, None, None),
            Node(5, None, None, None),
            None
        ),
        Node(
            3,
            None,
            Node(7, None, None, None),
            None
        ),
        None
    )
    Solution().connect(root)
    print(root)
    # Test by Debugger
