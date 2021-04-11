class Solution:
    def grayCode(self, n: int) -> 'List[int]':
        if n == 0:
            return [0]
        result = [0, 1]
        for i in range(1, n):
            head = 2 ** i
            result.extend(map(lambda x: head + x, reversed(result)))
        return result


if __name__ == "__main__":
    print(Solution().grayCode(2))
    print(Solution().grayCode(0))
    print(Solution().grayCode(1))
    print(Solution().grayCode(3))
    print(Solution().grayCode(4))
