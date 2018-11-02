from data_structure import ListNode, build_link_list, ds_print


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        head = ListNode(0)
        head.next = p
        p = head
        while p.next is not None and p.next.next is not None:
            tp1, tp2, q = p.next, p.next.next, p.next.next.next
            p.next, tp2.next, tp1.next = tp2, tp1, q
            p = tp1
        return head.next


if __name__ == "__main__":
    ds_print(Solution().swapPairs(build_link_list([1, 2, 3, 4])))
    ds_print(Solution().swapPairs(build_link_list([1, 2, 3, 4, 5])))
