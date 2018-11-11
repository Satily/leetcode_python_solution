from data_structure import ListNode, build_link_list, ds_print


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = head
        # head = ListNode(-1)
        # head.next = p
        lh = 0
        while p is not None:
            p = p.next
            lh += 1
        if lh == 0:
            return []
        k %= lh
        k = lh - k - 1
        p = head
        for _ in range(k):
            p = p.next
        q = p
        while q.next is not None:
            q = q.next
        q.next = head
        head = p.next
        p.next = None
        return head


if __name__ == "__main__":
    ds_print(Solution().rotateRight(build_link_list([1, 2, 3, 4, 5]), 2))
    ds_print(Solution().rotateRight(build_link_list([0, 1, 2]), 4))
    ds_print(Solution().rotateRight(build_link_list([0, 1, 2]), 0))
    ds_print(Solution().rotateRight(build_link_list([0]), 4))
    ds_print(Solution().rotateRight(build_link_list([0]), 0))
    ds_print(Solution().rotateRight(build_link_list([]), 0))
