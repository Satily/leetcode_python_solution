class DoubleLinkListNode:
    def __init__(self, value, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next


class DoubleLinkList:
    def __init__(self):
        self.head = DoubleLinkListNode(None)
        self.tail = DoubleLinkListNode(None)
        self.head.next = self.tail
        self.tail.previous = self.head
        self.size = 0

    def push_front(self, value):
        p = DoubleLinkListNode(value, self.head, self.head.next)
        self.head.next.previous = p
        self.head.next = p
        self.size += 1

    def pop_front(self):
        if self.size > 0:
            p = self.head.next
            self.head.next.next.previous = self.head
            self.head.next = p.next
            del p
            self.size -= 1

    def swap_next(self, p):
        q = p.next
        p.previous.next, q.next.previous = q, p
        p.next, q.previous = q.next, p.previous
        p.previous, q.next = q, p

    def to_list(self):
        result = []
        p = self.head
        for _ in range(self.size):
            result.append(p.next.value)
            p = p.next
        return result


class LFUCache:
    def __init__(self, capacity: 'int'):
        self.capacity = capacity
        self.index = {}
        self.pieces = DoubleLinkList()

    def __refresh(self, key):
        self.index[key].value = (self.index[key].value[0], self.index[key].value[1], self.index[key].value[2] + 1)
        while self.index[key].next.value is not None and self.index[key].value[2] >= self.index[key].next.value[2]:
            self.pieces.swap_next(self.index[key])

    def get(self, key: 'int') -> 'int':
        if key in self.index:
            self.__refresh(key)
            return self.index[key].value[1]
        else:
            return -1

    def put(self, key: 'int', value: 'int') -> 'None':
        if self.capacity == 0:
            return
        if key in self.index:
            self.index[key].value = (self.index[key].value[0], value, self.index[key].value[2])
        else:
            if len(self.index) == self.capacity:
                k = self.pieces.head.next.value[0]
                del self.index[k]
                self.pieces.pop_front()
            self.pieces.push_front((key, value, 0))
            self.index[key] = self.pieces.head.next
        self.__refresh(key)



if __name__ == "__main__":
    # ll = DoubleLinkList()
    # ll.push_front(1)
    # ll.push_front(2)
    # ll.push_front(3)
    # ll.push_front(4)
    # print(ll.to_list())
    # ll.swap_next(ll.head.next)
    # print(ll.to_list())
    # ll.pop_front()
    # print(ll.to_list())
    # ll.swap_next(ll.head.next.next)
    # print(ll.to_list())

    cache = LFUCache(2)
    cache.put(3, 1)
    cache.put(2, 1)
    cache.put(2, 2)
    cache.put(4, 4)
    print(cache.get(2))
    # cache.put(1, 5)
    # cache.put(2, 6)
    # print(cache.get(1))
    # cache.put(3, 7)
    # print(cache.get(2))
    # print(cache.get(3))
    # cache.put(4, 8)
    # print(cache.get(1))
    # print(cache.get(3))
    # print(cache.get(4))
