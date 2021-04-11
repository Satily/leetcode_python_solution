class Solution:
    def jump(self, nums: 'List[int]') -> 'int':
        ln = len(nums)
        if ln == 0:
            return 0
        current_step, current_longest, next_longest = 0, 0, nums[0]
        for i in range(1, ln):
            if i > current_longest:
                current_step, current_longest, next_longest = current_step + 1, next_longest, i + nums[i]
            else:
                next_longest = max(next_longest, i + nums[i])
        return current_step


if __name__ == "__main__":
    print(Solution().jump([2, 3, 1, 1, 4]))
