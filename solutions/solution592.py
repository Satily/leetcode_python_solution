from functools import reduce


def gcd(m, n):
    if m < n:
        m, n = n, m
    while n != 0:
        r = m % n
        m = n
        n = r
    return m


def lcm(m, n):
    return m // gcd(m, n) * n


class Fraction(object):
    def __init__(self, numerator, denominator, sign=None):
        if sign is not None and sign == "-":
            multiplier = -1
        else:
            multiplier = 1
        self.numerator = multiplier * numerator
        self.denominator = denominator

    def __add__(self, other):
        n0, d0, n1, d1 = self.numerator, self.denominator, other.numerator, other.denominator
        d = lcm(d0, d1)
        n = d // d0 * n0 + d // d1 * n1
        f = Fraction(n, d)
        f.reduce()
        return f

    def reduce(self):
        if self.numerator < 0:
            g = gcd(-self.numerator, self.denominator)
        else:
            g = gcd(self.numerator, self.denominator)
        self.numerator //= g
        self.denominator //= g

    @staticmethod
    def from_str(faction_str):
        numerator, denominator = map(lambda x: int(x), faction_str.split('/'))
        return Fraction(numerator, denominator)

    def __str__(self):
        return "%d/%d" % (self.numerator, self.denominator)


class ExpressionFractionExtractor(object):
    def __init__(self, expression):
        if expression[0] not in {"+", "-"}:
            self.expression = "+" + expression
        else:
            self.expression = expression

    def __iter__(self):
        r = self.expression[0]
        for c in self.expression[1:]:
            if c in {"+", "-"}:
                yield Fraction.from_str(r)
                r = ""
            r += c
        yield Fraction.from_str(r)


class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if len(expression) == 0:
            return 0
        # return list(ExpressionFractionExtractor(expression))
        return str(reduce(lambda x, y: x + y, ExpressionFractionExtractor(expression)))


if __name__ == "__main__":
    print(Solution().fractionAddition("-1/2+1/2"))
    print(Solution().fractionAddition("-1/2+1/2+1/3"))
    print(Solution().fractionAddition("1/3-1/2"))
    print(Solution().fractionAddition("5/3+1/3"))
