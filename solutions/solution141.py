from data_structure import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p, q = head, head
        while q is not None:
            p = p.next
            q = q.next if q.next is None else q.next.next
            if q is None:
                return False
            if p == q:
                return True
        return False


if __name__ == "__main__":
    # Example 1
    n0, n1, n2, n3 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    n0.next, n1.next, n2.next, n3.next = n1, n2, n3, n1
    print(Solution().hasCycle(n0))
    # Example 2
    n0, n1 = ListNode(1), ListNode(2)
    n0.next, n1.next = n1, n0
    print(Solution().hasCycle(n0))
    # Example 3
    n0 = ListNode(1)
    print(Solution().hasCycle(n0))