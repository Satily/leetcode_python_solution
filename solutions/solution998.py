from data_structure import TreeNode, build_binary_tree, ds_print, null


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or root is not None and root.val < val:
            node = TreeNode(val)
            node.left = root
            return node
        root.right = self.insertIntoMaxTree(root.right, val)
        return root


if __name__ == "__main__":
    ds_print(Solution().insertIntoMaxTree(root = build_binary_tree([4,1,3,null,null,2]), val = 5))
    ds_print(Solution().insertIntoMaxTree(root = build_binary_tree([5,2,4,null,1]), val = 3))
    ds_print(Solution().insertIntoMaxTree(root = build_binary_tree([5,2,3,null,1]), val = 4))
    