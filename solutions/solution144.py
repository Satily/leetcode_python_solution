from data_structure import TreeNode, build_binary_tree


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result = [root.val]
        result.extend(self.preorderTraversal(root.left))
        result.extend(self.preorderTraversal(root.right))
        return result


if __name__ == "__main__":
    print(Solution().preorderTraversal(build_binary_tree((1, ((3,), 2)))))
