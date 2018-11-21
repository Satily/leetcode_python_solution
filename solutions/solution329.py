from itertools import product, chain


class GraphNode(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.out_edges = set()
        self.in_edge_number = 0
        self.longest_path_length = 1


class Graph(object):
    def __init__(self, m, n):
        self.nodes = [[GraphNode(x, y) for y in range(n)] for x in range(m)]
        self.zero_in_edge_nodes = []


class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        graph = Graph(m, n)
        for x, y, d in product(range(m), range(n), directions):
            nx, ny = x + d[0], y + d[1]
            if 0 <= x + d[0] < m and 0 <= y + d[1] < n and matrix[x][y] < matrix[nx][ny]:
                graph.nodes[x][y].out_edges.add((nx, ny))
                graph.nodes[nx][ny].in_edge_number += 1
        graph.zero_in_edge_nodes = list(
            map(
                lambda x: (x.x, x.y),
                filter(
                    lambda x: x.in_edge_number == 0,
                    chain.from_iterable(graph.nodes)
                )
            )
        )
        while len(graph.zero_in_edge_nodes) != 0:
            x, y = graph.zero_in_edge_nodes.pop()
            current_node = graph.nodes[x][y]
            for next_node in map(lambda c: graph.nodes[c[0]][c[1]], current_node.out_edges):
                next_node.in_edge_number -= 1
                next_node.longest_path_length = max(next_node.longest_path_length, current_node.longest_path_length + 1)
                if next_node.in_edge_number == 0:
                    graph.zero_in_edge_nodes.append((next_node.x, next_node.y))
        return max(map(lambda x: x.longest_path_length, chain.from_iterable(graph.nodes)))


if __name__ == "__main__":
    print(Solution().longestIncreasingPath([
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]))
    print(Solution().longestIncreasingPath([
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ]))
