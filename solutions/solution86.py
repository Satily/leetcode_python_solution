from data_structure import build_link_list, ListNode, ds_print


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p0, p1 = ListNode(0), ListNode(0)
        head0, head1 = p0, p1
        while head is not None:
            if head.val < x:
                p0.next = head
                p0 = p0.next
            else:
                p1.next = head
                p1 = p1.next
            head = head.next
        p0.next = head1.next
        p1.next = None
        return head0.next


if __name__ == "__main__":
    ds_print(Solution().partition(build_link_list([1, 4, 3, 2, 5, 2]), 3))
