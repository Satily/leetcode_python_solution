class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        if m == 0:
            return []
        n = len(A[0])
        if n == 0:
            return []
        return [[A[j][i] for j in range(m)] for i in range(n)]


if __name__ == "__main__":
    print(Solution().transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(Solution().transpose([[1, 2, 3], [4, 5, 6]]))
