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
        stack = []
        symbols = {'+', '-', ')'}
        for e in ExpressionParser(s + '+'):
            if e in symbols and len(stack) >= 3 and stack[-2] in symbols:
                a, symbol, b = stack[-3:]
                stack = stack[:-3]
                if symbol == '+':
                    stack.append(a + b)
                else:
                    stack.append(a - b)
            if e == ')':
                stack.pop(-2)
            else:
                stack.append(e)
        return stack[0]


if __name__ == "__main__":
    print(Solution().calculate('(1)'))
    print(Solution().calculate('1 + 1'))
    print(Solution().calculate(' 2-1 + 2 '))
    print(Solution().calculate('(1+(4+5+2)-3)+(6+8)'))
