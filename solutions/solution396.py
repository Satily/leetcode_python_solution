class Solution:
    def maxRotateFunction(self, nums: 'List[int]') -> int:
        list_sum = sum(nums)
        weighted_sum = sum([index * num for index, num in enumerate(nums)])
        result = weighted_sum
        for num in reversed(nums):
            weighted_sum += list_sum - num * len(nums)
            result = max(result, weighted_sum)
        return result


if __name__ == '__main__':
    print(Solution().maxRotateFunction([4, 3, 2, 6]))
    print(Solution().maxRotateFunction([100]))
