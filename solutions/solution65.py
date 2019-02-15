class Solution:
    def isNumber(self, s: 'str') -> 'bool':
        def check_int(p: 'str') -> 'bool':
            if len(p) == 0:
                return False
            for pc in p:
                if pc not in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                    return False
            return True

        def check_signed_int(p: 'str') -> 'bool':
            if len(p) == 0:
                return False
            if p[0] in {'+', '-'}:
                p = p[1:]
            return check_int(p)

        def check_float(p: 'str') -> 'bool':
            if len(p) == 0:
                return False
            if p[0] in {'+', '-'}:
                p = p[1:]
            if len(p) == 0 or p == '.':
                return False
            sp = p.split('.')
            lsp = len(sp)
            if lsp > 2 or lsp == 0:
                return False
            for pp in sp:
                if not check_int(pp) and pp != '':
                    return False
            return True

        ss = s.strip().split('e')
        lss = len(ss)
        if lss > 2 or lss == 0:
            return False
        if not check_float(ss[0]):
            return False
        if lss == 2 and not check_signed_int(ss[1]):
            return False
        return True


if __name__ == "__main__":
    # print(Solution().isNumber("0"))
    # print(Solution().isNumber(" 0.1 "))
    # print(Solution().isNumber("abc"))
    # print(Solution().isNumber("1 a"))
    # print(Solution().isNumber("2e10"))
    # print(Solution().isNumber(" -90e3   "))
    # print(Solution().isNumber(" 1e"))
    # print(Solution().isNumber("e3"))
    # print(Solution().isNumber(" 6e-1"))
    # print(Solution().isNumber(" 99e2.5 "))
    # print(Solution().isNumber("53.5e93"))
    # print(Solution().isNumber(" --6 "))
    # print(Solution().isNumber("-+3"))
    # print(Solution().isNumber("95a54e53"))
    # print(Solution().isNumber(".1"))
    print(Solution().isNumber("-e58 "))

