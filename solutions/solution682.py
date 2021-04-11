class Solution:
    def calPoints(self, ops: 'List[str]') -> int:
        s = []
        for op in ops:
            if op == 'C':
                s.pop()
            elif op == 'D':
                s.append(s[-1] * 2)
            elif op == '+':
                s.append(s[-1] + s[-2]) 
            else:
                s.append(int(op))
        return sum(s)

if __name__ == "__main__":
    print(Solution().calPoints(["5","2","C","D","+"]))
    print(Solution().calPoints(["5","-2","4","C","D","9","+","+"]))