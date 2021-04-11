class Solution:
    def countSegments(self, s: 'str') -> 'int':
        return len(list(filter(lambda x: x != '', s.split(' '))))


if __name__ == "__main__":
    print(Solution().countSegments("Hello, my  name is John"))
