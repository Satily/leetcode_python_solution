class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: int) -> int:
        nums.sort()
        ln = len(nums)
        result = nums[0] + nums[1] + nums[2]
        for i in range(0, ln - 2):
            j, k = i + 1, ln - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > target:
                    k -= 1
                elif s < target:
                    j += 1
                elif s == target:
                    return s
                if abs(result - target) > abs(s - target):
                    result = s
        return result


if __name__ == "__main__":
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
