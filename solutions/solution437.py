from data_structure import TreeNode, build_binary_tree


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0

        def travel(root, path_sum):
            ns = path_sum[-1] + root.val
            r = 0
            for item in path_sum:
                if ns - item == sum:
                    r += 1
            path_sum.append(ns)
            if root.left is not None:
                r += travel(root.left, path_sum)
            if root.right is not None:
                r += travel(root.right, path_sum)
            path_sum.pop()
            return r

        return travel(root, [0])


if __name__ == "__main__":
    print(Solution().pathSum(
        build_binary_tree(((((3,), 3, (-2,)), 5, (2, (1,))), 10, (-3, (11,)))),
        8
    ))
