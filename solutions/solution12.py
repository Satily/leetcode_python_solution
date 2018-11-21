class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = [
            ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
            ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            ['', 'M', 'MM', 'MMM',   '',  '',   '',    '',     '',   ''],
        ]
        result = ''
        index = 0
        while num != 0:
            result = dic[index][num % 10] + result
            index += 1
            num //= 10
        return result


if __name__ == "__main__":
    print(Solution().intToRoman(3))
    print(Solution().intToRoman(4))
    print(Solution().intToRoman(9))
    print(Solution().intToRoman(58))
    print(Solution().intToRoman(1994))
