from data_structure import ListNode, ds_print, build_link_list


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_head, even_head = ListNode(0), ListNode(0)        
        index = 0
        p = head
        odd_p, even_p = odd_head, even_head
        while p is not None:
            if index & 1 == 0:
                even_p.next = p
                even_p = even_p.next
            else:
                odd_p.next = p
                odd_p = odd_p.next
            p = p.next
            index += 1
        odd_p.next = None
        even_p.next = odd_head.next
        return even_head.next
        


if __name__ == "__main__":
    ds_print(Solution().oddEvenList(build_link_list([1,2,3,4,5])))
    ds_print(Solution().oddEvenList(build_link_list([2,1,3,5,6,4,7])))