class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        is_positive = True
        if dividend < 0:
            is_positive = not is_positive
            dividend = -dividend
        if divisor < 0:
            is_positive = not is_positive
            divisor = -divisor
        if divisor == 1:
            result = dividend
        else:
            powers = [divisor]
            powers_2 = [1]
            while powers[-1:][0] <= dividend:
                powers.append(powers[-1:][0] + powers[-1:][0])
                powers_2.append(powers_2[-1:][0] + powers_2[-1:][0])
            powers.pop()
            powers_2.pop()
            powers.reverse()
            powers_2.reverse()
            result = 0
            for i in range(0, len(powers)):
                if dividend >= powers[i]:
                    dividend -= powers[i]
                    result += powers_2[i]
        if not is_positive:
            result = -result
        if result > 2147483647:
            result = 2147483647
        elif result < -2147483648:
            result = -2147483648
        return result


if __name__ == "__main__":
    # print(Solution().divide(1, 1))
    # print(Solution().divide(1, -1))
    print(Solution().divide(2, 2))
    print(Solution().divide(10, 3))
    print(Solution().divide(7, -3))
