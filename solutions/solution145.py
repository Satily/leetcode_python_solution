from data_structure import TreeNode, build_binary_tree


class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result = []
        result.extend(self.postorderTraversal(root.left))
        result.extend(self.postorderTraversal(root.right))
        result.append(root.val)
        return result


if __name__ == "__main__":
    print(Solution().postorderTraversal(build_binary_tree((1, ((3,), 2)))))
