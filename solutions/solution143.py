from data_structure import ListNode, build_link_list, ds_print


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None
        p, q = head, head.next
        while q is not None and q.next is not None:
            p = p.next
            q = q.next.next if q.next is not None else q.next

        head2 = p.next
        p.next = None
        
        p, q, r = None, head2, head2.next if head2 is not None else None
        while q is not None:
            q.next = p
            p = q
            q = r
            if r is not None:
                r = r.next
        head2 = p

        p = head
        while head2 is not None:
            q = p.next
            p.next = head2
            head2 = head2.next
            p.next.next = q
            p = q
            

if __name__ == "__main__":
    head = build_link_list([1,2,3,4])
    Solution().reorderList(head)
    ds_print(head)

    head = build_link_list([1,2,3,4,5])
    Solution().reorderList(head)
    ds_print(head)
