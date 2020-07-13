class Solution:
    def distributeCandies(self, candies: 'List[int]') -> int:
        return min(len(set(candies)), len(candies) // 2)


if __name__ == "__main__":
    print(Solution().distributeCandies([1,1,2,2,3,3]))
    print(Solution().distributeCandies([1,1,2,3]))
