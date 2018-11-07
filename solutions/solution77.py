class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 0 or n < k:
            return []
        result, line = [], [0]
        while line:
            line[-1] += 1
            while len(line) != k:
                line.append(line[-1] + 1)
            result.append(line.copy())
            while line and line[-1] >= n - k + len(line):
                line.pop()
        return result


if __name__ == "__main__":
    print(Solution().combine(4, 3))
