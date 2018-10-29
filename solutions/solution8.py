class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        max_int = 2147483647
        min_int = -2147483648
        num_set = set('0123456789')
        prefix_space_flag = True
        is_positive = True
        result = 0
        for c in str:
            if prefix_space_flag:
                if c != ' ':
                    prefix_space_flag = False
                    if c == '-':
                        is_positive = False
                        continue
                    elif c == '+':
                        continue
            if not prefix_space_flag:
                if c in num_set:
                    result = result * 10 + int(c)
                else:
                    break
        if not is_positive:
            result = -result
        if result > max_int:
            result = max_int
        elif result < min_int:
            result = min_int
        return result


if __name__ == "__main__":
    print(Solution().myAtoi('42'))
    print(Solution().myAtoi('   -42'))
    print(Solution().myAtoi('4193 with words'))
    print(Solution().myAtoi('words and 987'))
    print(Solution().myAtoi('-91283472332'))
