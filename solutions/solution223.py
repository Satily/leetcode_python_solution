class Solution:
    def computeArea(self, A: 'int', B: 'int', C: 'int', D: 'int', E: 'int', F: 'int', G: 'int', H: 'int') -> 'int':
        a, b = min(C, G) - max(A, E), min(D, H) - max(B, F)
        result = (C - A) * (D - B) + (G - E) * (H - F)
        if a > 0 and b > 0:
            result -= a * b
        return result


if __name__ == "__main__":
    print(Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
