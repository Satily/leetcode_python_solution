import random 


class Solution:
    def sortArray(self, nums: 'List[int]') -> 'List[int]':
        def qsort(nums, left, right):
            if left >= right:
                return
            pivot_index = random.randint(left, right - 1)            
            nums[pivot_index], nums[right - 1] = nums[right - 1], nums[pivot_index]            
            q = left
            for p in range(left, right):
                if nums[p] < nums[right - 1]:
                    nums[p], nums[q] = nums[q], nums[p]
                    q += 1
            nums[q], nums[right - 1] = nums[right - 1], nums[q]
            qsort(nums, left, q)
            qsort(nums, q + 1, right)
        
        qsort(nums, 0, len(nums))
        return nums


if __name__ == "__main__":
    print(Solution().sortArray([5,2,3,1]))
    print(Solution().sortArray([5,1,1,2,0,0]))
