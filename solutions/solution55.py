class Solution:
    def canJump(self, nums: 'List[int]') -> 'bool':
        ln = len(nums)
        if ln == 0:
            return 0
        current_longest, next_longest = 0, nums[0]
        for i in range(1, ln):
            if i > current_longest:
                current_longest, next_longest = next_longest, i + nums[i]
                if i > current_longest:
                    return False
            else:
                next_longest = max(next_longest, i + nums[i])
        return True


if __name__ == "__main__":
    print(Solution().canJump([2, 3, 1, 1, 4]))
    print(Solution().canJump([3, 2, 1, 0, 4]))
