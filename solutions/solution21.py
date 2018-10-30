from data_structure import ListNode
from data_structure import build_link_list
from data_structure import ds_print


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = result = ListNode(0)
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1 is not None:
            p.next = l1
        elif l2 is not None:
            p.next = l2
        return result.next


if __name__ == "__main__":
    ds_print(Solution().mergeTwoLists(build_link_list([1, 2, 4]), build_link_list([1, 3, 4])))
