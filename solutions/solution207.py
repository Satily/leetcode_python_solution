class Node(object):
    def __init__(self, no):
        self.no = no
        self.in_edges = set()
        self.out_edges = set()


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        nodes = [Node(index) for index in range(numCourses)]
        for prerequisite in prerequisites:
            nodes[prerequisite[1]].out_edges.add(prerequisite[0])
            nodes[prerequisite[0]].in_edges.add(prerequisite[1])
        stack = list(map(lambda x: x.no, filter(lambda x: len(x.in_edges) == 0, nodes)))
        result = []
        while len(stack) != 0:
            node_index = stack.pop()
            result.append(node_index)
            for out_node_index in nodes[node_index].out_edges:
                nodes[out_node_index].in_edges.remove(node_index)
                if len(nodes[out_node_index].in_edges) == 0:
                    stack.append(out_node_index)
            nodes[node_index].out_edges.clear()
        return len(result) == len(nodes)


if __name__ == "__main__":
    print(Solution().canFinish(2, [[1, 0]]))
    print(Solution().canFinish(2, [[1, 0], [0, 1]]))
