class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        if numerator ^ denominator < 0:
            result = '-'
        else:
            result = ''
        numerator = abs(numerator)
        denominator = abs(denominator)

        integer_part = numerator // denominator
        result += str(integer_part)
        numerator = numerator - integer_part * denominator
        if numerator == 0:
            return result
        result += '.'

        rest_map = {}
        decimal_part_result = []

        while numerator != 0 and numerator not in rest_map:
            rest_map[numerator] = len(decimal_part_result)
            numerator *= 10
            decimal_part_result.append(numerator // denominator)
            numerator -= decimal_part_result[-1] * denominator

        if numerator == 0:
            return result + ''.join(map(str, decimal_part_result))
        else:
            return result + ''.join(map(str, decimal_part_result[0:rest_map[numerator]])) + '(' + ''.join(map(str, decimal_part_result[rest_map[numerator]:])) + ')'


if __name__ == '__main__':
    print(Solution().fractionToDecimal(numerator=1, denominator=2))
    print(Solution().fractionToDecimal(numerator=2, denominator=1))
    print(Solution().fractionToDecimal(numerator=2, denominator=3))
    print(Solution().fractionToDecimal(numerator=4, denominator=333))
    print(Solution().fractionToDecimal(numerator=1, denominator=5))
    print(Solution().fractionToDecimal(numerator=7, denominator=30))
