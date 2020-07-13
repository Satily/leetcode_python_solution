class Solution:
    def twoSum(self, numbers: 'List[int]', target: int) -> 'List[int]':
        p, q = 0, len(numbers) - 1
        while numbers[p] + numbers[q] != target:
            if numbers[p] + numbers[q] > target:
                q -= 1
            else:
                p += 1
        return [p + 1, q + 1]


if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,15], 9))