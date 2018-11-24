from data_structure import TreeNode, build_binary_tree, ds_print


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result = []
        result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))
        return result


if __name__ == "__main__":
    print(Solution().inorderTraversal(build_binary_tree(
        (None, 1, ((None, 3, None), 2, None))
    )))
