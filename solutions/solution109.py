from data_structure import TreeNode, ListNode, build_link_list, ds_print


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        p = head
        while p is not None:
            nums.append(p.val)
            p = p.next
        return self.sortedArrayToBST(nums)

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        mid_index = len(nums) >> 1
        node = TreeNode(nums[mid_index])
        node.left = self.sortedArrayToBST(nums[:mid_index])
        node.right = self.sortedArrayToBST(nums[mid_index + 1:])
        return node


if __name__ == "__main__":
    ds_print(Solution().sortedListToBST(build_link_list([-10, -3, 0, 5, 9])))
