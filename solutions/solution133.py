from data_structure.graph_node import Node


from queue import Queue


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_graph = {}        
        scaned_queue = Queue()
        scaned_queue.put(node)
        while not scaned_queue.empty():
            current_node = scaned_queue.get()        
            old_graph[current_node.val] = current_node
            for target_node in current_node.neighbors:
                if target_node.val not in old_graph:
                    scaned_queue.put(target_node)
        
        new_graph = {value: Node(value, []) for value, _ in old_graph.items()}
        for value, old_graph_node in old_graph.items():
            for target_node in old_graph_node.neighbors:
                new_graph[value].neighbors.append(new_graph[target_node.val])
        return new_graph[node.val]


if __name__ == "__main__":
    node1 = Node(1, None)
    node2 = Node(2, None)
    node3 = Node(3, None)
    node4 = Node(4, None)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    result = Solution().cloneGraph(node1)
    print(result)
