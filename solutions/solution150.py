from math import floor


class Solution:
    def evalRPN(self, tokens: 'List[str]') -> int:
        symbols = {'+', '-', '*', '/'}
        stack = []
        for token in tokens:
            if token not in symbols:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    num = a + b
                elif token == '-':
                    num = a - b
                elif token == '*':
                    num = a * b
                elif token == '/':
                    num = a / b
                    if num < 0:
                        num = -floor(-num)
                    else:
                        num = floor(num)
                stack.append(num)
        return stack.pop()


if __name__ == "__main__":
    print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
    print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
