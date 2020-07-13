from data_structure import ds_print, build_binary_tree, TreeNode


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def equal(n1, n2):
            return n1 is None and n2 is None or n1 is not None and n2 is not None and n1.val == n2.val        
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        result = True
        if equal(root1.left, root2.right) and equal(root1.right, root2.left):
            if root1.left is not None:
                result = result and self.flipEquiv(root1.left, root2.right)
            if root1.right is not None:
                result = result and self.flipEquiv(root1.right, root2.left)
        elif equal(root1.left, root2.left) and equal(root1.right, root2.right):
            if root1.left is not None:
                result = result and self.flipEquiv(root1.left, root2.left)
            if root1.right is not None:
                result = result and self.flipEquiv(root1.right, root2.right)
        else: 
            result = False
        return result


if __name__ == "__main__":
    print(Solution().flipEquiv(build_binary_tree("[]"), build_binary_tree("[]")))
    print(Solution().flipEquiv(build_binary_tree("[1,2,3,4,5,6,null,null,null,7,8]"), build_binary_tree("[1,3,2,null,6,4,5,null,null,null,null,8]")))