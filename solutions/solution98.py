from data_structure import TreeNode, build_binary_tree, ds_print


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def middle_travel(root):
            if root is None:
                return []
            result = []
            result.extend(middle_travel(root.left))
            result.append(root.val)
            result.extend(middle_travel(root.right))
            return result

        t = middle_travel(root)
        for index in range(len(t) - 1):
            if t[index] >= t[index + 1]:
                return False
        return True



if __name__ == "__main__":
    print(Solution().isValidBST(build_binary_tree(((1,), 0))))
    print(Solution().isValidBST(build_binary_tree(((1,), 1))))
    print(Solution().isValidBST(build_binary_tree(((1,), 2, (3,)))))
    print(Solution().isValidBST(build_binary_tree(((1,), 5, ((3,), 4, (6,))))))
    print(Solution().isValidBST(build_binary_tree(((5,), 10, ((6,), 15, (20,))))))
