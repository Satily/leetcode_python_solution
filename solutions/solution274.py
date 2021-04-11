class Solution:
    def hIndex(self, citations: 'List[int]') -> int:
        for index, citation in enumerate(reversed(sorted(citations))):
            if index + 1 > citation:
                return index
        return len(citations)


if __name__ == "__main__":
    print(Solution().hIndex([3, 0, 6, 1, 5]))
    print(Solution().hIndex([4, 0, 6, 1, 5]))
    print(Solution().hIndex([2, 0, 6, 1, 5]))
    print(Solution().hIndex([10, 9, 8, 7, 6]))
