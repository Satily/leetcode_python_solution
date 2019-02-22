from itertools import product


class ExpressionParser(object):
    def __init__(self, expression):
        self.expression = expression

    def __iter__(self):
        num = 0
        symbol_set = {'+', '-', '*'}
        for ch in self.expression:
            if ch in symbol_set:
                yield num
                yield ch
                num = 0
            else:
                num = num * 10 + int(ch)
        yield num


class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
        }
        parsed_expression = list(ExpressionParser(input))
        nums = parsed_expression[::2]
        symbols = parsed_expression[1::2]
        dp = [[[] for _ in range(len(nums))] for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i] = [nums[i]]
        for l in range(2, len(nums) + 1):
            for i in range(len(nums) + 1 - l):
                for k in range(i, i + l - 1):
                    r = [operators[symbols[k]](lnum, rnum) for lnum, rnum in product(dp[i][k], dp[k + 1][i + l - 1])]
                    dp[i][i + l - 1].extend(r)
        return list(sorted(dp[0][len(nums) - 1]))


if __name__ == "__main__":
    print(Solution().diffWaysToCompute("2-1-1"))
    print(Solution().diffWaysToCompute("2*3-4*5"))
