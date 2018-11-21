class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
            return 0
        left = timeSeries[0]
        right = left + duration
        result = 0
        for i in range(1, len(timeSeries)):
            if timeSeries[i] <= right:
                right = timeSeries[i] + duration
            else:
                result += right - left
                left, right = timeSeries[i], timeSeries[i] + duration
        result += right - left
        return result


if __name__ == "__main__":
    print(Solution().findPoisonedDuration([1, 4], 2))
    print(Solution().findPoisonedDuration([1, 2], 2))
