from data_structure import ListNode, build_link_list, ds_print


class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        if head is None:
            return None
        p = ListNode(0)
        p.next = head
        head = p
        while p.next is not None and p.next.next is not None:
            if p.next.val == p.next.next.val:
                current = p.next.val
                while p.next.next is not None and p.next.next.val == current:
                    p.next.next = p.next.next.next
                p.next = p.next.next
            else:
                p = p.next
        return head.next


if __name__ == "__main__":
    # ds_print(Solution().deleteDuplicates(build_link_list([])))
    ds_print(Solution().deleteDuplicates(build_link_list([1, 1])))
    ds_print(Solution().deleteDuplicates(build_link_list([1, 2, 3, 3, 4, 4, 5])))
    ds_print(Solution().deleteDuplicates(build_link_list([1, 1, 1, 2, 3])))
