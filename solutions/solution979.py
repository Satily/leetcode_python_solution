from data_structure import TreeNode, build_binary_tree


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> (int, int, int):
            if node is None:
                return 0, 0, 0
            left_node_number, left_coin_number, left_result = dfs(node.left)
            right_node_number, right_coin_number, right_result = dfs(node.right)
            node_number, coin_number = left_node_number + right_node_number + 1, left_coin_number + right_coin_number + node.val
            return node_number, coin_number, left_result + right_result + abs(node_number - coin_number)
        return dfs(root)[2]


if __name__ == "__main__":
    print(Solution().distributeCoins(build_binary_tree("[3,0,0]")))    
    print(Solution().distributeCoins(build_binary_tree("[0,3,0]")))
    print(Solution().distributeCoins(build_binary_tree("[1,0,2]")))
    print(Solution().distributeCoins(build_binary_tree("[1,0,0,null,3]")))
