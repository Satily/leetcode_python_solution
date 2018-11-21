class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_link_list(*args):
    def build(nums):
        for num in nums:
            if not isinstance(num, int):
                raise RuntimeError("Unsupported type. %s." % nums)
        head = ListNode(0)
        p = head
        for item in nums:
            p.next = ListNode(item)
            p = p.next
        return head.next

    if len(args) == 1 and isinstance(args[0], list):
        return build(args[0])
    return build(list(args))


def flatten_link_list(link_list):
    if not isinstance(link_list, ListNode) and link_list is not None:
        raise RuntimeError("Unsupported type. %s." % link_list)
    p = link_list
    result = []
    while p is not None:
        result.append(p.val)
        p = p.next
    return result
