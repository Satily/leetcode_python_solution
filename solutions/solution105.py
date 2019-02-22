from data_structure import TreeNode, ds_print


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def find(l, v):
            for index, ele in enumerate(l):
                if ele == v:
                    return index
            return -1

        if len(preorder) == 0 or len(inorder) == 0:
            return None
        node = TreeNode(preorder[0])
        index = find(inorder, preorder[0])
        node.left = self.buildTree(preorder[1: index + 1], inorder[:index])
        node.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return node


if __name__ == "__main__":
    ds_print(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
