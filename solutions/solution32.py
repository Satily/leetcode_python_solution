class Solution:
    def longestValidParentheses(self, s: 'str') -> 'int':
        ls = len(s)
        seeds, new_seeds = [], []
        for i in range(ls - 1):
            if s[i: i + 2] == '()':
                seeds.append((i, i + 1))

        res, growing = 0, True
        while growing:
            growing = False
            for seed in seeds:
                growing_seed = seed
                while growing_seed[0] > 0 and growing_seed[1] < ls - 1 and s[growing_seed[0] - 1] == "(" and s[growing_seed[1] + 1] == ')':
                    growing_seed = (growing_seed[0] - 1, growing_seed[1] + 1)
                    growing = True
                if len(new_seeds) > 0 and new_seeds[-1][1] + 1 == growing_seed[0]:
                    left, _ = new_seeds.pop()
                    growing_seed = (left, growing_seed[1])
                    growing = True
                new_seeds.append(growing_seed)
            seeds, new_seeds = new_seeds, []
            res = max(map(lambda x: x[1] - x[0] + 1, seeds + [(0, -1)]))
        return res


if __name__ == "__main__":
    print(Solution().longestValidParentheses(""))
    print(Solution().longestValidParentheses(")()())"))
    print(Solution().longestValidParentheses("()()())"))
    print(Solution().longestValidParentheses("((())(()))(())())"))
    print(Solution().longestValidParentheses("()(()(((((())())((()))(()((())()(()()(()((()))()))))())))))())()())))(()()()())((()()()))()(()(()))())(((()))())(()((()))(()(()))()"))
    print(Solution().longestValidParentheses("())()()(())((()(()()(((()))((((())((()(())()())(()((((()))()(()))(())()(())(()(((((())((((((()())())(()(()((())()))(()))))))()(()))((((())()()()))()()()(((()(()())(()()(()(()()(((()))))))()()))())())((()()))))))((()))(((()((())()(()()))((())))()()())))))))()))))(()))))()))()))()((())))((()))(()))))))(((()))))))))()(()()()(())((())()))()()(())))()()))(()())()))(((()())()))((())((((()))(()(()(()()()(((())()(((((()))((()(((((())(()()))((((((((()(()(()(()(())))(())(()())())(()((((()(())((()(())))(())))()(((((()(()()(())))))))())(())(())(()()(((())))((()))(((((()))))())))()((()))()))))())))))((())(((((()()))((((())))(((()(()(())())(((()(()(()()()())))())()))((()((())())()()()(((())(((((()((((((()((()())))((((())((()(((((((()(()((()()()(()(()())(()(()()((((())))()(((()())))(()()))()(()()()()(((((())(()))))((()))())))()((((((()))())))()(()))(())))((((()())(((((()()())(((((())(()())(()))))()(()()))()))))))())))(((())(()(()()))(()))()(((())))())((((()(((()))))))()(()(()))()()(()()))))))))((()))))))(())((()((()))()))((((((()())))))(()((())((((()))))(()(()()()()(()))()()(()(()))(()()(((((((()())(())(()())((())())()(()())((())()())())(()())))())))(())())())(())((()())(((()()))()))()()))()(()(())((((((((())))()((())((()((((((((((()))))(()(((((())(()(()())())))((())())))))()))(()((()()))((()((())()()()((()(())())((())())(()()(((())))))())()()(()))()())(()(()((())))((((()()(())))())(())(()(()(())())())(()()())()(())())))(()()(((())))((()()(((())()()(()())((((()()(()())(()((((()(()()(()(()(((()((()())(()()))(()((((()(((((()))))()()))(((()((((((()(()()()()())()))(()(())))))((()(((()())())))(((()()))(()(()(((((((()()))(()(())))())()(())())(())(()))(())(()))()()(()()())))))()))()((())(((()((((((((())()()))())))((()())("))
