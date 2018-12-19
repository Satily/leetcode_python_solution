class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        avg = sum(A) / len(A)
        r1, r2 = [], []
        for a in A:
            if a > avg:
                r1.append(a - K)
                r2.append(a - K)
            elif a < avg:
                r1.append(a + K)
                r2.append(a + K)
            else:
                r1.append(a - K)
                r2.append(a + K)
        return min(max(r1) - min(r1), max(r2) - min(r2))



if __name__ == "__main__":
    print(Solution().smallestRangeII([1], 0))
    print(Solution().smallestRangeII([0, 10], 2))
    print(Solution().smallestRangeII([1, 3, 6], 3))
