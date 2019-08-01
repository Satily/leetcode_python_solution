import random


class Solution:
    def findKthLargest(self, nums: 'List[int]', k: int) -> int:
        def partition(nums, left, right, k):
            #pivot = random.randint(left, right - 1)
            #nums[pivot], nums[right - 1] = nums[right - 1], nums[pivot]
            q = left
            for p in range(left, right - 1):
                if nums[p] > nums[right - 1]:
                    nums[p], nums[q] = nums[q], nums[p]
                    q += 1
            nums[q], nums[right - 1] = nums[right - 1], nums[q]
            if q < k:
                return partition(nums, q + 1, right, k)
            elif q > k:
                return partition(nums, left, q, k)
            else:
                return nums[q]
        return partition(nums, 0, len(nums), k - 1)



if __name__ == "__main__":
    print(Solution().findKthLargest([3,2,1,5,6,4], 2))
    print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))
