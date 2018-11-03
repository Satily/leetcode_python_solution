class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 0:
            return 0
        flowerbed.append(0)
        flowerbed.insert(0, 0)
        empty_flowerbed = 0
        last = flowerbed[0]
        last_count = 1
        for i in range(1, len(flowerbed)):
            if last != flowerbed[i]:
                if last == 0:
                    empty_flowerbed += (last_count - 1) // 2
                last, last_count = flowerbed[i], 1
            else:
                last_count += 1
        if last == 0:
            empty_flowerbed += (last_count - 1) // 2
        return empty_flowerbed >= n


if __name__ == "__main__":
    print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1))
    print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2))
    print(Solution().canPlaceFlowers([0, 0, 1, 0, 1], 1))
