from data_structure import ListNode, build_link_list, ds_print


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p, q, r = head, head.next, head.next.next
        while q is not None:
            q.next = p
            p, q = q, r
            if r is not None:
                r = r.next
        head.next = None
        return p


if __name__ == "__main__":
    ds_print(Solution().reverseList(build_link_list([1, 2, 3, 4, 5])))
    ds_print(Solution().reverseList(build_link_list([1, 2])))
    ds_print(Solution().reverseList(build_link_list([1])))
    ds_print(Solution().reverseList(build_link_list([])))
