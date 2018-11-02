from data_structure import ListNode, build_link_list, ds_print


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Get Length
        p = head
        ll = 0
        while p is not None:
            p = p.next
            ll += 1
        # reverse
        p = head
        head = ListNode(0)
        head.next = p
        prev_end = head
        for i in range(0, ll // k):
            cur_start = cur_end = prev_end.next
            for j in range(0, k - 1):
                cur_end = cur_end.next
            if cur_end is None:
                next_start = None
            else:
                next_start = cur_end.next
            p, q, r = prev_end, prev_end.next, prev_end.next.next
            for j in range(0, k):
                q.next = p
                p, q = q, r
                if r is not None:
                    r = r.next
            cur_start.next = next_start
            prev_end.next = cur_end
            prev_end = cur_start
        return head.next


if __name__ == "__main__":
    ds_print(Solution().reverseKGroup(build_link_list([1, 2, 3, 4, 5]), 2))
    ds_print(Solution().reverseKGroup(build_link_list([1, 2, 3, 4, 5]), 3))
    ds_print(Solution().reverseKGroup(build_link_list([1, 2, 3, 4, 5, 6]), 3))
    ds_print(Solution().reverseKGroup(build_link_list([1, 2, 3, 4, 5]), 1))
