from data_structure import TreeNode, build_binary_tree


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None or q is None:
            return q == p
        return self.isSameTree(p.left, q.left) and p.val == q.val and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    print(Solution().isSameTree(build_binary_tree(((2,), 1, (3,))), build_binary_tree(((2,), 1, (3,)))))
    print(Solution().isSameTree(build_binary_tree(((2,), 1)), build_binary_tree((1, (2,)))))
    print(Solution().isSameTree(build_binary_tree(((2,), 1, (1,))), build_binary_tree(((1,), 1, (2,)))))
