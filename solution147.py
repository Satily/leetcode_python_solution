from data_structure import ListNode, build_link_list, ds_print


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        sorted_head = head
        head = head.next
        sorted_head.next = None
        while head is not None:
            current = head
            head = head.next
            current.next = None
            if current.val <= sorted_head.val:
                current.next = sorted_head
                sorted_head = current
            else:
                p = sorted_head
                while p.next is not None and current.val > p.next.val:
                    p = p.next
                current.next = p.next
                p.next = current
        return sorted_head
            
        

if __name__ == "__main__":
    ds_print(Solution().insertionSortList(build_link_list([4, 2, 1, 3])))
    ds_print(Solution().insertionSortList(build_link_list([-1, 5, 3, 4, 0])))
