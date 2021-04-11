class Solution:
    def productExceptSelf(self, nums: 'List[int]') -> 'List[int]':
        result = [1]
        for num in nums[:-1]:
            result.append(num * result[-1])
        s = 1
        for index in reversed(range(len(nums) - 1)):
            s *= nums[index + 1]
            result[index] *= s
        return result


if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3, 4]))
