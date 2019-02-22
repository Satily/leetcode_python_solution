class ExpressionParser(object):
    def __init__(self, expression):
        self.expression = expression.strip()

    def __iter__(self):
        num_set = {str(i) for i in range(10)}
        if self.expression[0] in num_set:
            s = int(self.expression[0])
        else:
            s = self.expression[0]
        for ch in self.expression[1:]:
            if ch != ' ':
                if ch in num_set and isinstance(s, int):
                    s = s * 10 + int(ch)
                else:
                    yield s
                    if ch in num_set:
                        s = int(ch)
                    else:
                        s = ch
        yield s


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        levels = {
            '+': 0,
            '-': 0,
            '*': 1,
            '/': 1,
        }
        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a // b,
        }
        stack = []
        for e in ExpressionParser(s + '+'):
            while isinstance(e, str) and len(stack) >= 3 and levels[e] <= levels[stack[-2]]:
                a, symbol, b = stack[-3:]
                stack = stack[:-3]
                stack.append(operators[symbol](a, b))
            stack.append(e)
        return stack[0]


if __name__ == "__main__":
    print(Solution().calculate('3+2*2'))
    print(Solution().calculate(' 3/2 '))
    print(Solution().calculate(' 3+5 / 2 '))
