from data_structure import ListNode
from data_structure import build_link_list
from data_structure import ds_print


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # get length
        p = head
        ll = 0
        while p is not None:
            ll += 1
            p = p.next
        on = ll + 1 - n
        # delete node
        p = ListNode(0)
        p.next = head
        q = p
        for _ in range(1, on):
            q = q.next
        q.next = q.next.next
        return p.next


if __name__ == "__main__":
    ds_print(Solution().removeNthFromEnd(build_link_list([1, 2, 3, 4, 5]), 2))
