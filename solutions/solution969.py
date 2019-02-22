class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def flip(p, n):
            return list(reversed(p[:n])) + p[n:]

        la = len(A)
        result = []
        for current in reversed(range(1, la + 1)):
            ci = current
            for index, num in enumerate(A):
                if num == current:
                    ci = index
                    break
            if ci + 1 != current:
                result.append(ci + 1)
                A = flip(A, ci + 1)
                result.append(current)
                A = flip(A, current)
        return [item for item in result if item != 1]


if __name__ == "__main__":
    print(Solution().pancakeSort([3, 2, 4, 1]))
    print(Solution().pancakeSort([1, 2, 3]))
