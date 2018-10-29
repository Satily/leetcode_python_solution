class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_link_list(nums):
    head = ListNode(0)
    p = head
    for item in nums:
        p.next = ListNode(item)
        p = p.next
    return head.next


def flatten_link_list(link_list):
    p = link_list
    result = []
    while p is not None:
        result.append(p.val)
        p = p.next
    return result
