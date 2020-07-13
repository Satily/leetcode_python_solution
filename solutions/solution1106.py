class Solution:    
    def parseBoolExpr(self, expression: str) -> bool:
        def parse(expression, start_pos):
            if expression[start_pos] in {'!', '|', '&'}:
                operator = expression[start_pos]
                end_pos = start_pos + 1
                if operator == '&':
                    result = True
                else:
                    result = False
                while expression[end_pos] != ')':
                    (res, end_pos) = parse(expression, end_pos + 1)
                    if operator == '&':
                        result = result and res
                    elif operator == '|':
                        result = result or res
                    else:
                        result = not res
                return result, end_pos + 1
            elif expression[start_pos] == 't':
                return True, start_pos + 1            
            return False, start_pos + 1
        return parse(expression, 0)[0]


if __name__ == "__main__":
    print(Solution().parseBoolExpr("!(f)"))
    print(Solution().parseBoolExpr("|(f,t)"))
    print(Solution().parseBoolExpr("&(t,f)"))
    print(Solution().parseBoolExpr("|(&(t,f,t),!(t))"))
