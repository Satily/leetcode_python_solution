class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        push_bracket = set("([{")
        bracket_pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c in push_bracket:
                stack.append(c)
            if c in bracket_pairs:
                if len(stack) > 0 and stack[len(stack) - 1] == bracket_pairs[c]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    print(Solution().isValid('()'))
    print(Solution().isValid('()[]{}'))
    print(Solution().isValid('(]'))
    print(Solution().isValid('([)]'))
    print(Solution().isValid('{[]}'))
    print(Solution().isValid(']'))
