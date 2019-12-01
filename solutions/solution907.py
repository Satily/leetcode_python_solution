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
            
            


        # def cal_min(A, left, right):
        #     if left >= right:
        #         return 0
        #     if right - left == 1:
        #         return A[left]
        #     min_index = left
        #     for index in range(left + 1, right):
        #         if A[index] < A[min_index]:
        #             min_index = index
        #     a_index = min(min_index - left, right - min_index - 1)
        #     min_res = (((1 + a_index) * a_index + (right - left - a_index * 2) * (a_index + 1)) * A[min_index]) % modulo
        #     return (min_res + cal_min(A, left, min_index) + cal_min(A, min_index + 1, right)) % modulo

        # return cal_min(A, 0, len(A))


if __name__ == "__main__":
    print(Solution().sumSubarrayMins([3,1,2,4]))
    print(Solution().sumSubarrayMins([3,1,2,4,1]))
