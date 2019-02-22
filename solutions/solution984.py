class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        result = ""
        if A >= B:
            turn = False
        else:
            turn = True
        while A != 0 or B != 0:
            if not turn:
                d = min(max(min(A - B, 2), 1), A)
                A -= d
                result += "a" * d
            else:
                d = min(max(min(B - A, 2), 1), B)
                B -= d
                result += "b" * d
            turn = not turn
        return result


if __name__ == "__main__":
    print(Solution().strWithout3a3b(1, 2))
    print(Solution().strWithout3a3b(4, 1))
