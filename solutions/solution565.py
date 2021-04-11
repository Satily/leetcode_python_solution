class Solution:
    def arrayNesting(self, nums: 'List[int]') -> int:
        m = len(nums)
        flag = [False] * m
        result = 0
        for index in range(m):
            if not flag[index]:
                step = 0
                current_index = index
                while not flag[current_index]:
                    step += 1
                    flag[current_index] = True
                    current_index = nums[current_index]
                result = max(result, step)
        return result


if __name__ == "__main__":
    print(Solution().arrayNesting([5,4,0,3,1,6,2]))
