from data_structure import ListNode, build_link_list, flatten_link_list


class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        def split(h, lh):
            if h is not None:
                p = h
                for _ in range(lh - 1):
                    p = p.next
                q = p.next
                p.next = None
                return q, h
            else:
                return None, None

        lr, p = 0, root
        while p is not None:
            p, lr = p.next, lr + 1
        n, r = lr // k, lr % k
        result = []
        for i in range(k):
            l = n
            if i < r:
                l += 1
            root, head = split(root, l)
            result.append(head)
        return result



if __name__ == "__main__":
    inputs = [
        # ([1, 2, 3], 5),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3),
    ]
    for root_list, k in inputs:
        root = build_link_list(root_list)
        result = [flatten_link_list(head) for head in Solution().splitListToParts(root, k)]
        print(result)
