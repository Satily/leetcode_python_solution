from data_structure import ListNode, build_link_list, ds_print
from itertools import zip_longest


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def gen_list(node):
            res = []
            while node is not None:
                res.append(node)
                node = node.next
            return res

        l1_list, l2_list = gen_list(l1), gen_list(l2)
        ll1, ll2 = len(l1_list), len(l2_list)
        if ll1 < ll2:
            l1, l2 = l2, l1
            l1_list, l2_list = l2_list, l1_list
            ll1, ll2 = ll2, ll1
        c = 0
        for n1, n2 in zip_longest(reversed(l1_list), reversed(l2_list)):
            if n2 is not None:
                n1.val += n2.val + c
            else:
                n1.val += c
            c, n1.val = n1.val // 10, n1.val % 10
        if c != 0:
            l1, p = ListNode(c), l1
            l1.next = p
        return l1


if __name__ == "__main__":
    ds_print(Solution().addTwoNumbers(build_link_list([7, 2, 4, 3]), build_link_list([5, 6, 4])))
    ds_print(Solution().addTwoNumbers(build_link_list([1]), build_link_list([9, 9])))
    ds_print(Solution().addTwoNumbers(build_link_list([0]), build_link_list([0])))
