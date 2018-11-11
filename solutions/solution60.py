class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s = 1
        k -= 1
        factors = [1]
        for i in range(1, n):
            s *= i
            factors.append(s)
        factors.reverse()
        flags = [True] * n
        result = []
        for i in range(n):
            t = k // factors[i]
            for j in range(len(flags)):
                if flags[j]:
                    if t == 0:
                        flags[j] = False
                        result.append(j)
                        break
                    t -= 1
            k %= factors[i]
        return ''.join(map(lambda x: str(x + 1), result))


if __name__ == "__main__":
    print(Solution().getPermutation(3, 3))
    print(Solution().getPermutation(4, 9))
    print(Solution().getPermutation(3, 1))
    print(Solution().getPermutation(3, 6))
