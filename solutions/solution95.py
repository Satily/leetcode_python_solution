from data_structure import TreeNode, ds_print


class Solution:
    def generateTrees(self, n: int) -> 'List[TreeNode]':

        def generate_tree_with_range(start, end):
            if start > end:
                return [None]
            result = []
            for index in range(start, end + 1):
                for left_tree in generate_tree_with_range(start, index - 1):
                    for right_tree in generate_tree_with_range(index + 1, end):
                        this_node = TreeNode(index)
                        this_node.left, this_node.right = left_tree, right_tree
                        result.append(this_node)
            return result

        if n == 0:
            return []
        else:
            return generate_tree_with_range(1, n)


if __name__ == '__main__':
    for tree in Solution().generateTrees(3):
        ds_print(tree)
    # for tree in Solution().generateTrees(0):
    #     ds_print(tree)
