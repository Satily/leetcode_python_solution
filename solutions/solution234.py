from data_structure import ListNode, build_link_list


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next
        for i in range(len(nums) // 2):
            if nums[i] != nums[len(nums) - 1 - i]:
                return False
        return True


if __name__ == "__main__":
    print(Solution().isPalindrome(build_link_list([1, 2])))
    print(Solution().isPalindrome(build_link_list([1, 2, 2, 1])))
