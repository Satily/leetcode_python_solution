from data_structure import ListNode, build_link_list, ds_print


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None or m == n:
            return head
        head, p = ListNode(0), head
        head.next = p
        p, q, r = head, head.next, head.next.next
        n -= m
        m -= 1
        while m > 0:
            p, q = q, r
            if r is not None:
                r = r.next
            m -= 1
        flag1, flag2 = p, q
        n += 1
        while n > 0:
            q.next = p
            n -= 1
            if n == 0:
                flag1.next, flag2.next = q, r
                break
            p, q = q, r
            if r is not None:
                r = r.next
        return head.next


if __name__ == "__main__":
    ds_print(Solution().reverseBetween(build_link_list([1, 2, 3, 4, 5]), 2, 4))
    ds_print(Solution().reverseBetween(build_link_list([1, 2, 3, 4, 5]), 4, 5))
    ds_print(Solution().reverseBetween(build_link_list([1, 2, 3, 4, 5]), 1, 2))
    ds_print(Solution().reverseBetween(build_link_list([1, 2, 3, 4, 5]), 1, 1))
