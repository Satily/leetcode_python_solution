from data_structure import ListNode, build_link_list, ds_print


class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        p = head
        while p is not None and p.next is not None:
            while p.next is not None and p.next.val == p.val:
                p.next = p.next.next
            p = p.next
        return head


if __name__ == "__main__":
    ds_print(Solution().deleteDuplicates(build_link_list([1, 1, 2])))
    ds_print(Solution().deleteDuplicates(build_link_list([1, 1, 2, 3, 3])))
