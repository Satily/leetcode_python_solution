# Time Limit Exceeded
# Need force pruning? That's crazy!
class Solution:
    def fourSum(self, nums: 'List[int]', target: int) -> 'List[List[int]]':
        nums.sort()
        ln = len(nums)
        result = []
        for i in range(0, ln - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, ln - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, l = j + 1, ln - 1
                while k < l:
                    line = list(map(lambda x: nums[x], [i, j, k, l]))
                    s = sum(line)
                    if s > target:
                        l -= 1
                    elif s < target:
                        k += 1
                    else:
                        result.append(line)
                        k += 1
                        while k < l and nums[k - 1] == nums[k]:
                            k += 1
        return result


if __name__ == "__main__":
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
    print(Solution().fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
