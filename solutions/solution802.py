from queue import Queue

class Solution:
    def eventualSafeNodes(self, graph: 'List[List[int]]') -> 'List[int]':
        backward_graph = [[] for _ in range(len(graph))]
        for in_node, out_nodes in enumerate(graph):
            for out_node in out_nodes:
                backward_graph[out_node].append(in_node)

        result = []
        end_node_queue = Queue()
        for end_node, _ in filter(lambda x: len(x[1]) == 0, enumerate(graph)):
            end_node_queue.put(end_node)
            result.append(end_node)
        unchecked_out_edges = list(map(lambda x: len(x), graph))

        while not end_node_queue.empty():
            current = end_node_queue.get()
            for in_node in backward_graph[current]:
                unchecked_out_edges[in_node] -= 1
                if unchecked_out_edges[in_node] == 0:
                    end_node_queue.put(in_node)
                    result.append(in_node)

        result.sort()
        return result


if __name__ == "__main__":
    print(Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
