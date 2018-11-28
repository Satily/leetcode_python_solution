from functools import reduce


class ExpressionItem(object):
    def __init__(self, ratio, x=False):
        self.ratio = ratio
        self.x = x

    def __neg__(self):
        return ExpressionItem(-self.ratio, self.x)

    def __add__(self, other):
        if self.x == other.x:
            return ExpressionItem(self.ratio + other.ratio, self.x)
        else:
            return None

    @staticmethod
    def parse(s):
        s2 = s
        if s2[-1] == 'x':
            x = True
            s2 = s2[0:-1]
        else:
            x = False
        if s2 in {'', '-', '+'}:
            s2 += '1'
        ratio = int(s2)
        return ExpressionItem(ratio, x)


class ExpressionParser(object):
    def __init__(self, expression):
        self.expression = expression

    def __iter__(self):
        r = ''
        for c in self.expression:
            if c in {'+', '-'} and len(r) > 0:
                yield ExpressionItem.parse(r)
                r = ''
            r += c
        yield ExpressionItem.parse(r)


class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        e0, e1 = tuple(map(lambda x: list(ExpressionParser(x)), equation.split('=')))
        e0.extend(list(map(lambda x: -x, e1)))
        x_item = reduce(lambda x, y: x + y, filter(lambda x: x.x, e0), ExpressionItem(0, True))
        c_item = reduce(lambda x, y: x + y, filter(lambda x: not x.x, e0), ExpressionItem(0, False))
        if x_item.ratio == 0 and c_item.ratio == 0:
            return "Infinite solutions"
        elif x_item.ratio == 0:
            return "No solution"
        else:
            return 'x=%d' % (-c_item.ratio // x_item.ratio)
        # return str_expression(e0)


def str_expression(e):
    r = ''
    for i in e:
        if i.ratio >= 0:
            r += '+'
        r += str(i.ratio)
        if i.x:
            r += 'x'
    return r


if __name__ == "__main__":
    print(Solution().solveEquation("x+5-3+x=6+x-2"))
    print(Solution().solveEquation("x=x"))
    print(Solution().solveEquation("2x=x"))
    print(Solution().solveEquation("2x+3x-6x=x+2"))
    print(Solution().solveEquation("x=x+2"))
