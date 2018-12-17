from data_structure import TreeNode, ds_print


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums is None or len(nums) == 0:
            return None
        mid_index = len(nums) >> 1
        node = TreeNode(nums[mid_index])
        node.left = self.sortedArrayToBST(nums[:mid_index])
        node.right = self.sortedArrayToBST(nums[mid_index + 1:])
        return node


if __name__ == "__main__":
    ds_print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))
