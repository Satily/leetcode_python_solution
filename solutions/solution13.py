class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        special_pair = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        ls = len(s)
        index = 0
        result = 0
        while index < ls:
            if s[index: index + 2] in special_pair:
                result += special_pair[s[index: index + 2]]
                index += 2
            else:
                result += roman_dict[s[index]]
                index += 1
        return result


if __name__ == "__main__":
    print(Solution().romanToInt('III'))
    print(Solution().romanToInt('IV'))
    print(Solution().romanToInt('IX'))
    print(Solution().romanToInt('LVIII'))
    print(Solution().romanToInt('MCMXCIV'))
