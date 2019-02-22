from data_structure import TreeNode, ds_print


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def find(l, v):
            for index, ele in enumerate(l):
                if ele == v:
                    return index
            return -1

        if len(postorder) == 0 or len(inorder) == 0:
            return None
        node = TreeNode(postorder[-1])
        index = find(inorder, postorder[-1])
        node.left = self.buildTree(inorder[:index], postorder[: index])
        node.right = self.buildTree(inorder[index + 1:], postorder[index: -1])
        return node


if __name__ == "__main__":
    ds_print(Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))
