class Solution:
    def sumSubarrayMins(self, A: 'List[int]') -> int:
        modulo = 1000000007
        A.append(0)
        d_stack = []
        res = 0
        for index, value in enumerate(A):
            while len(d_stack) > 0 and d_stack[-1][0] >= value:
                mid_value, mid_index = d_stack.pop()           
                left = 0 if len(d_stack) == 0 else (d_stack[-1][1] + 1)
                min_distance = min(mid_index - left, index - mid_index - 1)
                res = (res + (((1 + min_distance) * min_distance + (index - left - min_distance * 2) * (min_distance + 1)) * mid_value) % modulo) % modulo
            d_stack.append((value, index))
        return res

if __name__ == "__main__":
    print(Solution().sumSubarrayMins([3,1,2,4]))
    print(Solution().sumSubarrayMins([3,1,2,4,1]))
