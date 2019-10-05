from data_structure import ListNode, build_link_list, ds_print


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Merge sort is easier to implentment than others
        if head is None or head.next is None:
            return head
        # Split
        p, q = head, head.next
        while q is not None and q.next is not None:
            p = p.next
            q = q.next
            if q is not None:
                q = q.next
        q = p.next
        p.next = None 
        # Sort
        p, q = self.sortList(head), self.sortList(q)
        # Merge
        head = ListNode(0)
        tail = head
        while p is not None or q is not None:
            if p is None:
                tail.next = q
                q = q.next
            elif q is None:
                tail.next = p
                p = p.next
            else:
                if p.val < q.val:
                    tail.next = p
                    p = p.next
                else:
                    tail.next = q
                    q = q.next
            tail = tail.next
            tail.next = None
        return head.next
        
        
if __name__ == "__main__":
    ds_print(Solution().sortList(build_link_list([])))
    ds_print(Solution().sortList(build_link_list([4])))
    ds_print(Solution().sortList(build_link_list([4, 2, 1, 3])))
    ds_print(Solution().sortList(build_link_list([-1, 5, 3, 4, 0])))
