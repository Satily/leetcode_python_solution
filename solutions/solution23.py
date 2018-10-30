
from data_structure import ListNode
from data_structure import build_link_list
from data_structure import ds_print

from queue import PriorityQueue


class HeapItem(object):
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data

    def __lt__(self, other):
        return self.priority < other.priority


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = PriorityQueue()
        for list_item in lists:
            if list_item is not None:
                heap.put(HeapItem(list_item.val, list_item))
        p = result_head = ListNode(0)
        while not heap.empty():
            current = heap.get()
            p.next = current.data
            if current.data.next is not None:
                heap.put(HeapItem(current.data.next.val, current.data.next))
            p = p.next
            p.next = None
        return result_head.next


if __name__ == "__main__":
    # ds_print(Solution().mergeKLists([
    #     build_link_list([1, 4, 5]),
    #     build_link_list([1, 3, 4]),
    #     build_link_list([2, 6])
    # ]))
    ds_print(Solution().mergeKLists([
        build_link_list([])
    ]))
