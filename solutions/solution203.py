from data_structure import ListNode, build_link_list, ds_print


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = head
        head = ListNode(0)
        head.next = p
        p = head
        while p is not None and p.next is not None:
            while p.next is not None and p.next.val == val:
                p.next = p.next.next
            p = p.next
        return head.next


if __name__ == "__main__":
    ds_print(Solution().removeElements(build_link_list([1, 2, 6, 3, 4, 5, 6]), 6))
    ds_print(Solution().removeElements(build_link_list([1, 1]), 1))
