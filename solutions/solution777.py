class Solution:
    def canTransform(self, start: 'str', end: 'str') -> 'bool':
        return len(start) == len(end) and 'X' in start and 'X' in end and start.replace('X', '') == end.replace('X', '')


if __name__ == "__main__":
    print(Solution().canTransform("RXXLRXRXL", "XRLXXRRLX"))
    print(Solution().canTransform("XXRXXLXXXX", "XXXXRXXLXX"))
