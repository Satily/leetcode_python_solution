class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 1:
            return [0]
        forward_star = [set() for _ in range(n)]
        for s, d in edges:
            forward_star[s].add(d)
            forward_star[d].add(s)
        leaves = list(map(lambda x: x[0], filter(lambda x: len(x[1]) == 1, enumerate(forward_star))))
        while n > 2:
            n -= len(leaves)
            n_leaves = []
            for leaf in leaves:
                for o in forward_star[leaf]:
                    forward_star[o].remove(leaf)
                    if len(forward_star[o]) == 1:
                        n_leaves.append(o)
                forward_star[leaf].clear()
            leaves = n_leaves
        return leaves


if __name__ == "__main__":
    print(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
    print(Solution().findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))