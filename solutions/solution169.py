import random


class Solution:
    def majorityElement(self, nums: 'List[int]') -> int:
        def partition(nums, left, right, middle):
            pivot = random.randint(left, right - 1)            
            nums[pivot], nums[right - 1] = nums[right - 1], nums[pivot]
            q = left
            for p in range(left, right - 1):
                if nums[p] < nums[right - 1]:
                    nums[q], nums[p] = nums[p], nums[q]
                    q += 1
            nums[q], nums[right - 1] = nums[right - 1], nums[q]
            if middle == q:
                return nums[q]
            elif q < middle:
                return partition(nums, q + 1, right, middle)
            else:
                return partition(nums, left, q, middle)
        return partition(nums, 0, len(nums), len(nums) // 2)


if __name__ == "__main__":
    print(Solution().majorityElement([2,2]))
    print(Solution().majorityElement([3,2,3]))    
    print(Solution().majorityElement([2,2,1,1,1,2,2]))
    