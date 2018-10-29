from data_structure import ListNode
from data_structure import build_link_list
from data_structure import ds_print


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        p = head
        c = 0
        l1c = l1
        l2c = l2
        while l1c is not None and l2c is not None:
            s = l1c.val + l2c.val + c
            c = s // 10
            p.next = ListNode(s % 10)
            p = p.next
            l1c = l1c.next
            l2c = l2c.next
        if l1c is None:
            q = l2c
        else:
            q = l1c
        while q is not None:
            s = q.val + c
            c = s // 10
            p.next = ListNode(s % 10)
            p = p.next
            q = q.next
        if c != 0:
            p.next = ListNode(c)
        return head.next


if __name__ == "__main__":
    l1 = build_link_list([2, 4, 3])
    l2 = build_link_list([5, 6, 4])
    ds_print(Solution().addTwoNumbers(l1, l2))
    l1 = build_link_list([2])
    l2 = build_link_list([9, 9, 9, 9, 9, 9, 1])
    ds_print(Solution().addTwoNumbers(l1, l2))
    l1 = build_link_list([9, 9])
    l2 = build_link_list([1, 1])
    ds_print(Solution().addTwoNumbers(l1, l2))
