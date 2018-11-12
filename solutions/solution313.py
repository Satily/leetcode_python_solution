from queue import PriorityQueue


class HeapItem(object):
    def __init__(self, value, last_index):
        self.value = value
        self.last_index = last_index

    def __lt__(self, other):
        return self.value < other.value


class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        heap = PriorityQueue()
        heap.put(HeapItem(1, 0))
        for time in range(n - 1):
            current = heap.get()
            for prime_index in range(current.last_index, len(primes)):
                heap.put(HeapItem(current.value * primes[prime_index], prime_index))
        return heap.get().value


if __name__ == "__main__":
    print(Solution().nthSuperUglyNumber(12, [2, 7, 13, 19]))
    print(Solution().nthSuperUglyNumber(100000,
                                        [7, 19, 29, 37, 41, 47, 53, 59, 61, 79, 83, 89, 101, 103, 109, 127, 131, 137,
                                         139, 157, 167, 179, 181, 199, 211, 229, 233, 239, 241, 251]))
