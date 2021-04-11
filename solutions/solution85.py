class Solution:
    def maximalRectangle(self, matrix: 'List[List[str]]') -> 'int':
        lm = len(matrix)
        result = 0
        for start in range(lm):
            nums = [0] * (len(matrix[start]) + 1)
            for end in range(start, lm):
                ln = len(matrix[end])
                dp = []
                for index in range(ln + 1):
                    if index != ln:
                        a = int(matrix[end][index])
                        if a == 0:
                            nums[index] = 0
                        else:
                            nums[index] += 1
                    while len(dp) > 0 and nums[dp[-1]] > nums[index]:
                        result = max(result, (index - dp[-1]) * nums[dp[-1]])
                        dp.pop()
                    dp.append(index)
        return result



if __name__ == "__main__":
    matrix = [
        ["1", "0", "1", "1", "1"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "1", "1", "0"]
    ]
    print(Solution().maximalRectangle(matrix))
