from data_structure import TreeNode, build_binary_tree, ds_print


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def search_path(r, v, p):
            result = []
            if r is not None:
                if r.left is None and r.right is None:
                    if v == r.val:
                        item = p.copy()
                        item.append(r.val)
                        result.append(item)
                else:
                    p.append(r.val)
                    result.extend(search_path(r.left, v - r.val, p))
                    result.extend(search_path(r.right, v - r.val, p))
                    p.pop()
            return result
        return search_path(root, sum, [])


if __name__ == "__main__":
    root = build_binary_tree(
        ((((7,), 11, (2,)), 4), 5, ((13,), 8, ((5,), 4, (1,))))
    )
    print(Solution().pathSum(root, 22))
