from itertools import product


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def is_vaild_num_str(num_str):
            return 0 <= int(num_str) <= 255 and str(int(num_str)) == num_str

        def split(_s):
            result = []
            for i in range(1, len(_s)):
                if is_vaild_num_str(_s[0:i]) and is_vaild_num_str(_s[i:]):
                    result.append(_s[0: i] + '.' + _s[i:])
            return result

        result = []
        if len(s) <= 12:
            for mid in range(2, len(s) - 1):
                t_result = map(lambda x: '.'.join(x), product(split(s[0:mid]), split(s[mid:])))
                result.extend(t_result)
        return result


if __name__ == "__main__":
    print(Solution().restoreIpAddresses('25525511135'))
    print(Solution().restoreIpAddresses('111'))
    print(Solution().restoreIpAddresses('010010'))
