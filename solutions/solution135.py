class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        def scan(ratings):
            result = [0] * len(ratings)
            for index, rating in enumerate(ratings):
                if index != 0 and ratings[index - 1] < rating:
                    result[index] = result[index - 1] + 1
                else:
                    result[index] = 1
            return result

        left = scan(ratings)
        right = list(reversed(scan(list(reversed(ratings)))))
        return sum(map(lambda x: max(x[0], x[1]), zip(left, right)))


if __name__ == "__main__":
    print(Solution().candy([1, 0, 2]))
    print(Solution().candy([1, 2, 2]))
    print(Solution().candy([1, 2, 3, 2, 1]))
    print(Solution().candy([3, 2, 3, 4, 4]))
