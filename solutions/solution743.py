from queue import PriorityQueue
import sys


class HeapItem(object):
    def __init__(self, index, distance=0):
        self.index = index
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance


class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        nodes = [dict() for _ in range(N)]
        for u, v, w in times:
            nodes[u - 1][v - 1] = w
        K -= 1
        heap = PriorityQueue()
        heap.put(HeapItem(K, 0))
        distances = [sys.maxsize] * N
        distances[K] = True, 0
        while not heap.empty():
            index = heap.get().index
            for out_node, time in nodes[index].items():
                distance = distances[index] + time
                if distance < distances[out_node]:
                    distances[out_node]
        return nodes


if __name__ == "__main__":
    print(Solution().networkDelayTime(
        [
            [1, 2, 4],
            [2, 3, 5],
            [3, 2, 3],
            [1, 3, 3],
            [1, 4, 6],
            [2, 4, 3],
            [4, 3, 4],
        ],
        4,
        1
    ))
