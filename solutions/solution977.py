class Solution:
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        la = len(A)
        if la == 0:
            return []

        result = []
        n0, n1 = A[0] ** 2, A[la - 1] ** 2
        p0, p1 = 1, la - 2
        while p0 - p1 < 2:
            if n0 > n1:
                result.append(n0)
                n0 = A[p0] ** 2
                p0 += 1
            else:
                result.append(n1)
                n1 = A[p1] ** 2
                p1 -= 1

        result.append(n0)
        result.reverse()
        return result


if __name__ == "__main__":
    print(Solution().sortedSquares([]))
    print(Solution().sortedSquares([-4]))
    print(Solution().sortedSquares([-4, -1]))
    print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
    print(Solution().sortedSquares([-7, -3, 2, 3, 11]))
