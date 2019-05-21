class LRUUnit:
    def __init__(self, key, value, prev = None, next = None):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value     

class LRUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.head = LRUUnit("head sentinel", "head sentinel")
        self.tail = LRUUnit("tail sentinel", "tail sentinel")
        self.tail.prev = self.head
        self.head.next = self.tail
        self.cache = dict()

    def __push(self, unit) -> None:
        next_unit = self.head.next
        self.head.next = unit
        next_unit.prev = unit
        unit.prev, unit.next = self.head, next_unit

    def __remove(self, unit: LRUUnit) -> LRUUnit:
        prev_unit = unit.prev
        next_unit = unit.next
        prev_unit.next = next_unit
        next_unit.prev = prev_unit
        unit.prev, unit.next = None, None
        return unit

    def __move_to_front(self, unit) -> LRUUnit:
        self.__remove(unit)
        self.__push(unit)
        return unit

    def get(self, key: int) -> int:
        if key in self.cache:            
            return self.__move_to_front(self.cache[key]).value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.__move_to_front(self.cache[key])
            return
        unit = LRUUnit(key, value)        
        if self.size == self.capacity:
            poped_unit = self.__remove(self.tail.prev)
            del self.cache[poped_unit.key]
            self.size -= 1
        self.__push(unit)
        self.cache[key] = unit
        self.size += 1
        



if __name__ == "__main__":
    operators = ["LRUCache","put","put","put","put","get","get"]
    parameters = [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]

    for i in range(len(operators)):
        operator, parameter = operators[i], parameters[i]
        if operator == "LRUCache":
            cache = LRUCache(parameter[0])
            print("null")
        elif operator == "put":
            cache.put(parameter[0], parameter[1])
            print("null")
        elif operator == "get":
            print(cache.get(parameter[0]))
